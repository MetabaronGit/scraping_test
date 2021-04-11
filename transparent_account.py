import requests
import bs4
import sys

HEADER = ["Datum", "Částka", "Typ", "Název protiúčtu", "Zpráva pro příjemce", "KS", "VS", "SS", "Poznámka"]
URL = "https://ib.fio.cz/ib/transparent?a=2800396030&f=01.03.2021&t=01.04.2021"
URL = "https://ib.fio.cz/ib/transparent?a={account_nr}&f={date_from}&t={date_to}"


def get_data(account_nr: str, date_from: str, date_to: str) -> None:
    """Stáhne výpis pohybu na účtu account_nr v požadovaném časovém rozmezí."""
    web_content = requests.get(URL.format(account_nr=account_nr, date_from=date_from, date_to=date_to))
    soup = bs4.BeautifulSoup(web_content.text, "html.parser")
    # print(web_content.status_code)

    table_content = soup.find('table.tbody', {'class': 'table'}).text
    print(table_content)


def make_soup(URL,payload):
    try:
        r = requests.get(URL, params=payload)
        r.raise_for_status()
        soup = BS(r.text, "html.parser")
        return soup
    except HTTPError:
        print('Could not retrieve the page')
    except:
        print(sys.exc_info()[:1])


def main():
    account_nr = "2800396030"
    date_from = "01.03.2021"
    date_to = "01.04.2021"
    get_data(account_nr, date_from, date_to)


if __name__ == "__main__":
    main()
