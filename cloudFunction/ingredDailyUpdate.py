import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime
import random


if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def ingredUpdate():

    mealIngreds = db.collection(u'meal_ingred').stream()

    today = datetime.datetime.today()

    tomorrow = today+datetime.timedelta(days=1)

    day3 = today+datetime.timedelta(days=2)

    day4 = today+datetime.timedelta(days=3)

    day5 = today+datetime.timedelta(days=4)

    day = ["Today", "Tomorrow", day3.strftime(
        '%A'), day4.strftime('%A'), day5.strftime('%A')]
    date = [today.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'),
            day3.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d')]
    payload = {
        "day": day,
        "date": date,
        "type": "list"
    }

    selectionDay = db.collection(u'days').document(
        "selectionDay").get().to_dict()
    print(selectionDay)
    difference = datetime.datetime.fromisoformat(
        payload["date"][0]) - datetime.datetime.fromisoformat(selectionDay["date"][0])
    newDayList = selectionDay["day"][difference.days:]
    print(newDayList)

    for ingred in mealIngreds:

        ingredDetails = db.collection(
            u'meal_ingred').document(ingred.id).get().to_dict()
        newRecipeList = []
        # recipeList = ingredDetails["recipe_names"][:]
        for item in ingredDetails["recipe_names"]:
            if "Today" in item:
                print("today item", item, ingred.id)

                db.collection(u'meal_ingred').document(ingred.id).update(
                    {"recipe_names": firestore.ArrayRemove([item])})
            elif newDayList[0] in item:
                # remove
                print("tommrow item", item)
                db.collection(u'meal_ingred').document(ingred.id).update(
                    {"recipe_names": firestore.ArrayRemove([item])})
                print(newDayList[0])
                item = item.replace(newDayList[0], "Today")
                db.collection(u"meal_ingred").document(ingred.id).update(
                    {u"recipe_names": firestore.ArrayUnion([item])})
                # add
            elif newDayList[1] in item:
                print("others item", item)
                # remove
                db.collection(u'meal_ingred').document(ingred.id).update(
                    {"recipe_names": firestore.ArrayRemove([item])})
                item = item.replace(newDayList[1], newDayList[0])
                db.collection(u"meal_ingred").document(ingred.id).update(
                    {u"recipe_names": firestore.ArrayUnion([item])})

                # add
        recipeLen = len(db.collection(u'meal_ingred').document(
            ingred.id).get().to_dict()["recipe_names"])

        db.collection(u'meal_ingred').document(
            ingred.id).update({u'meal_count': recipeLen, u'status': 'unavailable', u'audit': 0})
