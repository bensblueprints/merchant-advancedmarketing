import os

FUNDING_URL = 'https://my.americasfundingexperts.com/?id=1820217000240009008'

for fname in ['mca.html','term-loan.html','sba.html','equipment.html','loc.html','processing.html','invoice-factoring.html']:
    path = f'public/loans/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(f'href="{FUNDING_URL}" class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>', 'href="#apply" class="btn btn-primary btn-lg">Apply Now &rarr;</a>')
    content = content.replace(f'href="{FUNDING_URL}" class="btn btn-primary">Apply Now</a>', 'href="#apply" class="btn btn-primary">Apply Now</a>')
    content = content.replace('Or fill out the form below and we will call you.', 'Fill out the application below and get redirected to our funding partners instantly.')
    content = content.replace('>Prefer a Callback?</h2>', '>Apply Now</h2>')
    content = content.replace('Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.', 'Complete the application below. A funding advisor will review your information, send you a confirmation email, and redirect you to our lending partners to finalize your funding.')
    content = content.replace('>Request a Callback &rarr;</button>', '>Submit Application &rarr;</button>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {path}')

path = 'public/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(f'href="{FUNDING_URL}" class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>', 'href="#apply" class="btn btn-primary btn-lg">Apply Now &rarr;</a>')
content = content.replace(f'href="{FUNDING_URL}" class="btn btn-primary">Apply Now</a>', 'href="#apply" class="btn btn-primary">Apply Now</a>')
content = content.replace('Or fill out the form below and we will call you.', 'Fill out the application below and get redirected to our funding partners instantly.')
content = content.replace('>Prefer a Callback?</h2>', '>Apply Now</h2>')
content = content.replace('Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.', 'Complete the application below. A funding advisor will review your information, send you a confirmation email, and redirect you to our lending partners to finalize your funding.')
content = content.replace('>Request a Callback &rarr;</button>', '>Submit Application &rarr;</button>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Updated {path}')
