import os
import re

files = ['mca.html','term-loan.html','sba.html','equipment.html','loc.html','processing.html','invoice-factoring.html']

# Match any old success handler pattern
old_pattern = re.compile(r"if \(json\.success\) \{ showToast\('.*?\); e\.target\.reset\(\); \}")
new = """if (json.success) {
          showToast('Thanks! Check your email for next steps. Redirecting to application...');
          setTimeout(() => { window.location.href = json.funding_url || 'https://my.americasfundingexperts.com/?id=1820217000240009008'; }, 2000);
        }"""

for f in files:
    path = f'public/loans/{f}'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_pattern.search(content):
        content = old_pattern.sub(new, content)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed {path}')
    else:
        print(f'Pattern not found in {path}')
