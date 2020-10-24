import requests

url = 'https://api.paccurate.io/'

payload = """{
  "itemSets": [
    {
      "refId": 0,
      "color": "tomato",
      "weight": 2,
      "dimensions": {
        "x": 5,
        "y": 6,
        "z": 4
      },
      "quantity": 4
    }
  ],
  "boxTypes": [
    {
      "weightMax": 150,
      "name": "5x6x8",
      "dimensions": {
        "x": 5,
        "y": 6,
        "z": 8
      }
    }
  ],
}"""


headers = {'Authorization': 'apikey PVjuMKCNFDZcPKdSJgeH_zun3r2ZAAiU-cXk0TClmc-zEUCogYBbvbepucZV8T3z'}

r = requests.post(url, data=payload, headers=headers)


print(r)
print(r.text)