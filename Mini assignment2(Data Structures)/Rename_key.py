sampleDict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

print(f"Old dictionary : {sampleDict}")
sampleDict["location"] = sampleDict.pop("city")
print(f"New dictionary : {sampleDict}")