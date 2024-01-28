export = {
 "users": [
 { "_id" : "4ke83hsejs", "name" : "John", "role" : "developer"},
 { "_id" : "34rkmlqek2", "name" : "Kevin", "role" : "developer"},
 { "_id" : "83i2kkwwj3", "name" : "Joe", "role" : "developer"},
 { "_id" : "12kw4jwmcq", "name" : "Bob", "role" : "developer"},
 { "_id" : "4i5ii32313", "name" : "Robert", "role" : "developer"},
 { "_id" : "lkr3jwl4k5", "name" : "Mary", "role" : "manager"},

 ],
 "sprints": [
 { "_id": "2",
 "tasks":[
 { "_id" : "T0005", "storypoint" : 60, "task" : "Search",
 "hours": [ ("4ke83hsejs", 23), ("83i2kkwwj3", 15), ("4i5ii32313", 11)]},
 { "_id" : "T0006", "storypoint" : 20, "task" : "Filter",
 "hours": [ ("4ke83hsejs", 17), ("4i5ii32313", 12)]},
 { "_id" : "T0007", "storypoint" : 40, "task" : "List items",
 "hours": [ ("4i5ii32313", 3)]},
 ]
 },{ "_id": "3",
 "tasks":[ { "_id" : "T008", "storypoint" : 25, "task" : "Basket",
 "hours": [ ("4ke83hsejs", 6), ("83i2kkwwj3", 15), ("4i5ii32313", 23)]},
 { "_id" : "T0009", "storypoint" : 20, "task" : "Subscription",
 "hours": [ ("4ke83hsejs", 3), ("83i2kkwwj3", 24), ("4i5ii32313", 23)]},
 { "_id" : "T0010", "storypoint" : 35, "task" : "Order",
 "hours": [ ("83i2kkwwj3", 13), ("4i5ii32313", 5)]}
 ]
 },{ "_id": "1",
 "tasks":[ { "_id" : "T0001", "storypoint" : 50, "task" : "Login",
 "hours": [ ("4ke83hsejs", 13), ("83i2kkwwj3", 5), ("4i5ii32313", 11)]},
 { "_id" : "T0002", "storypoint" : 20, "task" : "Registration",
 "hours": [ ("4ke83hsejs", 28), ("4i5ii32313", 12)]},
 { "_id" : "T0003", "storypoint" : 30, "task" : "Menu",
 "hours": [ ("83i2kkwwj3", 7), ("4i5ii32313", 5)]},
 { "_id" : "T0004", "storypoint" : 40, "task" : "Design",
 "hours": [ ("4ke83hsejs", 17)]}
 ]
 },
 ]

} 

name="John"
#name = input("Name of the user:")

def getUserID(name):
    for user in export["users"]:
        if user["name"]==name:
            return user["_id"]
    print( "User not in db!")
    return None

userID = getUserID(name)
if userID == None:
    input("...")
    exit()
print(userID)

sprints = export["sprints"]
for sprint in sprints:
    for task in sprint["tasks"]:
        for hour in task["hours"]:
            if  userID in hour:
                print( task["task"])


taskSet = set()
for sprint in sprints:
    for task in sprint["tasks"]:
        for hour in task["hours"]:
            if  userID in hour:
                taskSet.add(task["task"])

print(taskSet)


def getTaskHours(taskDict):
    total = 0
    for task in taskDict["hours"]:
        print(task[1])
        total += task[1]
    taskDict["sumHours"] = total
    return taskDict["storypoint"]





def getSprintHours(sprintDict):
    total = 0
    for tasks in sprintDict["tasks"]:
            getTaskHours(tasks)
            total += tasks["sumHours"]
    return total

for sprint in export["sprints"]:
    sprint["sumHours"] = getSprintHours(sprint)




sprints = export["sprints"]
for sprint in sprints:
   print(list(filter(lambda x : x["storypoint"] > 40,sprint["tasks"])))

print("ORDERED")
for sprint in sprints:
    sprint["tasks"] = sorted(sprint["tasks"], key = lambda x : x["storypoint"])
    print(sprint["tasks"][-1])

print("\nex.:d1\n")



for sprint in export["sprints"]:
    maxPoint=maxPlace=0
    for task in sprint["tasks"]:
        temp = task["storypoint"]/task["sumHours"]
        if temp>maxPoint:
            maxPoint=temp
            maxPlace=task["task"]

    print(sprint["_id"],maxPlace, maxPoint)


print("\nex.:d2\n")

def getSumStoryPoint(sprint):
    total = 0
    for task in sprint["tasks"]:
        total += task["storypoint"]
    return total

def getDevelopers(sprint):
    developers = set()
    for task in sprint["tasks"]:
        for hour in task["hours"]:
            developers.add(hour[0])
    return list(developers)


for sprint in export["sprints"]:
    developers = getDevelopers(sprint)
    sumStoryPoint = getSumStoryPoint(sprint)
    dictOut = {}
    dictOut["sprintID"]=sprint["_id"]
    dictOut["sumStoryPoint"]=sumStoryPoint
    dictOut["developers"]=developers
    print(dictOut)
