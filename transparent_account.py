import requests
import bs4

web_content = requests.get("http://example.com")
soup = bs4.BeautifulSoup(web_content.text, "html.parser")
print(web_content.status_code)
print(soup.find(charset="utf-8"))
print(soup.find("Example"))
