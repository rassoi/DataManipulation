import datetime
import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

selectionDay = db.collection(u'days').document("selectionDay").get().to_dict()

print(selectionDay)
message = ['aam_panna-1', '4u2FyDU2pNfkOayQlUeVhISdbTJ3', 'Today']

dayIndex = selectionDay["day"].index(message[2])
date = selectionDay["date"][dayIndex]
print(dayIndex)
print(date)
recipe = db.collection(u'temp').document(message[1]+message[0]).get().to_dict()
print(recipe)
print(recipe["dates"])
