import urllib.request

from bs4 import BeautifulSoup

links_map = {
    "metro": "https://kemerovo.metro-cc.ru/category/bakaleya/produkty-bystrogo-prigotovleniya/lapsha-govyadina-doshirak-90g-488492",
    "lenta": "https://lenta.com/product/lapsha-bystrogo-prigotovleniya-doshirak-so-vk-govyadiny-rossiya-90g-051625/"}


def get_price(url: str):
    if "lenta" in url:
        return lenta_get_price(url)
    elif "metro" in url:
        return metro_get_price(url)


def lenta_get_price(url: str):
    sample = urllib.request.urlopen(url)
    my_bytes = sample.read()
    my_str = my_bytes.decode("utf8")
    sample.close()
    soup = BeautifulSoup(my_str, 'html.parser')
    regular_price = soup.find('div', {"class": "sku-price sku-price--regular sku-prices-block__price"}).text.split()
    card_price = soup.find('div', {"class": "sku-price sku-price--primary sku-prices-block__price"}).text.split()
    regular_price = f"{regular_price[0]},{regular_price[1]}{regular_price[2]}"
    card_price = f"{card_price[0]},{card_price[1]}{card_price[2]}"
    return {
        'marketName': "Lenta",
        'message': f"Beef dooshirak's price in Lenta for bums w/o the card: {regular_price} and price for kings with the card: {card_price}",
        'price': card_price}


def metro_get_price(url: str):
    sample = urllib.request.urlopen(url)
    my_bytes = sample.read()
    my_str = my_bytes.decode("utf8")
    sample.close()
    soup = BeautifulSoup(my_str, 'html.parser')
    price = "".join(soup.find('span', {"itemprop": "price"}).text.split())
    return {
        'marketName': "Metro",
        'message': f"Beef doshirak's price in metro {price} в деревянных",
        'price': price
    }
