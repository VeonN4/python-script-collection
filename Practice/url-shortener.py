import requests

url = input("Enter URL: ")
TOKEN = "aa409994072b1120b2af5fce328b089dcdbc7e88"

if not url.startswith("https"):
    url = list(url)
    url.insert(0, "https://")
    url = ''.join(url)

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

json = { "long_url": "{}".format(url), "domain": "bit.ly" }

request = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=json)
data = request.json()

print("Shortened URL:", data["link"])