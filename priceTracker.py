import asyncio

from utils import lenta_get_price, metro_get_price, links_map


async def check_market(channel):
    price = None
    while True:
        metro = metro_get_price(links_map.get("metro"))
        lenta = lenta_get_price(links_map.get("lenta"))
        current_price = None
        message = None
        if lenta.get("price") < metro.get("price"):
            current_price = lenta.get('price')
            message = f"Current best price {lenta.get('price')} деревянных in {lenta.get('marketName')}, da link {lenta.get('URL')}"
        if metro.get("price") < lenta.get("price"):
            current_price = metro.get('price')
            message = f"Current best price {metro.get('price')} деревянных in {metro.get('marketName')}, da link {metro.get('URL')}"
        if price is not None:
            if price > current_price:
                await channel.send("https://imgur.com/m4Vertv")
                await channel.send("Yet another beautiful day for fans of doshirak: price went down")
            if price < current_price:
                await channel.send("https://imgur.com/RzJItGX")
                await channel.send("THE END IS NEAR, PRICE IS RISING, STOCKPILE WHILE YOU CAN")
            if price == current_price:
                await channel.send("https://imgur.com/a/M0lLThx")
                await channel.send("No price fluctuation and no idea what it means either")
        price = current_price
        await channel.send(message)
        await asyncio.sleep(21600)
