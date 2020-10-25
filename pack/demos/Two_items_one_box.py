from request import request_function

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
      "quantity": 2
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
    ]
    }"""

r = request_function(payload)
print(r.text)
