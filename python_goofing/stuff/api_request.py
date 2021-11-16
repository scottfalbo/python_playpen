import requests


def get_quote():
    path = "http://sunnyquotes.net/q.php?random"
    r = requests.get(url = path)
    data = r.json()

    print(data['sqQuote'])
    print(data['sqWho'])

