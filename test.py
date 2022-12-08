from pymongo import MongoClient

client = MongoClient('mongodb://localhost')

db = client.music

result = db.rock.insert_one(
    {'band': 'Cream', 'album': 'Goodbye', 'year': 1969})
print(result)

documents = db.rock.find({'band': 'Cream'})

for document in documents:
    print(document)

docs = db.rock.update_one({'album': 'Fresh Cream'}, {'$set': {'year': 1970}})

delete_query = db.rock.delete_one({'album': 'Goodbye'})
