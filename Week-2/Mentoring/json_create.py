import json

#REFERENCE :  https://www.w3schools.com/python/python_json.asp

def exDictionary():
    dictionary = {'a': 34, 'b': 61, 'c': 82}
    jsonString = json.dumps(dictionary, indent=4)
    print(jsonString)

# def exList():
#     myList = [{'a': 54}, {'b': 41, 'c': 87}]
#     jsonString = json.dumps(myList, indent=4)
#     print(jsonString)


# def exTuple():
#     myTuple = ({'a': 54}, {'b': 41, 'c': 87})
#     jsonString = json.dumps(myTuple, indent=4)
#     print(jsonString)

# def parseJson():
#     dictionary = {'a': 34, 'b': 61, 'c': 82}
#     jsonString = json.dumps(dictionary, indent=4)
#     print(f"JSON \n{jsonString}")
#     parseJson = json.loads(jsonString)
#     print(f"Parse ->>> {parseJson}")
#     print(f"A : {parseJson['a']}")

# def parseJsonArray():
#     myList = [{'a': 54, 'b': '21'}, {'b': 41, 'c': 87}]
#     jsonString = json.dumps(myList, indent=4)
#     print(f"JSON \n{jsonString}")
#     parseJson = json.loads(jsonString)
#     print(f"Parse ->>> {parseJson}")

#     for data in parseJson:
#         print(f"Data Parse : {data['b']}")

