import requests


url = 'https://api.paccurate.io/'

payload = """{
      "itemSets": [{
      "refId": 0,
      "dimensions": {"x": 5.5, "y": 6, "z": 6},
      "quantity": 3
  }],
  "boxTypeSets": ["fedex"]
}"""


headers = {'Authorization': 'apikey PVjuMKCNFDZcPKdSJgeH_zun3r2ZAAiU-cXk0TClmc-zEUCogYBbvbepucZV8T3z'}

r = requests.post(url, data=payload, headers=headers)


print(r)
print(r.text)
