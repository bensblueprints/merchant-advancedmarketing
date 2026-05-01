import os
from datetime import datetime

BASE_URL = 'https://merchant.advancedmarketing.co'
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

LOAN_TYPES = ['mca', 'term-loan', 'sba', 'equipment', 'loc', 'processing', 'invoice-factoring']

def today():
    return datetime.now().strftime('%Y-%m-%d')

def main():
    urls = []

    # Core pages
    urls.append((f'{BASE_URL}/', '1.0'))
    urls.append((f'{BASE_URL}/admin', '0.1'))

    # Loan type main pages
    for lt in LOAN_TYPES:
        urls.append((f'{BASE_URL}/loans/{lt}.html', '0.9'))

    # State and city pages
    for lt in LOAN_TYPES:
        for state_code in STATE_NAMES:
            urls.append((f'{BASE_URL}/loans/{lt}/{state_code}.html', '0.8'))
            state_dir = f'public/loans/{lt}/{state_code}'
            if os.path.exists(state_dir):
                for city_file in os.listdir(state_dir):
                    if city_file.endswith('.html'):
                        city_slug = city_file.replace('.html', '')
                        urls.append((f'{BASE_URL}/loans/{lt}/{state_code}/{city_slug}.html', '0.7'))

    # Build XML
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url, priority in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{url}</loc>')
        xml.append(f'    <lastmod>{today()}</lastmod>')
        xml.append(f'    <changefreq>weekly</changefreq>')
        xml.append(f'    <priority>{priority}</priority>')
        xml.append('  </url>')
    xml.append('</urlset>')

    with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml))

    print(f'Generated sitemap.xml with {len(urls)} URLs')

if __name__ == '__main__':
    main()
