const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 80;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// SQLite DB
const db = new sqlite3.Database('/data/leads.db', (err) => {
  if (err) {
    console.error('DB open error:', err.message);
    // Fallback to local file if /data isn't available
    return;
  }
  console.log('Connected to SQLite database.');
});

// If /data failed, use local
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
    res.json({ success: true, id: this.lastID });
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
