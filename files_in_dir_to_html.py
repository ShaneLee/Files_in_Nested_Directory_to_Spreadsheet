import glob

'''
  This script lists the pdfs in a directory and outputs a basic html page. 
  run python files_in_dir_to_html.py >> index.html
'''

print('''<html>\n<head>\n</head>\n<body>\n<ul>''')
for file in glob.glob("*.pdf"):
    print('<li>\n<a href="' + file + '">' + file + '</a>\n</li>')
print('''\n</ul>\n</body>\n</html>''')
