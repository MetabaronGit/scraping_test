# www.jobs.cz
# výpis nových nabídek s klíčovým slovem"python", Hradec Králové, pouze v zadané lokalitě (+0km)

# avaible radius 0, 10, 20, 30, 40, 50 km

# ukázka url
# Hradec Králové, 0km
# https://www.jobs.cz/prace/hradec-kralove/?q%5B%5D=python&locality%5Bradius%5D=0
# Praha, +10km
# https://www.jobs.cz/prace/praha/?q%5B%5D=python&locality%5Bradius%5D=10

import bs4
import requests
import sys
import datetime


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


def main():
    url = "https://www.jobs.cz/prace/{location}/?q%5B%5D={expression}&locality%5Bradius%5D={radius}".format(
        expression="python", location="hradec-kralove", radius="0")
    html_doc = make_soup(url)

    jobs = html_doc.find_all("h3", class_="search-list__main-info__title")
    for job in jobs:
         job_name = job.text.strip()
         link = job.find("a").attrs["href"]
         print(f"{job_name}: {link}")

    employers = html_doc.find_all("div", class_="search-list__main-info__company")
    for employer in employers:
        print(employer.text.strip())

    date_tags = html_doc.find_all("div", class_="search-list__status")
    for date_tag in date_tags:
        print(date_tag)
        date = date_tag.find("span", class_="label-added").attrs["data-label-added-valid-from"]
        print(date)
        # print(datetime.datetime.now())






if __name__ == "__main__":
    main()