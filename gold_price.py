import requests
import bs4
import datetime
import csv
import os

# ToDo: CSS selectory

URL = "https://markets.businessinsider.com/commodities/gold-price"
# DATE_FORMAT = '%d.%m.%Y %H:%M'
DATE_FORMAT = '%d.%m.%Y'
HEADER = ["Date", "Price"]

def request_gold_price() -> str:
    """Zjistí aktuální cenu zlata"""
    content = requests.get(URL)
    soup = bs4.BeautifulSoup(content.text, "html.parser")

    # print("status:", content.status_code)

    # aktuální cena zlata
    # <span data-v-0ae43770="" class="price-section__current-value">1,744.10</span>
    return soup.find('span', {'class': 'price-section__current-value'}).text


def save_data(date: str, price: str) -> None:
    """Přidá data do souboru csv"""
    if 'gold_prices2.csv' in os.listdir():
        mode = "a"
    else:
        mode = "w"

    with open('gold_prices2.csv', mode, newline="") as f:
        writer = csv.writer(f)
        writer2 = csv.DictWriter(f, HEADER)
        if mode == "w":
            # writer.writerow(["date","price"])
            writer2.writeheader()
        # writer.writerow([date, float(price)])
        writer2.writerow({HEADER[0]: date, HEADER[1]: float(price)})


def main():
    actual_gold_price = request_gold_price()
    actual_time = datetime.datetime.now().strftime(DATE_FORMAT)

    print(f"{actual_time} je aktuální cena zlata za trojskou unci {actual_gold_price} $.")

    save_data(actual_time, actual_gold_price)


if __name__ == "__main__":
    main()



