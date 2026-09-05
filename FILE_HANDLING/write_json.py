import json
with open("pratice.json", "w") as file:
    data = {
        "name": "abhay",
        "age": 25,
        "gender": "male"
    }
    json.dump(data, file)
    print("Data written to pratice.json successfully.")