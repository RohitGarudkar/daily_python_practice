info = {
   "name" : "Rohit",
   "age" : 21,
   "is_adult" : True,
   "topic" : ("dict","set"),
   "subject" : ["python","C","java"],
}
info["surname"] = "garudkar"

     #nested dictionary

dictionary = {
    "name" : "Rohit",
    "score" : {
        "c":95,
        "java": 99,
        "python" : 98
    }
}
print(dictionary["score"]["python"])

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("name"))

# print(len(list(info.keys())))

info.update({"city" : "chalisgaon"})
print(info)
