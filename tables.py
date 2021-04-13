from bs4 import BeautifulSoup
import requests

# vzhled URL po zadání argumentů
# URL = "https://ib.fio.cz/ib/transparent?a=2800396030&f=01.03.2021&t=01.04.2021"
URL = "https://ib.fio.cz/ib/transparent?a={account_nr}&f={date_from}&t={date_to}"
arguments = {"account_nr": "2800396030", "date_from": "01.03.2021", "date_to": "01.04.2021"}

content = requests.get(URL, arguments)
soup = BeautifulSoup(content.text, "html.parser")

table_headers = [x for x in soup.table.thead]

print(table_headers)