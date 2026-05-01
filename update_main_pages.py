import os
import re

FUNDING_URL = 'https://my.americasfundingexperts.com/?id=1820217000240009008'

# Files to update
LOAN_PAGES = [
    'public/loans/mca.html',
    'public/loans/term-loan.html',
    'public/loans/sba.html',
    'public/loans/equipment.html',
    'public/loans/loc.html',
    'public/loans/processing.html',
    'public/loans/invoice-factoring.html',
]

OTHER_PAGES = ['public/index.html']

def update_loan_page(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Nav Apply Now button
    content = content.replace(
        'href="#apply" class="btn btn-primary">Apply Now</a>',
        f'href="{FUNDING_URL}" class="btn btn-primary">Apply Now</a>'
    )

    # 2. Hero CTA buttons - various patterns
    content = content.replace(
        'href="#apply" class="btn btn-primary btn-lg">',
        f'href="{FUNDING_URL}" class="btn btn-primary btn-lg">'
    )

    # 3. Add subtext after hero CTA if not present
    if 'Or fill out the form below and we will call you.' not in content:
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for a Cash Advance &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for a Term Loan &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for an SBA Loan &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for Equipment Financing &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for a Line of Credit &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Get Your Free Rate Audit &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )
        content = content.replace(
            'class="btn btn-primary btn-lg">Apply for Invoice Factoring &rarr;</a>\n        </div>\n        <div class="loan-img">',
            f'class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>\n          <p style="margin-top:12px;font-size:13px;color:var(--gray-400);">Or fill out the form below and we will call you.</p>\n        </div>\n        <div class="loan-img">'
        )

    # 4. Form header text - replace various patterns
    content = re.sub(
        r'<h2>Apply for.*?</h2>',
        '<h2>Prefer a Callback?</h2>',
        content,
        count=1
    )

    # 5. Form subtext
    content = content.replace(
        '<p>Get a free, no-obligation quote in under 2 hours.</p>',
        '<p>Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.</p>'
    )

    # 6. Submit button text - various patterns
    content = content.replace('>Get My MCA Quote &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My Term Loan Quote &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My SBA Quote &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My Equipment Quote &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My LOC Quote &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My Free Rate Audit &rarr;</button>', '>Request a Callback &rarr;</button>')
    content = content.replace('>Get My Factoring Quote &rarr;</button>', '>Request a Callback &rarr;</button>')

    # 7. Form JS - update success handler
    old_js = """if (json.success) { showToast('Quote request submitted! We will call you within 2 hours.'); e.target.reset(); }
    else { showToast('Error. Please try again.'); }
  } catch { showToast('Network error. Please try again.'); }
  btn.innerHTML = original; btn.disabled = false;"""

    new_js = f"""if (json.success) {{
      showToast('Thanks! Check your email for next steps. Redirecting to application...');
      setTimeout(() => {{ window.location.href = json.funding_url || '{FUNDING_URL}'; }}, 2000);
    }} else {{ showToast('Error. Please try again.'); btn.innerHTML = original; btn.disabled = false; }}
  }} catch {{ showToast('Network error. Please try again.'); btn.innerHTML = original; btn.disabled = false; }}"""

    content = content.replace(old_js, new_js)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {path}')

def update_index_page(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update CTA buttons to external URL
    content = content.replace(
        'href="#apply" class="btn btn-primary btn-lg">Get Your Free Quote &rarr;</a>',
        f'href="{FUNDING_URL}" class="btn btn-primary btn-lg">Apply Now Directly &rarr;</a>'
    )

    # Update nav apply button
    content = content.replace(
        'href="#apply" class="btn btn-primary">Apply Now</a>',
        f'href="{FUNDING_URL}" class="btn btn-primary">Apply Now</a>'
    )

    # Update form header
    content = content.replace(
        '<h2>Get Your Free Funding Quote</h2>',
        '<h2>Prefer a Callback?</h2>'
    )

    # Update form subtext
    content = content.replace(
        '<p>Talk to a real funding advisor. No obligation, no hard credit pull.</p>',
        '<p>Fill out the form below and a funding advisor will call you within 2 hours to discuss your options. You will also receive a confirmation email with next steps.</p>'
    )

    # Update submit button
    content = content.replace(
        '>Get My Free Quote &rarr;</button>',
        '>Request a Callback &rarr;</button>'
    )

    # Update form JS
    old_js = """if (json.success) { showToast('Quote request submitted! We will call you within 2 hours.'); e.target.reset(); }
    else { showToast('Error. Please try again.'); }
  } catch { showToast('Network error. Please try again.'); }
  btn.innerHTML = original; btn.disabled = false;"""

    new_js = f"""if (json.success) {{
      showToast('Thanks! Check your email for next steps. Redirecting to application...');
      setTimeout(() => {{ window.location.href = json.funding_url || '{FUNDING_URL}'; }}, 2000);
    }} else {{ showToast('Error. Please try again.'); btn.innerHTML = original; btn.disabled = false; }}
  }} catch {{ showToast('Network error. Please try again.'); btn.innerHTML = original; btn.disabled = false; }}"""

    content = content.replace(old_js, new_js)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {path}')

if __name__ == '__main__':
    for path in LOAN_PAGES:
        if os.path.exists(path):
            update_loan_page(path)
        else:
            print(f'Not found: {path}')

    for path in OTHER_PAGES:
        if os.path.exists(path):
            update_index_page(path)
        else:
            print(f'Not found: {path}')
