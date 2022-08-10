import pymongo
client = pymongo.MongoClient("mongodb+srv://sairaj:sairaj55@cluster0.spixunq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'sairaj',
    'contact': '12345',
     'surname': 'waykool'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)