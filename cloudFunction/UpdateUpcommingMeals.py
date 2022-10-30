
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

uid = "4u2FyDU2pNfkOayQlUeVhISdbTJ3"


# Today

def updateUpcommingMeals(uid, paher):
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):
        # print(recipeDoc.id)

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        # print(recipe["name"])
        print("TodayBrakefast")
        if "TodayBrakefast" in recipe["meal_time"]:

            if paher == 1 or paher == 2 or paher == 3:
                db.collection(u'temp').document(uid+recipeDoc.id).update(
                    {"meal_time": firestore.ArrayRemove(["TodayBrakefast"])})

            else:
                payload = {
                    "name": recipe["name"],
                    "image": recipe["image"],
                    "meal_time": "TodayBrakefast",
                    "sequence": 11,
                    "uid": uid
                }
                db.collection(u'upcommingmeals').document(
                    uid+recipeDoc.id+"11").set(payload)

    print("abc")
    recipes = db.collection(u'recipes').stream()
    print("abc")
    for i, recipeDoc in enumerate(recipes):
        print("TodayLunch")
        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TodayLunch" in recipe["meal_time"]:
            if paher == 2 or paher == 3:
                db.collection(u'temp').document(uid+recipeDoc.id).update(
                    {"meal_time": firestore.ArrayRemove(["TodayLunch"])})

            else:

                payload = {
                    "name": recipe["name"],
                    "image": recipe["image"],
                    "meal_time": "TodayLunch",
                    "sequence": 12,
                    "uid": uid
                }

                db.collection(u'upcommingmeals').document(
                    uid+recipeDoc.id+"12").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TodaySnacks" in recipe["meal_time"]:
            if paher == 3:
                db.collection(u'temp').document(uid+recipeDoc.id).update(
                    {"meal_time": firestore.ArrayRemove(["TodaySnacks"])})

            else:

                payload = {
                    "name": recipe["name"],
                    "image": recipe["image"],
                    "meal_time": "TodaySnacks",
                    "sequence": 13,
                    "uid": uid
                }

                db.collection(u'upcommingmeals').document(
                    uid+recipeDoc.id+"13").set(payload)
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TodayDinner" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": "TodayDinner",
                "sequence": 14,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"14").set(payload)

    # TOmorrow
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TomorrowBrakefast" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": "TomorrowBrakefast",
                "sequence": 21,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"21").set(payload)
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TomorrowLunch" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": "TomorrowLunch",
                "sequence": 22,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"22").set(payload)
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TomorrowSnacks" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": "TomorrowSnacks",
                "sequence": 23,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"23").set(payload)
    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if "TomorrowDinner" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": "TomorrowDinner",
                "sequence": 24,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"24").set(payload)

    today = datetime.datetime.today()

    tomorrow = today+datetime.timedelta(days=1)

    day3 = today+datetime.timedelta(days=2)

    day4 = today+datetime.timedelta(days=3)

    day5 = today+datetime.timedelta(days=4)
    day3Day = day3.strftime('%A')

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day3Day+"Brakefast" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day3Day+"Brakefast",
                "sequence": 31,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+day3Day+"31").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day3Day+"Lunch" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day3Day+"Lunch",
                "sequence": 32,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"32").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day3Day+"Snacks" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day3Day+"Snacks",
                "sequence": 33,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"33").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day3Day+"Dinner" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day3Day+"Dinner",
                "sequence": 34,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"34").set(payload)

    recipes = db.collection(u'recipes').stream()
    day4Day = day4.strftime('%A')
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day4Day+"Brakefast" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day4Day+"Brakefast",
                "sequence": 41,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+day4Day+"41").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day4Day+"Lunch" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day4Day+"Lunch",
                "sequence": 42,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"42").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day4Day+"Snacks" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day4Day+"Snacks",
                "sequence": 43,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"43").set(payload)

    recipes = db.collection(u'recipes').stream()
    for i, recipeDoc in enumerate(recipes):

        recipe = db.collection(u'temp').document(
            uid+recipeDoc.id).get().to_dict()
        if day4Day+"Dinner" in recipe["meal_time"]:

            payload = {
                "name": recipe["name"],
                "image": recipe["image"],
                "meal_time": day4Day+"Dinner",
                "sequence": 44,
                "uid": uid
            }

            db.collection(u'upcommingmeals').document(
                uid+recipeDoc.id+"44").set(payload)


paher = 2
updateUpcommingMeals(uid, paher)
