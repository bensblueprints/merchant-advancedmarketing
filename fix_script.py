with open('C:/Users/HP/mca-website/generate_cities.py', 'r') as f:
    content = f.read()

start = content.find("TEMPLATE = '''") + len("TEMPLATE = '''")
end = content.find("'''\n\nCITIES = [", start)
print('start:', start, 'end:', end)
template = content[start:end]

result = []
i = 0
while i < len(template):
    brace_open = template.find('{', i)
    if brace_open == -1:
        result.append(template[i:])
        break
    brace_close = template.find('}', brace_open)
    if brace_close == -1:
        result.append(template[i:])
        break
    inner = template[brace_open + 1:brace_close]
    if '|' in inner:
        result.append(template[i:brace_open])
        result.append('[@')
        result.append(inner)
        result.append('@]')
    else:
        result.append(template[i:brace_close + 1])
    i = brace_close + 1
template = ''.join(result)

rest = content[end + 3:]
rest_start = rest.find(']\n\n')
print('rest_start:', rest_start)
rest = rest[rest_start + 2:]

new_content = '''from generate_cities import CITIES, STATE_MAP
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

TEMPLATE = \'\'\'''' + template + '''\'\'\'
''' + rest

with open('C:/Users/HP/mca-website/generate_cities_v2.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Fixed script written to generate_cities_v2.py')
