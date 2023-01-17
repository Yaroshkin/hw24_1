# -*- coding: cp1251 -*-
print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())


title = "Досвід роботи " 
print(f"<title>{title}</title>")

with open('header.html', 'r') as html:
    print(html.read())
with open('work_ex.html', 'r') as html:
    print(html.read())
with open('footer.html', 'r') as html:
    print(html.read())