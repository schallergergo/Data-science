course = {
    "name" : "Python programozás",
    "id"   : "VEMISAB132P",
    "students":[
    { "type": "full time",    "name": "John",    "neptun": "KEISAK", "points": [ 6, 9, 9, 9 ]},
    { "type": "correspondece","name": "Kevin",   "neptun": "ORJW45", "points": [ 3, 9, 5, 7 ]},
    { "type": "full time",    "name": "Bob",     "neptun": "FKSJDE", "points": [ 6, 9,10,10 ]},
    { "type": "correspondece","name": "Joe",     "neptun": "AE32ED", "points": [ 7, 6, 9, 6 ]},
    { "type": "full time",    "name": "Peter",   "neptun": "ZRT444", "points": [ 1, 9, 9, 3 ]},
    { "type": "correspondece","name": "Mary",    "neptun": "TREW34", "points": [ 6, 8, 2, 3 ]},
    { "type": "full time",    "name": "Robert",  "neptun": "EEIIOO", "points": [ 6, 4, 2, 4 ]},
    { "type": "full time",    "name": "James",   "neptun": "IORT32", "points": [ 8, 9, 2, 7 ]},
    { "type": "full time",    "name": "Jennifer","neptun": "S23432", "points": [ 1, 4, 4, 5 ]},
    { "type": "correspondece","name": "David",   "neptun": "NLDK55", "points": [ 6, 1, 8, 9 ]}
    ]
}


students = course["students"]

full_time = list(filter(lambda x : x["type"]=="full time",students))

#print(full_time)

def getResult(points):
    return sum(points)/sum([ 8, 8, 10, 10, 12 ])*100

for student in full_time:
    student ["result"] = getResult(student["points"])


ordered = sorted(full_time,key= lambda x : x["result"])

print("best: ",ordered[-1]["name"])
print("worst: ",ordered[0]["name"])

