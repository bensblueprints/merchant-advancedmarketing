import os

FUNDING_URL = 'https://my.americasfundingexperts.com/?id=1820217000240009008'

STATE_NAMES = {
    'ak': 'Alaska', 'al': 'Alabama', 'ar': 'Arkansas', 'az': 'Arizona',
    'ca': 'California', 'co': 'Colorado', 'ct': 'Connecticut', 'de': 'Delaware',
    'fl': 'Florida', 'ga': 'Georgia', 'hi': 'Hawaii', 'ia': 'Iowa',
    'id': 'Idaho', 'il': 'Illinois', 'in': 'Indiana', 'ks': 'Kansas',
    'ky': 'Kentucky', 'la': 'Louisiana', 'ma': 'Massachusetts', 'md': 'Maryland',
    'me': 'Maine', 'mi': 'Michigan', 'mn': 'Minnesota', 'mo': 'Missouri',
    'ms': 'Mississippi', 'mt': 'Montana', 'nc': 'North Carolina', 'nd': 'North Dakota',
    'ne': 'Nebraska', 'nh': 'New Hampshire', 'nj': 'New Jersey', 'nm': 'New Mexico',
    'nv': 'Nevada', 'ny': 'New York', 'oh': 'Ohio', 'ok': 'Oklahoma',
    'or': 'Oregon', 'pa': 'Pennsylvania', 'ri': 'Rhode Island', 'sc': 'South Carolina',
    'sd': 'South Dakota', 'tn': 'Tennessee', 'tx': 'Texas', 'ut': 'Utah',
    'va': 'Virginia', 'vt': 'Vermont', 'wa': 'Washington', 'wi': 'Wisconsin',
    'wv': 'West Virginia', 'wy': 'Wyoming'
}

LOAN_TYPES = {
    'mca': {
        'name': 'Merchant Cash Advance',
        'short': 'MCA',
        'amount_range': '$5,000 to $500,000',
        'speed': '24 hours',
        'term': '3 to 18 months',
        'credit_req': 'No minimum FICO',
        'revenue_req': '$8,000+/month',
        'repayment': 'Small percentage of daily sales',
        'best_for': 'Businesses with consistent card sales needing fast capital.',
        'features': [
            'Approval in as little as 2 hours',
            'Funding from $5,000 to $500,000',
            'Soft credit pull only',
            'No collateral required',
            'Flexible daily repayment',
            'Use for inventory, payroll, expansion, or equipment'
        ],
        'industries': 'restaurants, retail shops, auto repair, medical practices, salons, contractors, and e-commerce stores',
        'meta_desc': 'Get a merchant cash advance in {loc}. Fast approval, bad credit OK. Revenue-based funding up to $500K. Apply in 2 minutes.'
    },
    'term-loan': {
        'name': 'Business Term Loan',
        'short': 'Term Loan',
        'amount_range': '$25,000 to $5,000,000',
        'speed': '48-72 hours',
        'term': '6 to 60 months',
        'credit_req': '650+ preferred',
        'revenue_req': '$15,000+/month',
        'repayment': 'Fixed monthly payments',
        'best_for': 'Established businesses making large investments or acquisitions.',
        'features': [
            'Fixed interest rates with predictable payments',
            'Loan amounts from $25K up to $5M',
            'Terms from 6 to 60 months',
            'No prepayment penalties on most programs',
            'Full lump sum upfront',
            'Ideal for expansion, acquisition, or debt consolidation'
        ],
        'industries': 'manufacturing, professional services, healthcare, construction, logistics, and franchise owners',
        'meta_desc': 'Business term loans in {loc}. Fixed rates, predictable payments. $25K to $5M. Apply now for fast approval.'
    },
    'sba': {
        'name': 'SBA Loan',
        'short': 'SBA',
        'amount_range': '$50,000 to $5,000,000',
        'speed': '30-60 days',
        'term': 'Up to 25 years',
        'credit_req': '680+ preferred',
        'revenue_req': 'Strong 2+ year history',
        'repayment': 'Low fixed monthly payments',
        'best_for': 'Businesses seeking the lowest rates with patient capital needs.',
        'features': [
            'Government-backed rates from prime + 2.75%',
            'Terms up to 25 years for real estate',
            'We handle all SBA paperwork and packaging',
            'Work with SBA-preferred lenders only',
            '7(a) and 504 programs available',
            'Full documentation prep included'
        ],
        'industries': 'real estate investors, healthcare practices, manufacturers, restaurants, and professional service firms',
        'meta_desc': 'SBA loans in {loc}. Low-rate government-backed financing. We handle all paperwork. 7(a) and 504 programs. Apply today.'
    },
    'equipment': {
        'name': 'Equipment Financing',
        'short': 'Equipment',
        'amount_range': 'Up to $1,000,000',
        'speed': '24-48 hours',
        'term': '24 to 84 months',
        'credit_req': '600+',
        'revenue_req': 'Varies by equipment cost',
        'repayment': 'Fixed monthly payments',
        'best_for': 'Businesses purchasing machinery, vehicles, or technology.',
        'features': [
            'Finance 100% of equipment cost including soft costs',
            'The equipment itself is the collateral',
            'Terms from 24 to 84 months',
            'New and used equipment OK',
            'Lease-to-own options available',
            'Fast approval for most industries'
        ],
        'industries': 'construction, medical practices, restaurants, manufacturing, transportation, and technology companies',
        'meta_desc': 'Equipment financing in {loc}. Finance 100% of cost. New or used equipment. Up to $1M. Fast approval. Apply now.'
    },
    'loc': {
        'name': 'Business Line of Credit',
        'short': 'Line of Credit',
        'amount_range': '$10,000 to $250,000',
        'speed': 'Same-day draw',
        'term': 'Revolving',
        'credit_req': '600+',
        'revenue_req': '$10,000+/month',
        'repayment': 'Interest-only on what you use',
        'best_for': 'Businesses managing cash flow gaps and seasonal swings.',
        'features': [
            'Credit lines from $10K to $250K',
            'Draw funds same-day via ACH or wire',
            'Only pay interest on what you use',
            'Reuse the line as you repay',
            'No reapplication needed',
            'Perfect for seasonal businesses'
        ],
        'industries': 'retail, hospitality, construction, professional services, and any business with fluctuating cash flow',
        'meta_desc': 'Business line of credit in {loc}. Revolving credit up to $250K. Same-day access. Only pay for what you use. Apply now.'
    },
    'processing': {
        'name': 'Credit Card Processing',
        'short': 'Processing',
        'amount_range': 'N/A',
        'speed': 'Next-day funding',
        'term': 'Month-to-month',
        'credit_req': 'None',
        'revenue_req': 'Any card-accepting business',
        'repayment': 'Per-transaction fee',
        'best_for': 'Any business accepting card payments wanting lower rates.',
        'features': [
            'Free, no-obligation rate audit',
            'Average savings of 20-40% per month',
            'Next-day funding standard',
            'Free terminal or POS upgrade',
            'No cancellation fees',
            'E-commerce and online payments included'
        ],
        'industries': 'retail stores, restaurants, medical practices, e-commerce, salons, and any business that accepts cards',
        'meta_desc': 'Lower your credit card processing rates in {loc}. Free audit. Save 20-40%. Next-day funding. No cancellation fees.'
    },
    'invoice-factoring': {
        'name': 'Invoice Factoring',
        'short': 'Invoice Factoring',
        'amount_range': 'Up to 90% of invoice value',
        'speed': '24 hours',
        'term': 'Until customer pays',
        'credit_req': 'No minimum',
        'revenue_req': 'B2B with outstanding invoices',
        'repayment': 'Factor fee deducted from advance',
        'best_for': 'B2B businesses waiting 30-90 days for customer payment.',
        'features': [
            'Advance up to 90% of invoice value',
            'Funding within 24 hours of submission',
            'No new debt — this is not a loan',
            'We handle collections professionally',
            'Recourse and non-recourse options',
            'Spot factoring available'
        ],
        'industries': 'construction, manufacturing, staffing agencies, trucking, wholesale distributors, and government contractors',
        'meta_desc': 'Invoice factoring in {loc}. Get paid on your invoices now. Advance up to 90%. No new debt. B2B funding. Apply today.'
    }
}

def title_case(s):
    return ' '.join(w.capitalize() for w in s.replace('-', ' ').split())

def city_display(city_slug):
    return title_case(city_slug)

def generate_state_page(state_code, loan_key, loan):
    state_name = STATE_NAMES[state_code]
    cities_in_state = []
    state_dir = f'public/cities/{state_code}'
    if os.path.exists(state_dir):
        cities_in_state = sorted([f.replace('.html', '') for f in os.listdir(state_dir) if f.endswith('.html')])

    city_links = ''
    if cities_in_state:
        city_links += f'<h3 style="margin-top:48px;margin-bottom:20px;">Popular Cities in {state_name}</h3><div class="local-list">'
        for c in cities_in_state[:24]:
            city_links += f'<a href="/loans/{loan_key}/{state_code}/{c}.html" class="local-item">{city_display(c)}</a>'
        city_links += '</div>'

    features_html = ''.join(f'<li>{f}</li>' for f in loan['features'])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{loan['name']} in {state_name} | Fast Approval for {loan['short']}</title>
<meta name="description" content="{loan['meta_desc'].format(loc=state_name)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="header">
<div class="container">
<div class="header-inner">
<a href="/" class="logo"><div class="logo-mark">AM</div><div class="logo-text">Advanced Marketing Co.<span>Business Funding & Payments</span></div></a>
<nav class="nav">
<a href="/loans/mca.html">Cash Advance</a>
<a href="/loans/term-loan.html">Term Loans</a>
<a href="/loans/sba.html">SBA Loans</a>
<a href="/loans/equipment.html">Equipment</a>
<a href="/loans/processing.html">Processing</a>
<a href="/loans/loc.html">LOC</a>
<a href="/loans/invoice-factoring.html">Factoring</a>
</nav>
</div>
</div>
</header>

<div class="breadcrumb"><div class="container"><a href="/">Home</a> &rsaquo; <a href="/loans/{loan_key}.html">{loan['name']}</a> &rsaquo; {state_name}</div></div>

<section class="loan-hero">
<div class="container">
<div class="loan-hero-grid">
<div>
<h1>{loan['name']} in {state_name}</h1>
<p>Businesses across {state_name} need flexible financing to grow, hire, and compete. Our {loan['name']} program is built for {state_name} businesses of all sizes. Amounts range from {loan['amount_range']}. Funding as fast as {loan['speed']}.</p>
<ul class="loan-highlights">
<li><span style="color:var(--gold);">&#9733;</span> Amounts: {loan['amount_range']}</li>
<li><span style="color:var(--gold);">&#9733;</span> Funding speed: {loan['speed']}</li>
<li><span style="color:var(--gold);">&#9733;</span> Terms: {loan['term']}</li>
<li><span style="color:var(--gold);">&#9733;</span> {loan['credit_req']}</li>
</ul>
<a href="{FUNDING_URL}" class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>
<p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>
</div>
<div class="loan-img">
<img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=900&auto=format&fit=crop&q=80" alt="{loan['name']} for {state_name} businesses">
</div>
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="section-header">
<h2>Why {state_name} Businesses Choose {loan['name']}</h2>
<p>Our lending partners understand the {state_name} market and work with {loan['industries']}.</p>
</div>
<div class="cards-grid">
<div class="card">
<h3>How It Works</h3>
<p>{loan['best_for']} {loan['name']} offers {loan['amount_range']} with {loan['repayment']}. The application takes under 5 minutes and most decisions come back within hours.</p>
</div>
<div class="card">
<h3>Requirements</h3>
<p>Unlike traditional banks, our lending partners look at your business performance, not just your credit score:</p>
<ul style="margin-top:12px;padding-left:20px;color:var(--gray-500);">
{features_html}
</ul>
</div>
<div class="card">
<h3>Common Uses</h3>
<p>{loan['industries']} in {state_name} use {loan['name']} for working capital, payroll, inventory, equipment, marketing campaigns, expansion, and bridging seasonal gaps.</p>
</div>
</div>
{city_links}
</div>
</section>

<section class="section section-alt" id="apply">
<div class="container">
<div class="form-wrap">
<h2>Prefer a Callback?</h2>
<p>Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.</p>
<form id="leadForm">
<input type="hidden" name="loan_type" value="{loan_key}">
<div class="form-grid">
<div class="form-group"><label for="firstName">First Name *</label><input type="text" id="firstName" name="first_name" required placeholder="John"></div>
<div class="form-group"><label for="lastName">Last Name *</label><input type="text" id="lastName" name="last_name" required placeholder="Smith"></div>
<div class="form-group full"><label for="businessName">Business Name *</label><input type="text" id="businessName" name="business_name" required placeholder="Smith's LLC"></div>
<div class="form-group"><label for="email">Business Email *</label><input type="email" id="email" name="email" required placeholder="john@business.com"></div>
<div class="form-group"><label for="phone">Phone *</label><input type="tel" id="phone" name="phone" required placeholder="(555) 123-4567"></div>
<div class="form-group"><label for="monthlyRevenue">Monthly Revenue *</label>
<select id="monthlyRevenue" name="monthly_revenue" required>
<option value="">Select...</option>
<option value="Under $10K">Under $10,000</option>
<option value="$10K - $25K">$10,000 - $25,000</option>
<option value="$25K - $50K">$25,000 - $50,000</option>
<option value="$50K - $100K">$50,000 - $100,000</option>
<option value="$100K - $250K">$100,000 - $250,000</option>
<option value="$250K+">$250,000+</option>
</select></div>
<div class="form-group"><label for="timeInBusiness">Time in Business *</label>
<select id="timeInBusiness" name="time_in_business" required>
<option value="">Select...</option>
<option value="Startup">Startup</option>
<option value="0-6 months">0 - 6 months</option>
<option value="6-12 months">6 - 12 months</option>
<option value="1-2 years">1 - 2 years</option>
<option value="2-5 years">2 - 5 years</option>
<option value="5+ years">5+ years</option>
</select></div>
<div class="form-group full"><label for="notes">Additional Details</label><textarea id="notes" name="notes" placeholder="Tell us about your funding needs..."></textarea></div>
</div>
<button type="submit" class="btn btn-primary btn-lg submit-btn">Request a Callback &rarr;</button>
<p class="form-note">&#128274; Your information is secure and encrypted. No hard credit inquiry.</p>
</form>
</div>
</div>
</section>

<footer class="footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand"><h3>Advanced Marketing Co.</h3><p>Connecting businesses with the funding and payment solutions they need to grow.</p></div>
<div class="footer-col">
<h4>Funding</h4>
<a href="/loans/mca.html">Merchant Cash Advance</a>
<a href="/loans/term-loan.html">Business Term Loan</a>
<a href="/loans/sba.html">SBA Loan</a>
<a href="/loans/equipment.html">Equipment Financing</a>
<a href="/loans/loc.html">Line of Credit</a>
</div>
<div class="footer-col">
<h4>Payments</h4>
<a href="/loans/processing.html">Card Processing</a>
<a href="/loans/invoice-factoring.html">Invoice Factoring</a>
</div>
<div class="footer-col">
<h4>Company</h4>
<a href="/">Home</a>
<a href="/admin">Partner Portal</a>
<a href="mailto:contact@advancedmarketing.co">Contact</a>
</div>
</div>
<div class="footer-bottom"><p>&copy; 2026 Advanced Marketing Co. Ltd. Not a direct lender.</p></div>
</div>
</footer>

<div class="toast" id="toast"><span>&#10003;</span><span id="toastMsg">Application received!</span></div>

<script>
document.getElementById('leadForm').addEventListener('submit', async function(e) {{
  e.preventDefault();
  const btn = e.target.querySelector('.submit-btn');
  const original = btn.innerHTML;
  btn.innerHTML = 'Submitting...'; btn.disabled = true;
  const data = Object.fromEntries(new FormData(e.target).entries());
  try {{
    const res = await fetch('/api/lead', {{ method: 'POST', headers: {{'Content-Type':'application/json'}}, body: JSON.stringify(data) }});
    const json = await res.json();
    if (json.success) {{
      showToast('Thanks! Check your email for next steps. Redirecting to application...');
      setTimeout(() => {{ window.location.href = json.funding_url || '{FUNDING_URL}'; }}, 2000);
    }} else {{
      showToast('Error. Please try again.');
      btn.innerHTML = original; btn.disabled = false;
    }}
  }} catch {{
    showToast('Network error. Please try again.');
    btn.innerHTML = original; btn.disabled = false;
  }}
}});
function showToast(msg) {{ const t=document.getElementById('toast'); document.getElementById('toastMsg').textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),5000); }}
</script>
</body>
</html>
'''

def generate_city_page(state_code, city_slug, loan_key, loan):
    state_name = STATE_NAMES[state_code]
    city_name = city_display(city_slug)
    loc = f"{city_name}, {state_name}"

    features_html = ''.join(f'<li>{f}</li>' for f in loan['features'])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{loan['name']} in {loc} | {loan['short']} Funding</title>
<meta name="description" content="{loan['meta_desc'].format(loc=loc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="header">
<div class="container">
<div class="header-inner">
<a href="/" class="logo"><div class="logo-mark">AM</div><div class="logo-text">Advanced Marketing Co.<span>Business Funding & Payments</span></div></a>
<nav class="nav">
<a href="/loans/mca.html">Cash Advance</a>
<a href="/loans/term-loan.html">Term Loans</a>
<a href="/loans/sba.html">SBA Loans</a>
<a href="/loans/equipment.html">Equipment</a>
<a href="/loans/processing.html">Processing</a>
<a href="/loans/loc.html">LOC</a>
<a href="/loans/invoice-factoring.html">Factoring</a>
</nav>
</div>
</div>
</header>

<div class="breadcrumb"><div class="container"><a href="/">Home</a> &rsaquo; <a href="/loans/{loan_key}.html">{loan['name']}</a> &rsaquo; <a href="/loans/{loan_key}/{state_code}.html">{state_name}</a> &rsaquo; {city_name}</div></div>

<section class="loan-hero">
<div class="container">
<div class="loan-hero-grid">
<div>
<h1>{loan['name']} in {city_name}, <span>{state_name}</span></h1>
<p>If you run a business in {city_name}, you know that access to working capital can make or break your growth. We connect {city_name} business owners with {loan['name']} options designed for their specific needs. {loan['amount_range']}. Funding as fast as {loan['speed']}.</p>
<ul class="loan-highlights">
<li><span style="color:var(--gold);">&#9733;</span> Amounts: {loan['amount_range']}</li>
<li><span style="color:var(--gold);">&#9733;</span> Funding speed: {loan['speed']}</li>
<li><span style="color:var(--gold);">&#9733;</span> {loan['credit_req']}</li>
<li><span style="color:var(--gold);">&#9733;</span> Works with {loan['industries']}</li>
</ul>
<a href="{FUNDING_URL}" class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>
<p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>
</div>
<div class="loan-img">
<img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=900&auto=format&fit=crop&q=80" alt="{loan['name']} for {loc} businesses">
</div>
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="section-header">
<h2>{loan['name']} for {city_name} Businesses</h2>
<p>Our lending partners work with {loan['industries']} throughout {city_name} and surrounding areas.</p>
</div>
<div class="cards-grid">
<div class="card">
<h3>How It Works</h3>
<p>{loan['best_for']} Apply online in under 5 minutes. Most {city_name} applicants receive a decision within hours. Once approved, funds are deposited directly to your business account.</p>
</div>
<div class="card">
<h3>Requirements</h3>
<p>Unlike traditional banks, our lending partners look at your business performance, not just your credit score:</p>
<ul style="margin-top:12px;padding-left:20px;color:var(--gray-500);">
{features_html}
</ul>
</div>
<div class="card">
<h3>Popular Uses in {city_name}</h3>
<p>Local businesses use {loan['name']} for working capital, payroll coverage, inventory purchases, marketing campaigns, equipment upgrades, expansion projects, and managing seasonal cash flow gaps.</p>
</div>
</div>
</div>
</section>

<section class="section section-alt" id="apply">
<div class="container">
<div class="form-wrap">
<h2>Prefer a Callback?</h2>
<p>Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.</p>
<form id="leadForm">
<input type="hidden" name="loan_type" value="{loan_key}">
<div class="form-grid">
<div class="form-group"><label for="firstName">First Name *</label><input type="text" id="firstName" name="first_name" required placeholder="John"></div>
<div class="form-group"><label for="lastName">Last Name *</label><input type="text" id="lastName" name="last_name" required placeholder="Smith"></div>
<div class="form-group full"><label for="businessName">Business Name *</label><input type="text" id="businessName" name="business_name" required placeholder="Smith's LLC"></div>
<div class="form-group"><label for="email">Business Email *</label><input type="email" id="email" name="email" required placeholder="john@business.com"></div>
<div class="form-group"><label for="phone">Phone *</label><input type="tel" id="phone" name="phone" required placeholder="(555) 123-4567"></div>
<div class="form-group"><label for="monthlyRevenue">Monthly Revenue *</label>
<select id="monthlyRevenue" name="monthly_revenue" required>
<option value="">Select...</option>
<option value="Under $10K">Under $10,000</option>
<option value="$10K - $25K">$10,000 - $25,000</option>
<option value="$25K - $50K">$25,000 - $50,000</option>
<option value="$50K - $100K">$50,000 - $100,000</option>
<option value="$100K - $250K">$100,000 - $250,000</option>
<option value="$250K+">$250,000+</option>
</select></div>
<div class="form-group"><label for="timeInBusiness">Time in Business *</label>
<select id="timeInBusiness" name="time_in_business" required>
<option value="">Select...</option>
<option value="Startup">Startup</option>
<option value="0-6 months">0 - 6 months</option>
<option value="6-12 months">6 - 12 months</option>
<option value="1-2 years">1 - 2 years</option>
<option value="2-5 years">2 - 5 years</option>
<option value="5+ years">5+ years</option>
</select></div>
<div class="form-group full"><label for="notes">Additional Details</label><textarea id="notes" name="notes" placeholder="Tell us about your funding needs..."></textarea></div>
</div>
<button type="submit" class="btn btn-primary btn-lg submit-btn">Request a Callback &rarr;</button>
<p class="form-note">&#128274; Your information is secure and encrypted. No hard credit inquiry.</p>
</form>
</div>
</div>
</section>

<footer class="footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand"><h3>Advanced Marketing Co.</h3><p>Connecting businesses with the funding and payment solutions they need to grow.</p></div>
<div class="footer-col">
<h4>Funding</h4>
<a href="/loans/mca.html">Merchant Cash Advance</a>
<a href="/loans/term-loan.html">Business Term Loan</a>
<a href="/loans/sba.html">SBA Loan</a>
<a href="/loans/equipment.html">Equipment Financing</a>
<a href="/loans/loc.html">Line of Credit</a>
</div>
<div class="footer-col">
<h4>Payments</h4>
<a href="/loans/processing.html">Card Processing</a>
<a href="/loans/invoice-factoring.html">Invoice Factoring</a>
</div>
<div class="footer-col">
<h4>Company</h4>
<a href="/">Home</a>
<a href="/admin">Partner Portal</a>
<a href="mailto:contact@advancedmarketing.co">Contact</a>
</div>
</div>
<div class="footer-bottom"><p>&copy; 2026 Advanced Marketing Co. Ltd. Not a direct lender.</p></div>
</div>
</footer>

<div class="toast" id="toast"><span>&#10003;</span><span id="toastMsg">Application received!</span></div>

<script>
document.getElementById('leadForm').addEventListener('submit', async function(e) {{
  e.preventDefault();
  const btn = e.target.querySelector('.submit-btn');
  const original = btn.innerHTML;
  btn.innerHTML = 'Submitting...'; btn.disabled = true;
  const data = Object.fromEntries(new FormData(e.target).entries());
  try {{
    const res = await fetch('/api/lead', {{ method: 'POST', headers: {{'Content-Type':'application/json'}}, body: JSON.stringify(data) }});
    const json = await res.json();
    if (json.success) {{
      showToast('Thanks! Check your email for next steps. Redirecting to application...');
      setTimeout(() => {{ window.location.href = json.funding_url || '{FUNDING_URL}'; }}, 2000);
    }} else {{
      showToast('Error. Please try again.');
      btn.innerHTML = original; btn.disabled = false;
    }}
  }} catch {{
    showToast('Network error. Please try again.');
    btn.innerHTML = original; btn.disabled = false;
  }}
}});
function showToast(msg) {{ const t=document.getElementById('toast'); document.getElementById('toastMsg').textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),5000); }}
</script>
</body>
</html>
'''

def main():
    total = 0
    for loan_key in LOAN_TYPES:
        loan_dir = f'public/loans/{loan_key}'
        os.makedirs(loan_dir, exist_ok=True)
        for state_code in STATE_NAMES:
            state_dir = f'{loan_dir}/{state_code}'
            os.makedirs(state_dir, exist_ok=True)

            # State page
            state_path = f'{loan_dir}/{state_code}.html'
            with open(state_path, 'w', encoding='utf-8') as f:
                f.write(generate_state_page(state_code, loan_key, LOAN_TYPES[loan_key]))
            total += 1

            # City pages
            city_src = f'public/cities/{state_code}'
            if os.path.exists(city_src):
                for city_file in os.listdir(city_src):
                    if not city_file.endswith('.html'):
                        continue
                    city_slug = city_file.replace('.html', '')
                    city_path = f'{state_dir}/{city_slug}.html'
                    with open(city_path, 'w', encoding='utf-8') as f:
                        f.write(generate_city_page(state_code, city_slug, loan_key, LOAN_TYPES[loan_key]))
                    total += 1

    print(f'Generated {total} pages')

if __name__ == '__main__':
    main()
