from request import request_function


payload = """{
  "itemSets": [
    {
      "refId": 0,
      "color": "tomato",
      "weight": 0,
      "dimensions": {
        "x": 5,
        "y": 6,
        "z": 4
      },
      "quantity": 1
    },
    {
      "refId": 1,
      "color": "cornflowerblue",
      "weight": 0,
      "dimensions": {
        "x": 2.5,
        "y": 3,
        "z": 2
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
    ]
    }"""

r = request_function(payload)
print(r.text)
