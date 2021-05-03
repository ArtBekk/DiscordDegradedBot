import asyncio
import threading

from utils import lenta_get_price, metro_get_price, links_map


def thread_entry(client):
    asyncio.run(check_market(client))


async def check_market(client):
    print(f"Launched from {threading.Thread.name}")
    # very_important_economical_channel = client.get_channel(830723947904368651)
    metro = metro_get_price(links_map.get("metro"))
    lenta = lenta_get_price(links_map.get("lenta"))
    message = ""
    if lenta.get("price") < metro.get("price"):
        message = f"Current best price {metro.get('price')} деревянных in {metro.get('marketName')}"
    if metro.get("price") < lenta.get("price"):
        message = f"Current best price {lenta.get('price')} деревянных in {lenta.get('marketName')}"
    print(message)
    # await very_important_economical_channel.send("message")
