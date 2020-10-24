from request import request_function

payload = """{
      "itemSets": [{
      "refId": 0,
      "dimensions": {"x": 5.5, "y": 6, "z": 6},
      "quantity": 3
  }],
  "boxTypeSets": ["fedex"]
}"""
r=request_function(payload)
print (r.text)