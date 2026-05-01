from generate_cities import CITIES, STATE_MAP
import os
import random

def spintax_spin(text):
    while '[@' in text and '@]' in text:
        start = text.find('[@')
        end = text.find('@]', start)
        if end == -1:
            break
        options = text[start + 2:end].split('|')
        text = text[:start] + random.choice(options) + text[end + 2:]
    return text

TEMPLATE = '''<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>[@Merchant Cash Advance|MCA Funding|Business Cash Advance|Working Capital@] in %%CITY%%, %%STATE_CODE%% | Same-Day Approval</title>
<meta name='description' content='[@Get|Apply for@] [@merchant cash advance|revenue-based funding|business funding@] in %%CITY%%, %%STATE_NAME%%. [@Bad credit OK|No collateral|24hr funding@]. [@Free quote|Instant pre-qualification@].'>
<style>
:root{--bg:#0a0a0f;--surface:#12121a;--surface-2:#1a1a25;--border:#2a2a3a;--text:#e4e4e7;--text-muted:#71717a;--accent:#00d4aa;--accent-glow:rgba(0,212,170,0.15);--success:#10b981;}
body{font-family:'Inter',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;margin:0;}
.container{max-width:900px;margin:0 auto;padding:24px;}
header{border-bottom:1px solid var(--border);background:var(--surface);padding:16px 0;}
.logo{display:flex;align-items:center;gap:12px;font-weight:800;font-size:1.25rem;color:var(--text);text-decoration:none;}
.logo-icon{width:40px;height:40px;background:linear-gradient(135deg,var(--accent),#00b4d8);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;}
.nav-links a{color:var(--text-muted);text-decoration:none;font-weight:500;margin-left:24px;font-size:0.9rem;}
h1{font-size:2.2rem;font-weight:800;line-height:1.2;margin-bottom:16px;}
h1 span{background:linear-gradient(135deg,var(--accent),#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
h2{font-size:1.5rem;font-weight:700;margin-bottom:12px;}
p{color:var(--text-muted);margin-bottom:16px;}
.accent{color:var(--accent);}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:12px;font-weight:700;text-decoration:none;transition:all .2s;border:none;cursor:pointer;}
.btn-primary{background:linear-gradient(135deg,var(--accent),#00b4d8);color:#fff;box-shadow:0 4px 20px var(--accent-glow);}
.section{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px;margin:24px 0;}
.section ul{margin:0;padding-left:20px;color:var(--text-muted);}
.section li{margin-bottom:8px;}
.footer{border-top:1px solid var(--border);padding:32px 0;margin-top:40px;text-align:center;color:var(--text-muted);font-size:0.85rem;}
.badge{display:inline-flex;align-items:center;gap:8px;background:var(--surface-2);border:1px solid var(--border);padding:6px 14px;border-radius:100px;font-size:0.8rem;font-weight:600;color:var(--accent);margin-bottom:16px;}
.local-list{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px;}
.local-item{background:var(--surface-2);border:1px solid var(--border);padding:12px;border-radius:10px;font-size:0.9rem;color:var(--text-muted);}
.local-item strong{color:var(--text);display:block;margin-bottom:4px;}
@media(max-width:768px){.local-list{grid-template-columns:1fr;}h1{font-size:1.7rem;}}
</style>
</head>
<body>
<header>
<div class='container' style='display:flex;justify-content:space-between;align-items:center;'>
<a href='../index.html' class='logo'><div class='logo-icon'>AM</div>Advanced Marketing Co.</a>
<nav class='nav-links'><a href='../index.html#services'>Services</a><a href='../index.html#apply'>Apply Now</a></nav>
</div>
</header>

<div class='container'>
<div class='badge'>Fast Funding in %%CITY%% â€” Apply in 2 Minutes</div>
<h1>[@Merchant Cash Advance|Business Funding|Working Capital@] in %%CITY%%, <span>%%STATE_CODE%%</span></h1>
<p>[@If you own a business in %%CITY%%|Running a company in %%CITY%%|%%CITY%% entrepreneurs@], you [@already know|understand@] that [@steady cash flow|fast access to capital|reliable working capital@] [@is critical|can make or break|drives every decision@] [@you make|in your market@]. [@Whether you are a restaurant owner near downtown|From retail shops on Main Street to service providers across %%STATE_NAME%%|No matter if you are in hospitality, construction, or professional services@], our [@funding network|capital advisors|MCA specialists@] [@help %%CITY%% businesses|connect %%STATE_NAME%% owners|work with local companies@] [@secure same-day approvals|get funded within 24 hours|access flexible capital@] â€” [@even with bad credit|with no collateral required|regardless of credit history@].</p>
<a href='../index.html#apply' class='btn btn-primary'>Check My Eligibility &rarr;</a>
</div>

<div class='container'>
<div class='section'>
<h2>[@Why %%CITY%% Business Owners Choose Us|Fast MCA Funding for %%CITY%% Companies|%%STATE_NAME%% Revenue-Based Financing@]</h2>
<p>[@We are not a bank|Unlike traditional lenders|No red tape here@]. We [@specialize in|focus on|connect you to@] [@merchant cash advances and revenue-based funding|flexible business capital|fast alternative financing@] [@for small and mid-sized businesses|for companies doing $10K+/month in revenue|across %%STATE_NAME%% and beyond@]. [@Here is what %%CITY%% clients get|Local business owners benefit from|Your %%CITY%% company qualifies for@]:</p>
<ul>
<li>[@Approval in as little as 2 hours|Same-day pre-qualification|24-hour approval turnaround@]</li>
<li>[@Funding from $5,000 to $500,000|Advances from $5Kâ€“$500K|Capital amounts tailored to your revenue@]</li>
<li>[@No hard credit check|Soft pull only â€” will not hurt your score|Bad credit and prior defaults OK@]</li>
<li>[@Repay as you earn from daily sales|Flexible remittance tied to revenue|No fixed monthly payments@]</li>
<li>[@Use funds for any business purpose|Spend on payroll, inventory, expansion, or equipment|No restrictions on how you use the capital@]</li>
</ul>
</div>

<div class='section'>
<h2>[@Credit Card Processing %%CITY%%|Lower Your Processing Rates in %%CITY%%|%%STATE_NAME%% Payment Solutions@]</h2>
<p>[@In addition to MCA funding|Beyond business loans|Alongside fast capital@], we [@audit and reduce|help %%CITY%% merchants lower|negotiate better@] [@credit card processing fees|merchant service rates|payment processing costs@]. [@Most %%CITY%% businesses we speak with|Many local merchants|The average %%STATE_NAME%% company@] [@overpay by 20â€“40%|are locked into inflated rates|can save hundreds monthly@] [@without even knowing it|on every swipe and tap@]. [@We compare your statement|Our free rate audit shows|We analyze your current setup and@] [@switch you to a wholesale or interchange-plus program|match you with a lower-cost processor|find hidden markups and eliminate them@] â€” [@often with better equipment and next-day funding|usually with zero switching costs|typically within 48 hours@].</p>
<div class='local-list'>
<div class='local-item'><strong>[@Free Rate Audit|Zero Cost Analysis|Complimentary Review@]</strong>[@We review your current statement|No obligation comparison|See exactly what you overpay@]</div>
<div class='local-item'><strong>[@20â€“40% Savings|Dramatic Rate Cuts|Lower Monthly Fees@]</strong>[@Average client saves $300+/mo|Keep more of every transaction|Better than your current MSP@]</div>
<div class='local-item'><strong>[@Next-Day Deposits|Faster Funding|Quick Settlement@]</strong>[@Do not wait 2â€“3 days for your money|Improve cash flow immediately|Get paid faster@]</div>
<div class='local-item'><strong>[@Local Support|Dedicated Rep|Personal Advisor@]</strong>[@One point of contact|We answer the phone|Real people, not call centers@]</div>
</div>
</div>

<div class='section'>
<h2>[@Who Qualifies in %%CITY%%|MCA Requirements %%STATE_NAME%%|Do You Qualify?@]</h2>
<p>[@We work with|Our network funds|You may qualify if you are@] [@restaurants, auto shops, medical practices, salons, contractors, retailers, wholesalers, and online sellers|virtually any %%CITY%% business with consistent revenue|companies across %%STATE_NAME%% that process payments@]. [@Basic requirements include|The process is simple|Minimum criteria@]:</p>
<ul>
<li>[@3+ months in business|At least 90 days operating|Active business for one quarter@]</li>
<li>[@$10,000+ average monthly revenue|$10K+/month in gross sales|Consistent monthly deposits@]</li>
<li>[@Business bank account|Active checking account|Valid commercial account@]</li>
<li>[@No minimum FICO|All credit scores welcome|Bad credit, prior defaults, and tax liens OK@]</li>
</ul>
<p>[@Ready to see your offer?|Want a free quote?|Curious what you qualify for?@] [@Apply now â€” it takes 2 minutes|Fill out the form below|Click through and check your eligibility@] [@and we will call you within 2 hours|for a same-day funding assessment|to discuss your %%CITY%% business funding options@].</p>
<a href='../index.html#apply' class='btn btn-primary'>[@Get My Free Quote &rarr;|Check Eligibility &rarr;|Apply Now &rarr;@]</a>
</div>

<div class='section'>
<h2>[@%%CITY%% Local Business Funding FAQ|Common Questions From %%STATE_NAME%% Owners|MCA FAQ@]</h2>
<p><strong>[@Is a merchant cash advance a loan?|What is the difference between an MCA and a loan?@]</strong><br>[@An MCA is not technically a loan|MCA purchases future revenue|It is a sale of future receivables@]. [@You receive a lump sum|We advance capital against future sales|Funding is based on projected revenue@] [@and repay via a fixed percentage of daily card sales|remitted automatically from daily deposits|through small daily deductions@]. [@There is no fixed term|Repayment adjusts with your cash flow|Slow day = smaller payment@].</p>
<p><strong>[@Will this hurt my credit?|Is there a hard credit pull?@]</strong><br>[@No hard inquiry|Most of our funding partners use soft pulls only|Your personal credit is not impacted@] [@during the quote stage|for pre-qualification|to generate your offer@]. [@Some providers may do a hard pull only after you accept|A hard check only happens if you move forward with certain lenders|Approval is primarily revenue-based@].</p>
<p><strong>[@How fast can I get funded in %%CITY%%?|When will I receive the money?@]</strong><br>[@Many %%CITY%% businesses receive funds within 24 hours|Same-day wire available|Funds hit your account as soon as tomorrow@] [@after approval|once docs are signed|following final verification@].</p>
</div>
</div>

<footer class='footer'>
<div class='container'>
<p>&copy; 2026 Advanced Marketing Co. Ltd. All rights reserved.</p>
<p>Advanced Marketing Co. is a referral partner, not a direct lender. All funding decisions are made by our licensed financial partners.</p>
<p><a href='../index.html' style='color:var(--text-muted);'>&larr; Back to Home</a></p>
</div>
</footer>
</body>
</html>'''

def slugify(text):
    text = text.replace(' ', '-').replace("'", '').replace('.', '')
    return text.lower()

def generate_all():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cities')
    os.makedirs(base_dir, exist_ok=True)
    sitemap_entries = []
    city_links = []
    count = 0
    for city, state_code in CITIES:
        state_name = STATE_MAP.get(state_code, state_code)
        city_slug = slugify(city)
        state_dir = os.path.join(base_dir, state_code.lower())
        os.makedirs(state_dir, exist_ok=True)
        html = TEMPLATE.replace('%%CITY%%', city)
        html = html.replace('%%STATE_CODE%%', state_code)
        html = html.replace('%%STATE_NAME%%', state_name)
        html = spintax_spin(html)
        filepath = os.path.join(state_dir, city_slug + '.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        url = state_code.lower() + '/' + city_slug + '.html'
        sitemap_entries.append('<url><loc>https://yoursite.com/cities/' + url + '</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>')
        city_links.append('<li><a href="' + url + '">' + city + ', ' + state_code + '</a></li>')
        count += 1
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += '\n'.join(sitemap_entries)
    sitemap += '\n</urlset>'
    with open(os.path.join(os.path.dirname(base_dir), 'sitemap-cities.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap)
    index_html = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Business Funding Locations</title>
<style>body{font-family:Inter,sans-serif;background:#0a0a0f;color:#e4e4e7;padding:40px;}
a{color:#00d4aa;text-decoration:none;} ul{columns:3;} li{margin:4px 0;}</style>
</head><body><h1>Business Funding & Processing â€” All Locations</h1><ul>
''' + '\n'.join(city_links) + '''
</ul></body></html>'''
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print('Generated', count, 'city pages in', base_dir)
    print('Sitemap written to sitemap-cities.xml')
    print('Index written to cities/index.html')

if __name__ == '__main__':
    generate_all()
