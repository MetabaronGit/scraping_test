import requests
import bs4
import sys

# vzhled URL po zadání argumentů
# URL = "https://ib.fio.cz/ib/transparent?a=2800396030&f=01.03.2021&t=01.04.2021"
URL = "https://ib.fio.cz/ib/transparent?a={account_nr}&f={date_from}&t={date_to}"

# Hlavička hledané tabulky
TARGET_HEADER = ["Datum", "Částka", "Typ", "Název protiúčtu", "Zpráva pro příjemce", "KS", "VS", "SS", "Poznámka"]


# starting_url = "https://www.6dhub.cz"
# link_selektor = "div.article_tile a"
# nadpis_selektor = "div.container h1"
# fulltext_selektor = "div.single__body p"

# def najdi_selektorem(html, selektor) -> str:
#     soup = BeautifulSoup(html, 'html.parser')
#     nalezene_texty = []
#
#     for elem in soup.select(selektor):
#         text = elem.text
#         nalezene_texty.append(text)
#
#     return " ".join(nalezene_texty)


# def get_data(account_nr: str, date_from: str, date_to: str) -> None:
#     """Stáhne výpis pohybu na účtu account_nr v požadovaném časovém rozmezí."""
#
#     web_content = requests.get(URL.format(account_nr=account_nr, date_from=date_from, date_to=date_to))
#     soup = bs4.BeautifulSoup(web_content.text, "html.parser")
#     # print(web_content.status_code)
#     # table_content = soup.find('table', {'class': 'table'}).text
#     # print(table_content)
#     payment_table = soup.select("table tbody tr")
#     for tag in payment_table:
#         print(tag)


def make_soup(url: str, payload: dict) -> bs4.BeautifulSoup:
    """
    Načte ze zadané URL s požadovanými argumenty kompletní HTML kód a vrátí soup objekt.
    """
    try:
        r = requests.get(url, params=payload)
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


def get_table(soup: bs4.BeautifulSoup, tag: str, css_id: str):
    target_tab = soup.find(tag), {"id": css_id}
    print(target_tab)


def main():
    # account_nr = "2800396030"
    # date_from = "01.03.2021"
    # date_to = "01.04.2021"
    # get_data(account_nr, date_from, date_to)
    arguments = {"account_nr": "2800396030", "date_from": "01.03.2021", "date_to": "01.04.2021"}
    html_doc = make_soup(URL, arguments)

    get_table(html_doc, "table", "idf61c66a14c7508978")
    # table_to_scrape = extract_table(html_doc, TARGET_HEADER)
    # i = html_doc.table.thead.tr
    # print(table_to_scrape)
    # print("type:", type(table_to_scrape))
    # print(table_to_scrape)



if __name__ == "__main__":
    main()
