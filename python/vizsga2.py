li = [
{ "course": "VEMISAB132P", "name": "John", "neptun": "KEISAK",
"theory": [ 6, 9, 9, 9, 5 ], "practice" :[3,8,9,8]},
{ "course": "VEMISAB144A" , "name": "John", "neptun": "KEISAK",
"theory": [ 3, 2, 5, 7, 5 ], "practice" :[3,6,9,6] },
{ "course": "VEMISAB132P", "name": "Kevin", "neptun": "FKSJDE",
"theory": [ 6, 9,10,10, 4 ], "practice" :[9,7,9,8] },
{ "course": "VEMISAB144O", "name": "Kevin", "neptun": "FKSJDE",
"theory": [ 7, 2, 2, 6, 0 ], "practice" :[3,8,9,6], "result" : 43 },
{ "course": "VEMISAB144O", "name": "Bob", "neptun": "ZZRWD",
"theory": [ 1, 9, 9, 3, 3 ], "practice" :[9,6,9,8], "result" : 57 },
{ "course": "VEMISAB144A" , "name": "Joe", "neptun": "TTWQS",
"theory": [ 6, 6, 2, 3, 1 ], "practice" :[3,2,9,6] },
{ "course": "VEMISAB132P", "name": "Joe", "neptun": "TTWQS",
"theory": [ 6, 4, 2, 4, 5 ], "practice" :[3,8,5,8] },
{ "course": "VEMISAB144O", "name": "Peter", "neptun": "NVMCX",
"theory": [ ], "practice" :[] },
{ "course": "VEMISAB144A" , "name": "Bob", "neptun": "ZZRWD",
"theory": [ 1, 4, 4, 5, 8 ], "practice" :[3,8,7,9] },
{ "course": "VEMISAB132P", "name": "Peter", "neptun": "NVMCX",
"theory": [ 1, 1, 0, 0, 0 ], "practice" :[1,4,9,8] }
]


filtered = list(filter(lambda x : x["course"]=="VEMISAB132P" or x["course"]=="VEMISAB144A",li))



def calculate(a,b):
    return sum(a)+sum(b)

for item in filtered :
    item["result"] = calculate(item["theory"],item["practice"])


ordered = sorted( list( filter( lambda x :"result" in x,filtered)), key = lambda x : x["result"])
