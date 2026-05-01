with open('C:/Users/HP/mca-website/generate_cities.py', 'r') as f:
    content = f.read()
start = content.find("TEMPLATE = '''") + len("TEMPLATE = '''")
end = content.find("\n'''\n\nCITIES = [", start)
print('start:', start)
print('end:', end)
print('end snippet:', repr(content[end:end+20]))
print('end+5 snippet:', repr(content[end+5:end+25]))
rest = content[end+5:]
rest_start = rest.find(']\n\n')
print('rest_start:', rest_start)
print('rest snippet:', repr(rest[rest_start:rest_start+20]))
print('rest after slice:', repr(rest[rest_start+2:rest_start+40]))
