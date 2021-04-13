import requests
import bs4
import sys

# vzhled URL po zadání argumentů
URL = "https://ib.fio.cz/ib/transparent?a=2800396030&f=01.03.2021&t=01.04.2021"
# URL = "https://ib.fio.cz/ib/transparent?a={account_nr}&f={date_from}&t={date_to}"

# Hlavička hledané tabulky
TARGET_HEADER = ["Datum", "Částka", "Typ", "Název protiúčtu", "Zpráva pro příjemce", "KS", "VS", "SS", "Poznámka"]


def make_soup(url: str) -> bs4.BeautifulSoup:
    """
    Načte ze zadané URL s požadovanými argumenty kompletní HTML kód a vrátí soup objekt.
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        return soup
    except requests.HTTPError:
        print('Could not retrieve the page')
    except Exception:
        print(sys.exc_info()[:1])


def extract_data(soup):
    # extracts transfers into a list of lists
    table_to_scrape = extract_table(soup, TARGET_HEADER)
    transfers = [TARGET_HEADER]
    for row in filter(lambda x: x != '\n', table_to_scrape.tbody.children):
        transfers.append([])
        for info in filter(lambda x: x != '\n', row.children):
            transfers[-1].append(info.attrs.get('data-value') or info.string)
    return transfers


def extract_table(soup, target_header):
    # found by the content
    # jednotlivé sloupce tabulky: table.thead.tr.th
    for table in soup.find_all('table'):
        header = [child.string for child in table.thead.tr.children if child.string != '\n']
        if header == target_header:
            return table


def main():
    # account_nr = "2800396030"
    # date_from = "01.03.2021"
    # date_to = "01.04.2021"
    # arguments = {"account_nr": "2800396030", "date_from": "01.03.2021", "date_to": "01.04.2021"}
    html_doc = make_soup(URL)
    table = extract_data(html_doc)
    print(table)


if __name__ == "__main__":
    main()
