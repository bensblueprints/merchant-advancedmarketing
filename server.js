const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 80;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Email transporter (configured via env vars)
let transporter = null;
if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
  transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT || '587'),
    secure: process.env.SMTP_SECURE === 'true',
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });
  console.log('Email transporter configured.');
} else {
  console.log('Email not configured. Set SMTP_HOST, SMTP_USER, SMTP_PASS env vars to enable.');
}

const FUNDING_URL = 'https://my.americasfundingexperts.com/?id=1820217000240009008';
const FROM_EMAIL = process.env.FROM_EMAIL || 'contact@advancedmarketing.co';

function sendConfirmationEmail(to, name, loanType) {
  if (!transporter) {
    console.log('No email transporter. Skipping confirmation email.');
    return Promise.resolve(false);
  }
  const loanName = loanType ? loanType.replace(/-/g, ' ').toUpperCase() : 'BUSINESS FUNDING';
  const mailOptions = {
    from: `"Advanced Marketing Co." <${FROM_EMAIL}>`,
    to,
    subject: 'Your Funding Application — Next Steps',
    html: `
      <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#1e293b;">
        <div style="background:#0f172a;padding:24px;text-align:center;">
          <h1 style="color:#c9a44c;margin:0;font-size:22px;">Advanced Marketing Co.</h1>
          <p style="color:#cbd5e1;margin:6px 0 0;font-size:13px;">Business Funding & Payment Solutions</p>
        </div>
        <div style="padding:24px;background:#ffffff;">
          <p style="font-size:16px;">Hi ${name || 'there'},</p>
          <p>Thank you for submitting your ${loanName} quote request. We've received your information and a funding advisor will review it shortly.</p>
          <p><strong>Next step:</strong> Complete your official funding application to get matched with lenders instantly.</p>
          <div style="text-align:center;margin:28px 0;">
            <a href="${FUNDING_URL}" style="background:#0f172a;color:#c9a44c;padding:14px 28px;text-decoration:none;border-radius:6px;font-weight:700;display:inline-block;">Complete My Application</a>
          </div>
          <p style="font-size:13px;color:#64748b;">If the button doesn't work, copy and paste this link:<br>${FUNDING_URL}</p>
          <hr style="border:none;border-top:1px solid #e2e8f0;margin:24px 0;">
          <p style="font-size:13px;color:#64748b;"><strong>Questions?</strong> Reply to this email or call us. We're here to help.</p>
          <p style="font-size:13px;color:#64748b;">Please check your inbox (and spam folder) for updates from our lending partners.</p>
        </div>
        <div style="background:#f8fafc;padding:16px;text-align:center;font-size:12px;color:#94a3b8;">
          &copy; 2026 Advanced Marketing Co. Ltd. Not a direct lender.
        </div>
      </div>
    `
  };
  return transporter.sendMail(mailOptions)
    .then(info => {
      console.log('Email sent:', info.messageId);
      return true;
    })
    .catch(err => {
      console.error('Email error:', err.message);
      return false;
    });
}

// SQLite DB
const db = new sqlite3.Database('/data/leads.db', (err) => {
  if (err) {
    console.error('DB open error:', err.message);
    return;
  }
  console.log('Connected to SQLite database.');
});

const dbPath = db.open ? '/data/leads.db' : path.join(__dirname, 'leads.db');
const db2 = new sqlite3.Database(dbPath);

db2.serialize(() => {
  db2.run(`CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_type TEXT,
    first_name TEXT,
    last_name TEXT,
    business_name TEXT,
    email TEXT,
    phone TEXT,
    monthly_revenue TEXT,
    time_in_business TEXT,
    credit_score TEXT,
    funding_amount TEXT,
    notes TEXT,
    ip TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);
});

// Health check
app.get('/health', (req, res) => res.json({ status: 'ok' }));

// Submit lead
app.post('/api/lead', (req, res) => {
  const {
    loan_type, first_name, last_name, business_name,
    email, phone, monthly_revenue, time_in_business,
    credit_score, funding_amount, notes
  } = req.body;

  if (!first_name || !last_name || !business_name || !email || !phone) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const sql = `INSERT INTO leads
    (loan_type, first_name, last_name, business_name, email, phone, monthly_revenue, time_in_business, credit_score, funding_amount, notes, ip)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;

  db2.run(sql, [
    loan_type || 'general',
    first_name, last_name, business_name,
    email, phone,
    monthly_revenue || '',
    time_in_business || '',
    credit_score || '',
    funding_amount || '',
    notes || '',
    req.ip || req.headers['x-forwarded-for'] || ''
  ], function(err) {
    if (err) {
      console.error('Insert error:', err);
      return res.status(500).json({ error: 'Database error' });
    }
    const id = this.lastID;

    // Fire confirmation email asynchronously
    sendConfirmationEmail(email, first_name, loan_type);

    res.json({ success: true, id, funding_url: FUNDING_URL });
  });
});

// Basic auth middleware
function basicAuth(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth) {
    res.set('WWW-Authenticate', 'Basic realm="Admin"');
    return res.status(401).send('Authentication required');
  }
  const [user, pass] = Buffer.from(auth.split(' ')[1], 'base64').toString().split(':');
  if (user === 'admin' && pass === 'admin') {
    return next();
  }
  res.set('WWW-Authenticate', 'Basic realm="Admin"');
  res.status(401).send('Invalid credentials');
}

// Admin API
app.get('/api/admin/leads', basicAuth, (req, res) => {
  const { search, loan_type, page = 1, limit = 50 } = req.query;
  let sql = 'SELECT * FROM leads WHERE 1=1';
  const params = [];

  if (search) {
    sql += ` AND (first_name LIKE ? OR last_name LIKE ? OR business_name LIKE ? OR email LIKE ? OR phone LIKE ?)`;
    const like = `%${search}%`;
    params.push(like, like, like, like, like);
  }
  if (loan_type && loan_type !== 'all') {
    sql += ' AND loan_type = ?';
    params.push(loan_type);
  }
  sql += ' ORDER BY created_at DESC LIMIT ? OFFSET ?';
  params.push(parseInt(limit), (parseInt(page) - 1) * parseInt(limit));

  db2.all(sql, params, (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

app.get('/api/admin/stats', basicAuth, (req, res) => {
  db2.get('SELECT COUNT(*) as total FROM leads', [], (err, totalRow) => {
    if (err) return res.status(500).json({ error: err.message });
    db2.all('SELECT loan_type, COUNT(*) as count FROM leads GROUP BY loan_type', [], (err, typeRows) => {
      if (err) return res.status(500).json({ error: err.message });
      db2.get('SELECT COUNT(*) as today FROM leads WHERE date(created_at) = date("now")', [], (err, todayRow) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({
          total: totalRow.total,
          today: todayRow.today,
          by_type: typeRows
        });
      });
    });
  });
});

app.delete('/api/admin/leads/:id', basicAuth, (req, res) => {
  db2.run('DELETE FROM leads WHERE id = ?', [req.params.id], function(err) {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ success: true, deleted: this.changes });
  });
});

// Admin panel HTML
app.get('/admin', basicAuth, (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'admin.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});
