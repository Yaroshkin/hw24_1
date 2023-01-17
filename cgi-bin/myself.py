
print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())


title = "About" 
print(f"<title>{title}</title>")

with open('header.html', 'r') as html:
    print(html.read())

with open('about.html', 'r') as html:
    print(html.read())
    
with open('footer.html', 'r') as html:
    print(html.read())