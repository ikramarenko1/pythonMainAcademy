import requests


def get_offers():
    url = "https://nanutru.org/api/wm/offers.json?id=32-1c8816175bad926abc74089595590f85"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data


offers = get_offers()
offers_ids = sorted([offer for offer in offers])
print(", ".join(offers_ids))