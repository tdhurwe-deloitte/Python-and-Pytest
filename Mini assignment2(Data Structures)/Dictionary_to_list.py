original_dictionary = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
result = [[key] + value for key, value in original_dictionary.items()]
print(result)
