
from cmath import e
import datetime
import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random


if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
ingreds = db.collection(u'meal_ingred').stream()

uid = "qnxzsG184Gfp17RDnvGdAg6DFu23"
unavailableCount = 0
availableCount = 0
for ingredDoc in ingreds:

    ingred = db.collection(u'meal_ingred').document(
        ingredDoc.id).get().to_dict()
    print(ingred)
    print(ingred["english"])
    if ingred["meal_count"] > 0:
        if ingred["status"] == "unavailable":
            unavailableCount = unavailableCount+1
        if ingred["status"] == "available":
            availableCount = availableCount+1
print(unavailableCount)
print(availableCount)
