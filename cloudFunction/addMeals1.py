# Input take date as input
# Get difference between mentioned date and current date
# add date and anddd day, in days collection

# Now take meal_id, run loop for brakefast, lunch, dinner

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


recipes = db.collection(u'recipes_temp').stream()
meals_list = []
for doc in recipes:
    meals_list.append(doc.id)

print(meals_list)


def addMeals(input_date, uid, meal_list):

    todayDate = datetime.datetime.today()
    todayDay = todayDate.strftime('%A')

    # input_date = "2022-06-28"
    mealDate = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    mealDay = mealDate.strftime('%A')

    # meal_list = ['achari_paneer', 'aloo palak ki sabzi', 'dabeli_sev', 'dhaba style baingan bharta', 'hariyali dum aloo',
    #              'khatte meethe aloo', 'peanut_butter_oats_idli', 'smoked_lemon_chiken', 'sprout_mung_salad', 'tamatar pyaz ki sabzi']

    b1 = random.randint(0, len(meal_list)-1)
    b1 = meal_list[b1]
    b2 = random.randint(0, len(meal_list)-1)
    print(b2)
    b2 = meal_list[b2]

    l1 = random.randint(0, len(meal_list)-1)
    l1 = meal_list[l1]
    l2 = random.randint(0, len(meal_list)-1)
    print(l2)
    l2 = meal_list[l2]

    s1 = random.randint(0, len(meal_list)-1)
    s1 = meal_list[s1]
    s2 = random.randint(0, len(meal_list)-1)
    s2 = meal_list[s2]

    d1 = random.randint(0, len(meal_list)-1)
    d1 = meal_list[d1]
    d2 = random.randint(0, len(meal_list)-1)
    d2 = meal_list[d2]

    def scheduleMeal(mealId, Day, mealTime, uid):

        db.collection(u'temp').document(uid+mealId).update(
            {u"meal_time": firestore.ArrayUnion([Day+mealTime])})

        print(mealId, Day, mealTime)

    difference = mealDate-todayDate
    if (difference.days == -1):
        # db.collection(u'days').document(u'selectionDay').update(
        #     {u"date": firestore.ArrayUnion([input_date])})
        # db.collection(u'days').document(u'selectionDay').update(
        #     {u"day": firestore.ArrayUnion(["Today"])})
        # scheduleMeal(mealId, Day, mealTime, uid)
        scheduleMeal(b1, "Today", "Brakefast", uid)
        scheduleMeal(b2, "Today", "Brakefast", uid)
        scheduleMeal(l1, "Today", "Lunch", uid)
        scheduleMeal(l2, "Today", "Lunch", uid)
        scheduleMeal(s1, "Today", "Snacks", uid)
        scheduleMeal(s2, "Today", "Snacks", uid)
        scheduleMeal(d1, "Today", "Dinner", uid)
        scheduleMeal(d2, "Today", "Dinner", uid)

    elif (difference.days == 0):
        # db.collection(u'days').document(u'selectionDay').update(
        # {u"date": firestore.ArrayUnion([input_date])})
        # db.collection(u'days').document(u'selectionDay').update(
        # {u"day": firestore.ArrayUnion(["Tomorrow"])})

        scheduleMeal(b1, "Tomorrow", "Brakefast", uid)
        scheduleMeal(b2, "Tomorrow", "Brakefast", uid)
        scheduleMeal(l1, "Tomorrow", "Lunch", uid)
        scheduleMeal(l2, "Tomorrow", "Lunch", uid)
        scheduleMeal(s1, "Tomorrow", "Snacks", uid)
        scheduleMeal(s2, "Tomorrow", "Snacks", uid)
        scheduleMeal(d1, "Tomorrow", "Dinner", uid)
        scheduleMeal(d2, "Tomorrow", "Dinner", uid)

    elif (difference.days > 0 and difference.days <= 2):
        # db.collection(u'days').document(u'selectionDay').update(
        # {u"date": firestore.ArrayUnion([input_date])})
        # db.collection(u'days').document(u'selectionDay').update(
        # {u"day": firestore.ArrayUnion([mealDay])})
        scheduleMeal(b1, mealDay, "Brakefast", uid)
        scheduleMeal(b2, mealDay, "Brakefast", uid)
        scheduleMeal(l1, mealDay, "Lunch", uid)
        scheduleMeal(l2, mealDay, "Lunch", uid)
        scheduleMeal(s1, mealDay, "Snacks", uid)
        scheduleMeal(s2, mealDay, "Snacks", uid)
        scheduleMeal(d1, mealDay, "Dinner", uid)
        scheduleMeal(d2, mealDay, "Dinner", uid)
    else:
        print("Meal cannot be planed for more than 3 days from today")
    # recipes = db.collection(u'recipes').stream()
    # recipe_list = []
    # for recipe in recipes:
    #     recipe_list.append(recipe.id)

    # print(recipe_list)]


today = datetime.datetime.today()

tomorrow = today+datetime.timedelta(days=1)

day3 = today+datetime.timedelta(days=2)

day4 = today+datetime.timedelta(days=3)

day5 = today+datetime.timedelta(days=4)

uid = "qnxzsG184Gfp17RDnvGdAg6DFu23"

# addMeals(day3.strftime('%Y-%m-%d'), uid, meals_list)
