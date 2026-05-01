import os
import random

def spintax_spin(text):
    while '{' in text and '}' in text:
        start = text.find('{')
        end = text.find('}', start)
        if end == -1:
            break
        options = text[start + 1:end].split('|')
        text = text[:start] + random.choice(options) + text[end + 1:]
    return text

STATE_MAP = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

TEMPLATE = '''<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>{Merchant Cash Advance|MCA Funding|Business Cash Advance|Working Capital} in %%CITY%%, %%STATE_CODE%% | Same-Day Approval</title>
<meta name='description' content='{Get|Apply for} {merchant cash advance|revenue-based funding|business funding} in %%CITY%%, %%STATE_NAME%%. {Bad credit OK|No collateral|24hr funding}. {Free quote|Instant pre-qualification}.'>
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
<div class='badge'>Fast Funding in %%CITY%% — Apply in 2 Minutes</div>
<h1>{Merchant Cash Advance|Business Funding|Working Capital} in %%CITY%%, <span>%%STATE_CODE%%</span></h1>
<p>{If you own a business in %%CITY%%|Running a company in %%CITY%%|%%CITY%% entrepreneurs}, you {already know|understand} that {steady cash flow|fast access to capital|reliable working capital} {is critical|can make or break|drives every decision} {you make|in your market}. {Whether you are a restaurant owner near downtown|From retail shops on Main Street to service providers across %%STATE_NAME%%|No matter if you are in hospitality, construction, or professional services}, our {funding network|capital advisors|MCA specialists} {help %%CITY%% businesses|connect %%STATE_NAME%% owners|work with local companies} {secure same-day approvals|get funded within 24 hours|access flexible capital} — {even with bad credit|with no collateral required|regardless of credit history}.</p>
<a href='../index.html#apply' class='btn btn-primary'>Check My Eligibility &rarr;</a>
</div>

<div class='container'>
<div class='section'>
<h2>{Why %%CITY%% Business Owners Choose Us|Fast MCA Funding for %%CITY%% Companies|%%STATE_NAME%% Revenue-Based Financing}</h2>
<p>{We are not a bank|Unlike traditional lenders|No red tape here}. We {specialize in|focus on|connect you to} {merchant cash advances and revenue-based funding|flexible business capital|fast alternative financing} {for small and mid-sized businesses|for companies doing $10K+/month in revenue|across %%STATE_NAME%% and beyond}. {Here is what %%CITY%% clients get|Local business owners benefit from|Your %%CITY%% company qualifies for}:</p>
<ul>
<li>{Approval in as little as 2 hours|Same-day pre-qualification|24-hour approval turnaround}</li>
<li>{Funding from $5,000 to $500,000|Advances from $5K–$500K|Capital amounts tailored to your revenue}</li>
<li>{No hard credit check|Soft pull only — will not hurt your score|Bad credit and prior defaults OK}</li>
<li>{Repay as you earn from daily sales|Flexible remittance tied to revenue|No fixed monthly payments}</li>
<li>{Use funds for any business purpose|Spend on payroll, inventory, expansion, or equipment|No restrictions on how you use the capital}</li>
</ul>
</div>

<div class='section'>
<h2>{Credit Card Processing %%CITY%%|Lower Your Processing Rates in %%CITY%%|%%STATE_NAME%% Payment Solutions}</h2>
<p>{In addition to MCA funding|Beyond business loans|Alongside fast capital}, we {audit and reduce|help %%CITY%% merchants lower|negotiate better} {credit card processing fees|merchant service rates|payment processing costs}. {Most %%CITY%% businesses we speak with|Many local merchants|The average %%STATE_NAME%% company} {overpay by 20–40%|are locked into inflated rates|can save hundreds monthly} {without even knowing it|on every swipe and tap}. {We compare your statement|Our free rate audit shows|We analyze your current setup and} {switch you to a wholesale or interchange-plus program|match you with a lower-cost processor|find hidden markups and eliminate them} — {often with better equipment and next-day funding|usually with zero switching costs|typically within 48 hours}.</p>
<div class='local-list'>
<div class='local-item'><strong>{Free Rate Audit|Zero Cost Analysis|Complimentary Review}</strong>{We review your current statement|No obligation comparison|See exactly what you overpay}</div>
<div class='local-item'><strong>{20–40% Savings|Dramatic Rate Cuts|Lower Monthly Fees}</strong>{Average client saves $300+/mo|Keep more of every transaction|Better than your current MSP}</div>
<div class='local-item'><strong>{Next-Day Deposits|Faster Funding|Quick Settlement}</strong>{Do not wait 2–3 days for your money|Improve cash flow immediately|Get paid faster}</div>
<div class='local-item'><strong>{Local Support|Dedicated Rep|Personal Advisor}</strong>{One point of contact|We answer the phone|Real people, not call centers}</div>
</div>
</div>

<div class='section'>
<h2>{Who Qualifies in %%CITY%%|MCA Requirements %%STATE_NAME%%|Do You Qualify?}</h2>
<p>{We work with|Our network funds|You may qualify if you are} {restaurants, auto shops, medical practices, salons, contractors, retailers, wholesalers, and online sellers|virtually any %%CITY%% business with consistent revenue|companies across %%STATE_NAME%% that process payments}. {Basic requirements include|The process is simple|Minimum criteria}:</p>
<ul>
<li>{3+ months in business|At least 90 days operating|Active business for one quarter}</li>
<li>{$10,000+ average monthly revenue|$10K+/month in gross sales|Consistent monthly deposits}</li>
<li>{Business bank account|Active checking account|Valid commercial account}</li>
<li>{No minimum FICO|All credit scores welcome|Bad credit, prior defaults, and tax liens OK}</li>
</ul>
<p>{Ready to see your offer?|Want a free quote?|Curious what you qualify for?} {Apply now — it takes 2 minutes|Fill out the form below|Click through and check your eligibility} {and we will call you within 2 hours|for a same-day funding assessment|to discuss your %%CITY%% business funding options}.</p>
<a href='../index.html#apply' class='btn btn-primary'>{Get My Free Quote &rarr;|Check Eligibility &rarr;|Apply Now &rarr;}</a>
</div>

<div class='section'>
<h2>{%%CITY%% Local Business Funding FAQ|Common Questions From %%STATE_NAME%% Owners|MCA FAQ}</h2>
<p><strong>{Is a merchant cash advance a loan?|What is the difference between an MCA and a loan?}</strong><br>{An MCA is not technically a loan|MCA purchases future revenue|It is a sale of future receivables}. {You receive a lump sum|We advance capital against future sales|Funding is based on projected revenue} {and repay via a fixed percentage of daily card sales|remitted automatically from daily deposits|through small daily deductions}. {There is no fixed term|Repayment adjusts with your cash flow|Slow day = smaller payment}.</p>
<p><strong>{Will this hurt my credit?|Is there a hard credit pull?}</strong><br>{No hard inquiry|Most of our funding partners use soft pulls only|Your personal credit is not impacted} {during the quote stage|for pre-qualification|to generate your offer}. {Some providers may do a hard pull only after you accept|A hard check only happens if you move forward with certain lenders|Approval is primarily revenue-based}.</p>
<p><strong>{How fast can I get funded in %%CITY%%?|When will I receive the money?}</strong><br>{Many %%CITY%% businesses receive funds within 24 hours|Same-day wire available|Funds hit your account as soon as tomorrow} {after approval|once docs are signed|following final verification}.</p>
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

CITIES = [
    ('Birmingham', 'AL'), ('Montgomery', 'AL'), ('Mobile', 'AL'), ('Huntsville', 'AL'), ('Tuscaloosa', 'AL'),
    ('Hoover', 'AL'), ('Dothan', 'AL'), ('Auburn', 'AL'), ('Decatur', 'AL'), ('Madison', 'AL'),
    ('Florence', 'AL'), ('Phenix City', 'AL'), ('Gadsden', 'AL'), ('Prattville', 'AL'), ('Vestavia Hills', 'AL'),
    ('Anchorage', 'AK'), ('Fairbanks', 'AK'), ('Juneau', 'AK'), ('Wasilla', 'AK'), ('Sitka', 'AK'),
    ('Ketchikan', 'AK'), ('Kenai', 'AK'), ('Kodiak', 'AK'), ('Bethel', 'AK'), ('Palmer', 'AK'),
    ('Phoenix', 'AZ'), ('Tucson', 'AZ'), ('Mesa', 'AZ'), ('Chandler', 'AZ'), ('Scottsdale', 'AZ'),
    ('Glendale', 'AZ'), ('Gilbert', 'AZ'), ('Tempe', 'AZ'), ('Peoria', 'AZ'), ('Surprise', 'AZ'),
    ('Yuma', 'AZ'), ('Avondale', 'AZ'), ('Flagstaff', 'AZ'), ('Goodyear', 'AZ'), ('Lake Havasu City', 'AZ'),
    ('Little Rock', 'AR'), ('Fort Smith', 'AR'), ('Fayetteville', 'AR'), ('Springdale', 'AR'), ('Jonesboro', 'AR'),
    ('North Little Rock', 'AR'), ('Conway', 'AR'), ('Rogers', 'AR'), ('Pine Bluff', 'AR'), ('Bentonville', 'AR'),
    ('Hot Springs', 'AR'), ('Benton', 'AR'), ('Texarkana', 'AR'), ('Sherwood', 'AR'), ('Russellville', 'AR'),
    ('Los Angeles', 'CA'), ('San Diego', 'CA'), ('San Jose', 'CA'), ('San Francisco', 'CA'), ('Fresno', 'CA'),
    ('Sacramento', 'CA'), ('Long Beach', 'CA'), ('Oakland', 'CA'), ('Bakersfield', 'CA'), ('Anaheim', 'CA'),
    ('Santa Ana', 'CA'), ('Riverside', 'CA'), ('Stockton', 'CA'), ('Chula Vista', 'CA'), ('Irvine', 'CA'),
    ('Fremont', 'CA'), ('San Bernardino', 'CA'), ('Modesto', 'CA'), ('Fontana', 'CA'), ('Oxnard', 'CA'),
    ('Moreno Valley', 'CA'), ('Huntington Beach', 'CA'), ('Glendale', 'CA'), ('Santa Clarita', 'CA'), ('Oceanside', 'CA'),
    ('Garden Grove', 'CA'), ('Rancho Cucamonga', 'CA'), ('Santa Rosa', 'CA'), ('Ontario', 'CA'), ('Elk Grove', 'CA'),
    ('Denver', 'CO'), ('Colorado Springs', 'CO'), ('Aurora', 'CO'), ('Fort Collins', 'CO'), ('Lakewood', 'CO'),
    ('Thornton', 'CO'), ('Arvada', 'CO'), ('Westminster', 'CO'), ('Pueblo', 'CO'), ('Centennial', 'CO'),
    ('Boulder', 'CO'), ('Greeley', 'CO'), ('Longmont', 'CO'), ('Loveland', 'CO'), ('Grand Junction', 'CO'),
    ('Broomfield', 'CO'), ('Castle Rock', 'CO'), ('Commerce City', 'CO'), ('Parker', 'CO'), ('Littleton', 'CO'),
    ('Bridgeport', 'CT'), ('New Haven', 'CT'), ('Stamford', 'CT'), ('Hartford', 'CT'), ('Waterbury', 'CT'),
    ('Norwalk', 'CT'), ('Danbury', 'CT'), ('New Britain', 'CT'), ('Bristol', 'CT'), ('Meriden', 'CT'),
    ('Milford', 'CT'), ('West Haven', 'CT'), ('Middletown', 'CT'), ('Norwich', 'CT'), ('Shelton', 'CT'),
    ('Wilmington', 'DE'), ('Dover', 'DE'), ('Newark', 'DE'), ('Middletown', 'DE'), ('Smyrna', 'DE'),
    ('Milford', 'DE'), ('Seaford', 'DE'), ('Georgetown', 'DE'), ('Elsmere', 'DE'), ('New Castle', 'DE'),
    ('Jacksonville', 'FL'), ('Miami', 'FL'), ('Tampa', 'FL'), ('Orlando', 'FL'), ('St. Petersburg', 'FL'),
    ('Hialeah', 'FL'), ('Port St. Lucie', 'FL'), ('Cape Coral', 'FL'), ('Tallahassee', 'FL'), ('Fort Lauderdale', 'FL'),
    ('Pembroke Pines', 'FL'), ('Hollywood', 'FL'), ('Gainesville', 'FL'), ('Miramar', 'FL'), ('Coral Springs', 'FL'),
    ('Miami Gardens', 'FL'), ('Lehigh Acres', 'FL'), ('Clearwater', 'FL'), ('Palm Bay', 'FL'), ('Pompano Beach', 'FL'),
    ('West Palm Beach', 'FL'), ('Lakeland', 'FL'), ('Davie', 'FL'), ('Miami Beach', 'FL'), ('Plantation', 'FL'),
    ('Sunrise', 'FL'), ('Boca Raton', 'FL'), ('Deltona', 'FL'), ('Largo', 'FL'), ('Deerfield Beach', 'FL'),
    ('Atlanta', 'GA'), ('Augusta', 'GA'), ('Columbus', 'GA'), ('Macon', 'GA'), ('Savannah', 'GA'),
    ('Athens', 'GA'), ('Sandy Springs', 'GA'), ('Roswell', 'GA'), ('Johns Creek', 'GA'), ('Albany', 'GA'),
    ('Warner Robins', 'GA'), ('Alpharetta', 'GA'), ('Marietta', 'GA'), ('Valdosta', 'GA'), ('Smyrna', 'GA'),
    ('Brookhaven', 'GA'), ('Dunwoody', 'GA'), ('Peachtree Corners', 'GA'), ('Mableton', 'GA'), ('Gainesville', 'GA'),
    ('Newnan', 'GA'), ('Rome', 'GA'), ('Tucker', 'GA'), ('East Point', 'GA'), ('Peachtree City', 'GA'),
    ('Dalton', 'GA'), ('Hinesville', 'GA'), ('Woodstock', 'GA'), ('Carrollton', 'GA'), ('Canton', 'GA'),
    ('Honolulu', 'HI'), ('East Honolulu', 'HI'), ('Pearl City', 'HI'), ('Hilo', 'HI'), ('Kailua', 'HI'),
    ('Waipahu', 'HI'), ('Kaneohe', 'HI'), ('Mililani Town', 'HI'), ('Kahului', 'HI'), ('Ewa Gentry', 'HI'),
    ('Boise', 'ID'), ('Meridian', 'ID'), ('Nampa', 'ID'), ('Idaho Falls', 'ID'), ('Caldwell', 'ID'),
    ('Pocatello', 'ID'), ('Coeur d' + chr(39) + 'Alene', 'ID'), ('Twin Falls', 'ID'), ('Rexburg', 'ID'), ('Post Falls', 'ID'),
    ('Lewiston', 'ID'), ('Eagle', 'ID'), ('Moscow', 'ID'), ('Kuna', 'ID'), ('Ammon', 'ID'),
    ('Chicago', 'IL'), ('Aurora', 'IL'), ('Naperville', 'IL'), ('Joliet', 'IL'), ('Rockford', 'IL'),
    ('Springfield', 'IL'), ('Elgin', 'IL'), ('Peoria', 'IL'), ('Champaign', 'IL'), ('Waukegan', 'IL'),
    ('Cicero', 'IL'), ('Bloomington', 'IL'), ('Arlington Heights', 'IL'), ('Evanston', 'IL'), ('Decatur', 'IL'),
    ('Schaumburg', 'IL'), ('Bolingbrook', 'IL'), ('Palatine', 'IL'), ('Skokie', 'IL'), ('Des Plaines', 'IL'),
    ('Orland Park', 'IL'), ('Tinley Park', 'IL'), ('Oak Lawn', 'IL'), ('Berwyn', 'IL'), ('Mount Prospect', 'IL'),
    ('Normal', 'IL'), ('Wheaton', 'IL'), ('Hoffman Estates', 'IL'), ('Oak Park', 'IL'), ('Downers Grove', 'IL'),
    ('Indianapolis', 'IN'), ('Fort Wayne', 'IN'), ('Evansville', 'IN'), ('South Bend', 'IN'), ('Carmel', 'IN'),
    ('Fishers', 'IN'), ('Bloomington', 'IN'), ('Hammond', 'IN'), ('Gary', 'IN'), ('Lafayette', 'IN'),
    ('Muncie', 'IN'), ('Noblesville', 'IN'), ('Terre Haute', 'IN'), ('Kokomo', 'IN'), ('Anderson', 'IN'),
    ('Greenwood', 'IN'), ('Elkhart', 'IN'), ('Mishawaka', 'IN'), ('Lawrence', 'IN'), ('Columbus', 'IN'),
    ('Jeffersonville', 'IN'), ('Westfield', 'IN'), ('Portage', 'IN'), ('Goshen', 'IN'), ('Michigan City', 'IN'),
    ('West Lafayette', 'IN'), ('Marion', 'IN'), ('East Chicago', 'IN'), ('Franklin', 'IN'), ('Valparaiso', 'IN'),
    ('Des Moines', 'IA'), ('Cedar Rapids', 'IA'), ('Davenport', 'IA'), ('Sioux City', 'IA'), ('Iowa City', 'IA'),
    ('Waterloo', 'IA'), ('Ames', 'IA'), ('West Des Moines', 'IA'), ('Ankeny', 'IA'), ('Council Bluffs', 'IA'),
    ('Dubuque', 'IA'), ('Urbandale', 'IA'), ('Cedar Falls', 'IA'), ('Marion', 'IA'), ('Bettendorf', 'IA'),
    ('Mason City', 'IA'), ('Marshalltown', 'IA'), ('Clinton', 'IA'), ('Burlington', 'IA'), ('Ottumwa', 'IA'),
    ('Wichita', 'KS'), ('Overland Park', 'KS'), ('Kansas City', 'KS'), ('Olathe', 'KS'), ('Topeka', 'KS'),
    ('Lawrence', 'KS'), ('Shawnee', 'KS'), ('Manhattan', 'KS'), ('Lenexa', 'KS'), ('Salina', 'KS'),
    ('Hutchinson', 'KS'), ('Leavenworth', 'KS'), ('Leawood', 'KS'), ('Dodge City', 'KS'), ('Garden City', 'KS'),
    ('Emporia', 'KS'), ('Junction City', 'KS'), ('Derby', 'KS'), ('Prairie Village', 'KS'), ('Liberal', 'KS'),
    ('Louisville', 'KY'), ('Lexington', 'KY'), ('Bowling Green', 'KY'), ('Owensboro', 'KY'), ('Covington', 'KY'),
    ('Richmond', 'KY'), ('Georgetown', 'KY'), ('Florence', 'KY'), ('Hopkinsville', 'KY'), ('Nicholasville', 'KY'),
    ('Elizabethtown', 'KY'), ('Henderson', 'KY'), ('Frankfort', 'KY'), ('Jeffersontown', 'KY'), ('Independence', 'KY'),
    ('Paducah', 'KY'), ('Radcliff', 'KY'), ('Ashland', 'KY'), ('Madisonville', 'KY'), ('Murray', 'KY'),
    ('New Orleans', 'LA'), ('Baton Rouge', 'LA'), ('Shreveport', 'LA'), ('Lafayette', 'LA'), ('Lake Charles', 'LA'),
    ('Kenner', 'LA'), ('Bossier City', 'LA'), ('Monroe', 'LA'), ('Alexandria', 'LA'), ('Houma', 'LA'),
    ('New Iberia', 'LA'), ('Slidell', 'LA'), ('Central', 'LA'), ('Ruston', 'LA'), ('Sulphur', 'LA'),
    ('Hammond', 'LA'), ('Marrero', 'LA'), ('Laplace', 'LA'), ('Terrytown', 'LA'), ('Natchitoches', 'LA'),
    ('Portland', 'ME'), ('Lewiston', 'ME'), ('Bangor', 'ME'), ('South Portland', 'ME'), ('Auburn', 'ME'),
    ('Biddeford', 'ME'), ('Sanford', 'ME'), ('Saco', 'ME'), ('Westbrook', 'ME'), ('Augusta', 'ME'),
    ('Waterville', 'ME'), ('Presque Isle', 'ME'), ('Brewer', 'ME'), ('Bath', 'ME'), ('Caribou', 'ME'),
    ('Baltimore', 'MD'), ('Frederick', 'MD'), ('Rockville', 'MD'), ('Gaithersburg', 'MD'), ('Bowie', 'MD'),
    ('Hagerstown', 'MD'), ('Annapolis', 'MD'), ('College Park', 'MD'), ('Salisbury', 'MD'), ('Laurel', 'MD'),
    ('Greenbelt', 'MD'), ('Cumberland', 'MD'), ('Westminster', 'MD'), ('Hyattsville', 'MD'), ('Takoma Park', 'MD'),
    ('Easton', 'MD'), ('Elkton', 'MD'), ('Aberdeen', 'MD'), ('Havre de Grace', 'MD'), ('Cambridge', 'MD'),
    ('Boston', 'MA'), ('Worcester', 'MA'), ('Springfield', 'MA'), ('Cambridge', 'MA'), ('Lowell', 'MA'),
    ('Brockton', 'MA'), ('Quincy', 'MA'), ('New Bedford', 'MA'), ('Lynn', 'MA'), ('Fall River', 'MA'),
    ('Newton', 'MA'), ('Lawrence', 'MA'), ('Somerville', 'MA'), ('Framingham', 'MA'), ('Haverhill', 'MA'),
    ('Waltham', 'MA'), ('Malden', 'MA'), ('Brookline', 'MA'), ('Medford', 'MA'), ('Taunton', 'MA'),
    ('Chicopee', 'MA'), ('Weymouth', 'MA'), ('Revere', 'MA'), ('Peabody', 'MA'), ('Methuen', 'MA'),
    ('Everett', 'MA'), ('Attleboro', 'MA'), ('Arlington', 'MA'), ('Pittsfield', 'MA'), ('Billerica', 'MA'),
    ('Detroit', 'MI'), ('Grand Rapids', 'MI'), ('Warren', 'MI'), ('Sterling Heights', 'MI'), ('Ann Arbor', 'MI'),
    ('Lansing', 'MI'), ('Flint', 'MI'), ('Dearborn', 'MI'), ('Livonia', 'MI'), ('Troy', 'MI'),
    ('Westland', 'MI'), ('Farmington Hills', 'MI'), ('Kalamazoo', 'MI'), ('Wyoming', 'MI'), ('Southfield', 'MI'),
    ('Rochester Hills', 'MI'), ('Taylor', 'MI'), ('Pontiac', 'MI'), ('St. Clair Shores', 'MI'), ('Royal Oak', 'MI'),
    ('Dearborn Heights', 'MI'), ('Novi', 'MI'), ('Battle Creek', 'MI'), ('Saginaw', 'MI'), ('Kentwood', 'MI'),
    ('East Lansing', 'MI'), ('Roseville', 'MI'), ('Portage', 'MI'), ('Midland', 'MI'), ('Muskegon', 'MI'),
    ('Minneapolis', 'MN'), ('St. Paul', 'MN'), ('Rochester', 'MN'), ('Duluth', 'MN'), ('Bloomington', 'MN'),
    ('Brooklyn Park', 'MN'), ('Plymouth', 'MN'), ('Maple Grove', 'MN'), ('Woodbury', 'MN'), ('St. Cloud', 'MN'),
    ('Eagan', 'MN'), ('Eden Prairie', 'MN'), ('Coon Rapids', 'MN'), ('Burnsville', 'MN'), ('Blaine', 'MN'),
    ('Lakeville', 'MN'), ('Minnetonka', 'MN'), ('Apple Valley', 'MN'), ('Edina', 'MN'), ('St. Louis Park', 'MN'),
    ('Mankato', 'MN'), ('Moorhead', 'MN'), ('Shakopee', 'MN'), ('Maplewood', 'MN'), ('Cottage Grove', 'MN'),
    ('Jackson', 'MS'), ('Gulfport', 'MS'), ('Southaven', 'MS'), ('Hattiesburg', 'MS'), ('Biloxi', 'MS'),
    ('Olive Branch', 'MS'), ('Tupelo', 'MS'), ('Meridian', 'MS'), ('Greenville', 'MS'), ('Madison', 'MS'),
    ('Clinton', 'MS'), ('Pearl', 'MS'), ('Horn Lake', 'MS'), ('Oxford', 'MS'), ('Brandon', 'MS'),
    ('Starkville', 'MS'), ('Ridgeland', 'MS'), ('Columbus', 'MS'), ('Pascagoula', 'MS'), ('Vicksburg', 'MS'),
    ('Kansas City', 'MO'), ('St. Louis', 'MO'), ('Springfield', 'MO'), ('Columbia', 'MO'), ('Independence', 'MO'),
    ('Lee' + chr(39) + 's Summit', 'MO'), ('O' + chr(39) + 'Fallon', 'MO'), ('St. Joseph', 'MO'), ('St. Charles', 'MO'), ('St. Peters', 'MO'),
    ('Blue Springs', 'MO'), ('Joplin', 'MO'), ('Florissant', 'MO'), ('Chesterfield', 'MO'), ('Jefferson City', 'MO'),
    ('Cape Girardeau', 'MO'), ('Oakville', 'MO'), ('Wentzville', 'MO'), ('Wildwood', 'MO'), ('University City', 'MO'),
    ('Liberty', 'MO'), ('Ballwin', 'MO'), ('Raytown', 'MO'), ('Kirkwood', 'MO'), ('Gladstone', 'MO'),
    ('Maryland Heights', 'MO'), ('Hazelwood', 'MO'), ('Grandview', 'MO'), ('Belton', 'MO'), ('Webster Groves', 'MO'),
    ('Billings', 'MT'), ('Missoula', 'MT'), ('Great Falls', 'MT'), ('Bozeman', 'MT'), ('Butte', 'MT'),
    ('Helena', 'MT'), ('Kalispell', 'MT'), ('Havre', 'MT'), ('Anaconda', 'MT'), ('Miles City', 'MT'),
    ('Belgrade', 'MT'), ('Livingston', 'MT'), ('Laurel', 'MT'), ('Whitefish', 'MT'), ('Lewistown', 'MT'),
    ('Omaha', 'NE'), ('Lincoln', 'NE'), ('Bellevue', 'NE'), ('Grand Island', 'NE'), ('Kearney', 'NE'),
    ('Fremont', 'NE'), ('Hastings', 'NE'), ('North Platte', 'NE'), ('Norfolk', 'NE'), ('Columbus', 'NE'),
    ('Papillion', 'NE'), ('La Vista', 'NE'), ('Scottsbluff', 'NE'), ('South Sioux City', 'NE'), ('Beatrice', 'NE'),
    ('Lexington', 'NE'), ('Chalco', 'NE'), ('Gering', 'NE'), ('Alliance', 'NE'), ('York', 'NE'),
    ('Las Vegas', 'NV'), ('Henderson', 'NV'), ('Reno', 'NV'), ('North Las Vegas', 'NV'), ('Paradise', 'NV'),
    ('Spring Valley', 'NV'), ('Sunrise Manor', 'NV'), ('Enterprise', 'NV'), ('Sparks', 'NV'), ('Carson City', 'NV'),
    ('Whitney', 'NV'), ('Pahrump', 'NV'), ('Winchester', 'NV'), ('Summerlin South', 'NV'), ('Fernley', 'NV'),
    ('Mesquite', 'NV'), ('Boulder City', 'NV'), ('Spanish Springs', 'NV'), ('Spring Creek', 'NV'), ('Dayton', 'NV'),
    ('Manchester', 'NH'), ('Nashua', 'NH'), ('Concord', 'NH'), ('Derry', 'NH'), ('Rochester', 'NH'),
    ('Salem', 'NH'), ('Dover', 'NH'), ('Merrimack', 'NH'), ('Keene', 'NH'), ('Bedford', 'NH'),
    ('Portsmouth', 'NH'), ('Goffstown', 'NH'), ('Laconia', 'NH'), ('Hampton', 'NH'), ('Milford', 'NH'),
    ('Newark', 'NJ'), ('Jersey City', 'NJ'), ('Paterson', 'NJ'), ('Elizabeth', 'NJ'), ('Edison', 'NJ'),
    ('Woodbridge', 'NJ'), ('Lakewood', 'NJ'), ('Toms River', 'NJ'), ('Hamilton', 'NJ'), ('Trenton', 'NJ'),
    ('Clifton', 'NJ'), ('Camden', 'NJ'), ('Brick', 'NJ'), ('Cherry Hill', 'NJ'), ('Passaic', 'NJ'),
    ('Middletown', 'NJ'), ('Union City', 'NJ'), ('Old Bridge', 'NJ'), ('Franklin', 'NJ'), ('Bayonne', 'NJ'),
    ('Vineland', 'NJ'), ('Union', 'NJ'), ('Piscataway', 'NJ'), ('New Brunswick', 'NJ'), ('West New York', 'NJ'),
    ('Hoboken', 'NJ'), ('Perth Amboy', 'NJ'), ('East Brunswick', 'NJ'), ('West Orange', 'NJ'), ('Plainfield', 'NJ'),
    ('Albuquerque', 'NM'), ('Las Cruces', 'NM'), ('Rio Rancho', 'NM'), ('Santa Fe', 'NM'), ('Roswell', 'NM'),
    ('Farmington', 'NM'), ('Clovis', 'NM'), ('Hobbs', 'NM'), ('Alamogordo', 'NM'), ('Carlsbad', 'NM'),
    ('Gallup', 'NM'), ('Deming', 'NM'), ('Los Lunas', 'NM'), ('Sunland Park', 'NM'), ('Las Vegas', 'NM'),
    ('New York', 'NY'), ('Buffalo', 'NY'), ('Rochester', 'NY'), ('Yonkers', 'NY'), ('Syracuse', 'NY'),
    ('Albany', 'NY'), ('New Rochelle', 'NY'), ('Mount Vernon', 'NY'), ('Schenectady', 'NY'), ('Utica', 'NY'),
    ('White Plains', 'NY'), ('Hempstead', 'NY'), ('Troy', 'NY'), ('Niagara Falls', 'NY'), ('Binghamton', 'NY'),
    ('Freeport', 'NY'), ('Valley Stream', 'NY'), ('Long Beach', 'NY'), ('Rome', 'NY'), ('North Tonawanda', 'NY'),
    ('Ithaca', 'NY'), ('Poughkeepsie', 'NY'), ('Jamestown', 'NY'), ('Elmira', 'NY'), ('Saratoga Springs', 'NY'),
    ('Auburn', 'NY'), ('Glens Falls', 'NY'), ('Middletown', 'NY'), ('Kingston', 'NY'), ('Peekskill', 'NY'),
    ('Charlotte', 'NC'), ('Raleigh', 'NC'), ('Greensboro', 'NC'), ('Durham', 'NC'), ('Winston-Salem', 'NC'),
    ('Fayetteville', 'NC'), ('Cary', 'NC'), ('Wilmington', 'NC'), ('High Point', 'NC'), ('Concord', 'NC'),
    ('Greenville', 'NC'), ('Asheville', 'NC'), ('Gastonia', 'NC'), ('Jacksonville', 'NC'), ('Chapel Hill', 'NC'),
    ('Huntersville', 'NC'), ('Apex', 'NC'), ('Burlington', 'NC'), ('Kannapolis', 'NC'), ('Rocky Mount', 'NC'),
    ('Wilson', 'NC'), ('Wake Forest', 'NC'), ('Hickory', 'NC'), ('Indian Trail', 'NC'), ('Mooresville', 'NC'),
    ('Holly Springs', 'NC'), ('Monroe', 'NC'), ('Goldboro', 'NC'), ('Salisbury', 'NC'), ('Matthews', 'NC'),
    ('Fargo', 'ND'), ('Bismarck', 'ND'), ('Grand Forks', 'ND'), ('Minot', 'ND'), ('West Fargo', 'ND'),
    ('Williston', 'ND'), ('Dickinson', 'ND'), ('Mandan', 'ND'), ('Jamestown', 'ND'), ('Wahpeton', 'ND'),
    ('Columbus', 'OH'), ('Cleveland', 'OH'), ('Cincinnati', 'OH'), ('Toledo', 'OH'), ('Akron', 'OH'),
    ('Dayton', 'OH'), ('Parma', 'OH'), ('Canton', 'OH'), ('Youngstown', 'OH'), ('Lorain', 'OH'),
    ('Hamilton', 'OH'), ('Springfield', 'OH'), ('Kettering', 'OH'), ('Elyria', 'OH'), ('Lakewood', 'OH'),
    ('Cuyahoga Falls', 'OH'), ('Middletown', 'OH'), ('Newark', 'OH'), ('Dublin', 'OH'), ('Mansfield', 'OH'),
    ('Mentor', 'OH'), ('Beavercreek', 'OH'), ('Cleveland Heights', 'OH'), ('Strongsville', 'OH'), ('Fairfield', 'OH'),
    ('Grove City', 'OH'), ('Warren', 'OH'), ('Findlay', 'OH'), ('Lancaster', 'OH'), ('Westerville', 'OH'),
    ('Huber Heights', 'OH'), ('Delaware', 'OH'), ('Lima', 'OH'), ('Reynoldsburg', 'OH'), ('Marion', 'OH'),
    ('Oklahoma City', 'OK'), ('Tulsa', 'OK'), ('Norman', 'OK'), ('Broken Arrow', 'OK'), ('Lawton', 'OK'),
    ('Edmond', 'OK'), ('Moore', 'OK'), ('Midwest City', 'OK'), ('Enid', 'OK'), ('Stillwater', 'OK'),
    ('Muskogee', 'OK'), ('Bartlesville', 'OK'), ('Shawnee', 'OK'), ('Owasso', 'OK'), ('Ponca City', 'OK'),
    ('Ardmore', 'OK'), ('Yukon', 'OK'), ('Duncan', 'OK'), ('Del City', 'OK'), ('Bixby', 'OK'),
    ('Portland', 'OR'), ('Eugene', 'OR'), ('Salem', 'OR'), ('Gresham', 'OR'), ('Hillsboro', 'OR'),
    ('Beaverton', 'OR'), ('Bend', 'OR'), ('Medford', 'OR'), ('Springfield', 'OR'), ('Corvallis', 'OR'),
    ('Albany', 'OR'), ('Tigard', 'OR'), ('Lake Oswego', 'OR'), ('Keizer', 'OR'), ('Grants Pass', 'OR'),
    ('Oregon City', 'OR'), ('McMinnville', 'OR'), ('Redmond', 'OR'), ('Tualatin', 'OR'), ('West Linn', 'OR'),
    ('Philadelphia', 'PA'), ('Pittsburgh', 'PA'), ('Allentown', 'PA'), ('Erie', 'PA'), ('Reading', 'PA'),
    ('Scranton', 'PA'), ('Bethlehem', 'PA'), ('Lancaster', 'PA'), ('Harrisburg', 'PA'), ('Altoona', 'PA'),
    ('York', 'PA'), ('Wilkes-Barre', 'PA'), ('Chester', 'PA'), ('Hershey', 'PA'), ('Bethel Park', 'PA'),
    ('Williamsport', 'PA'), ('Monroeville', 'PA'), ('Easton', 'PA'), ('Plum', 'PA'), ('Lebanon', 'PA'),
    ('Hazleton', 'PA'), ('New Castle', 'PA'), ('Johnstown', 'PA'), ('West Mifflin', 'PA'), ('Chambersburg', 'PA'),
    ('Murrysville', 'PA'), ('McKeesport', 'PA'), ('Baldwin', 'PA'), ('Carlisle', 'PA'), ('West Chester', 'PA'),
    ('Providence', 'RI'), ('Warwick', 'RI'), ('Cranston', 'RI'), ('Pawtucket', 'RI'), ('East Providence', 'RI'),
    ('Woonsocket', 'RI'), ('Coventry', 'RI'), ('Cumberland', 'RI'), ('North Providence', 'RI'), ('South Kingstown', 'RI'),
    ('West Warwick', 'RI'), ('Johnston', 'RI'), ('North Kingstown', 'RI'), ('Newport', 'RI'), ('Bristol', 'RI'),
    ('Columbia', 'SC'), ('Charleston', 'SC'), ('North Charleston', 'SC'), ('Mount Pleasant', 'SC'), ('Rock Hill', 'SC'),
    ('Greenville', 'SC'), ('Summerville', 'SC'), ('Goose Creek', 'SC'), ('Hilton Head Island', 'SC'), ('Sumter', 'SC'),
    ('Florence', 'SC'), ('Spartanburg', 'SC'), ('Myrtle Beach', 'SC'), ('Greer', 'SC'), ('Aiken', 'SC'),
    ('Anderson', 'SC'), ('Mauldin', 'SC'), ('Hanahan', 'SC'), ('Greenwood', 'SC'), ('Conway', 'SC'),
    ('Sioux Falls', 'SD'), ('Rapid City', 'SD'), ('Aberdeen', 'SD'), ('Brookings', 'SD'), ('Watertown', 'SD'),
    ('Mitchell', 'SD'), ('Yankton', 'SD'), ('Pierre', 'SD'), ('Huron', 'SD'), ('Spearfish', 'SD'),
    ('Memphis', 'TN'), ('Nashville', 'TN'), ('Knoxville', 'TN'), ('Chattanooga', 'TN'), ('Clarksville', 'TN'),
    ('Murfreesboro', 'TN'), ('Franklin', 'TN'), ('Jackson', 'TN'), ('Johnson City', 'TN'), ('Bartlett', 'TN'),
    ('Hendersonville', 'TN'), ('Kingsport', 'TN'), ('Collierville', 'TN'), ('Cleveland', 'TN'), ('Smyrna', 'TN'),
    ('Germantown', 'TN'), ('Brentwood', 'TN'), ('Columbia', 'TN'), ('La Vergne', 'TN'), ('Cookeville', 'TN'),
    ('Gallatin', 'TN'), ('Oak Ridge', 'TN'), ('Morristown', 'TN'), ('Spring Hill', 'TN'), ('Maryville', 'TN'),
    ('Bristol', 'TN'), ('Lebanon', 'TN'), ('Mount Juliet', 'TN'), ('East Ridge', 'TN'), ('Farragut', 'TN'),
    ('Houston', 'TX'), ('San Antonio', 'TX'), ('Dallas', 'TX'), ('Austin', 'TX'), ('Fort Worth', 'TX'),
    ('El Paso', 'TX'), ('Arlington', 'TX'), ('Corpus Christi', 'TX'), ('Plano', 'TX'), ('Laredo', 'TX'),
    ('Lubbock', 'TX'), ('Garland', 'TX'), ('Irving', 'TX'), ('Amarillo', 'TX'), ('Grand Prairie', 'TX'),
    ('Brownsville', 'TX'), ('McKinney', 'TX'), ('Frisco', 'TX'), ('Pasadena', 'TX'), ('Mesquite', 'TX'),
    ('Killeen', 'TX'), ('McAllen', 'TX'), ('Waco', 'TX'), ('Denton', 'TX'), ('Midland', 'TX'),
    ('Carrollton', 'TX'), ('Round Rock', 'TX'), ('Abilene', 'TX'), ('Pearland', 'TX'), ('Richardson', 'TX'),
    ('Odessa', 'TX'), ('Sugar Land', 'TX'), ('Beaumont', 'TX'), ('The Woodlands', 'TX'), ('Tyler', 'TX'),
    ('Salt Lake City', 'UT'), ('West Valley City', 'UT'), ('Provo', 'UT'), ('West Jordan', 'UT'), ('Orem', 'UT'),
    ('Sandy', 'UT'), ('Ogden', 'UT'), ('St. George', 'UT'), ('Layton', 'UT'), ('South Jordan', 'UT'),
    ('Lehi', 'UT'), ('Millcreek', 'UT'), ('Taylorsville', 'UT'), ('Logan', 'UT'), ('Murray', 'UT'),
    ('Burlington', 'VT'), ('South Burlington', 'VT'), ('Rutland', 'VT'), ('Essex Junction', 'VT'), ('Barre', 'VT'),
    ('Montpelier', 'VT'), ('Winooski', 'VT'), ('St. Albans', 'VT'), ('Newport', 'VT'), ('Bellows Falls', 'VT'),
    ('Virginia Beach', 'VA'), ('Norfolk', 'VA'), ('Chesapeake', 'VA'), ('Richmond', 'VA'), ('Newport News', 'VA'),
    ('Alexandria', 'VA'), ('Hampton', 'VA'), ('Roanoke', 'VA'), ('Portsmouth', 'VA'), ('Suffolk', 'VA'),
    ('Lynchburg', 'VA'), ('Harrisonburg', 'VA'), ('Leesburg', 'VA'), ('Charlottesville', 'VA'), ('Danville', 'VA'),
    ('Manassas', 'VA'), ('Petersburg', 'VA'), ('Winchester', 'VA'), ('Salem', 'VA'), ('Staunton', 'VA'),
    ('Fairfax', 'VA'), ('Hopewell', 'VA'), ('Colonial Heights', 'VA'), ('Radford', 'VA'), ('Bristol', 'VA'),
    ('Waynesboro', 'VA'), ('Christiansburg', 'VA'), ('Culpeper', 'VA'), ('Front Royal', 'VA'), ('Martinsville', 'VA'),
    ('Seattle', 'WA'), ('Spokane', 'WA'), ('Tacoma', 'WA'), ('Vancouver', 'WA'), ('Bellevue', 'WA'),
    ('Kent', 'WA'), ('Everett', 'WA'), ('Renton', 'WA'), ('Yakima', 'WA'), ('Federal Way', 'WA'),
    ('Spokane Valley', 'WA'), ('Bellingham', 'WA'), ('Kennewick', 'WA'), ('Auburn', 'WA'), ('Pasco', 'WA'),
    ('Marysville', 'WA'), ('Lakewood', 'WA'), ('Redmond', 'WA'), ('Shoreline', 'WA'), ('Richland', 'WA'),
    ('Kirkland', 'WA'), ('Sammamish', 'WA'), ('Olympia', 'WA'), ('Lacey', 'WA'), ('Burien', 'WA'),
    ('Charleston', 'WV'), ('Huntington', 'WV'), ('Morgantown', 'WV'), ('Parkersburg', 'WV'), ('Wheeling', 'WV'),
    ('Weirton', 'WV'), ('Fairmont', 'WV'), ('Martinsburg', 'WV'), ('Beckley', 'WV'), ('Clarksburg', 'WV'),
    ('South Charleston', 'WV'), ('St. Albans', 'WV'), ('Vienna', 'WV'), ('Bluefield', 'WV'), ('Moundsville', 'WV'),
    ('Milwaukee', 'WI'), ('Madison', 'WI'), ('Green Bay', 'WI'), ('Kenosha', 'WI'), ('Racine', 'WI'),
    ('Appleton', 'WI'), ('Waukesha', 'WI'), ('Eau Claire', 'WI'), ('Oshkosh', 'WI'), ('Janesville', 'WI'),
    ('West Allis', 'WI'), ('La Crosse', 'WI'), ('Sheboygan', 'WI'), ('Wauwatosa', 'WI'), ('Fond du Lac', 'WI'),
    ('Brookfield', 'WI'), ('New Berlin', 'WI'), ('Wausau', 'WI'), ('Menomonee Falls', 'WI'), ('Greenfield', 'WI'),
    ('Franklin', 'WI'), ('Oak Creek', 'WI'), ('Sun Prairie', 'WI'), ('Manitowoc', 'WI'), ('West Bend', 'WI'),
    ('Fitchburg', 'WI'), ('Mount Pleasant', 'WI'), ('Neenah', 'WI'), ('Stevens Point', 'WI'), ('Superior', 'WI'),
    ('Cheyenne', 'WY'), ('Casper', 'WY'), ('Laramie', 'WY'), ('Gillette', 'WY'), ('Rock Springs', 'WY'),
    ('Sheridan', 'WY'), ('Green River', 'WY'), ('Evanston', 'WY'), ('Riverton', 'WY'), ('Jackson', 'WY'),
]

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
</head><body><h1>Business Funding & Processing — All Locations</h1><ul>
''' + '\n'.join(city_links) + '''
</ul></body></html>'''
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print('Generated', count, 'city pages in', base_dir)
    print('Sitemap written to sitemap-cities.xml')
    print('Index written to cities/index.html')

if __name__ == '__main__':
    generate_all()
