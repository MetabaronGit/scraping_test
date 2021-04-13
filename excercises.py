from bs4 import BeautifulSoup
import requests

URL = "http://python.org"
URL = "http://example.com"

html_doc = requests.get(URL)
soup = BeautifulSoup(html_doc.text, "html.parser")

# root_childs = [e.name for e in soup.body.children if e.name is not None]
# print(root_childs)

i = soup.select("body div")
print(soup.prettify())
# print(i)

# for tag in i:
#     print(tag)