# -*- coding: cp1251 -*-
print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())


title = "Education" 
print(f"<title>{title}</title>")

with open('header.html', 'r') as html:
    print(html.read())
with open('education.html', 'r') as html:
    print(html.read())
with open('footer.html', 'r') as html:
    print(html.read())