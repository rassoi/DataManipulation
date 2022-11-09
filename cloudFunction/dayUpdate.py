from cmath import e
import datetime
import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# import addMeals

# print("hi")
if not firebase_admin._apps:
    cred = credentials.Certificate(
            r'C:\Users\Siddhant Bhatt\Downloads\rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

today = datetime.datetime.today()+datetime.timedelta(days=1)

tomorrow = today+datetime.timedelta(days=2)

day3 = today+datetime.timedelta(days=3)

day4 = today+datetime.timedelta(days=4)

day5 = today+datetime.timedelta(days=5)

day = ["Today", "Tomorrow", day3.strftime(
    '%A'), day4.strftime('%A'), day5.strftime('%A')]
date = [today.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'),
        day3.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d')]
payload = {
    "day": day,
    "date": date,
    "type": "list"
}
selectionDay = db.collection(u'days').document("selectionDay").get().to_dict()
print("0. current Days ", selectionDay)
print("0.5. New Days ", payload)
difference = datetime.datetime.fromisoformat(
    payload["date"][0]) - datetime.datetime.fromisoformat(selectionDay["date"][0])
print("1.difference ", difference)
uid_list = ["qqgAmuXBvsRMXpQDUvxS0FraQiQH3", "qgAmuXBvsRMXpQDUvxS0FraQiQH3"]
# , "qgAmuXBvsRMXpQDUvxS0FraQiQH3"

def ingredRemover(ingred_id,meal):
  
    db.collection(u'meal_ingred').document(ingred_id).update({u'recipe_names': firestore.ArrayRemove([meal])})
    meal_length=len(db.collection(u'meal_ingred').document(ingred_id).get().to_dict()['recipe_names'])
    db.collection(u'meal_ingred').document(ingred_id).update({'meal_count':meal_length})
    if(meal_length==0):
        db.collection(u'meal_ingred').document(ingred_id).update({'status': 'unavailable'})
        db.collection(u'meal_ingred').document(ingred_id).update({'audit': 0})
    
    return 
def update_meal_time(day, action, meal_time_list,recipe_id,user_id,meal):
    new_list = meal_time_list[:]
    j = 0
    for i in range(len(meal_time_list)):
        # print("Checking :", meal_time_list[i])
        # print(day)
        if day in meal_time_list[i]:

            if action == "remove":
                new_list.remove(new_list[i-j])
                # db.collection(u'temp').document(recipe.id).update(
                #     {"meal_time": firestore.ArrayRemove([meal_time_list[i]])})
                j = j+1
                # print("removing : ", new_list[i-j])

            else:
                # print("****", new_list)
                # db.collection(u'temp').document(recipe.id).update(
                #     {"meal_time": firestore.ArrayRemove([meal_time_list[i]])})
                a = new_list[i-j].replace(day, action)
                # print("----", [a])
                # db.collection(u'temp').document(recipe.id).update(
                #     {"meal_time": firestore.ArrayUnion([a])})
    if(len(new_list)==0):
        ingreds= db.collection(u'temp').document(recipe_id).get().to_dict()['ingred_names']
        ingreds_list=ingreds.split('*')
        for ingred in ingreds_list:
            ingred_id=ingred.split('+')
            if(len(ingred)>1):
                ingredRemover(user_id+ingred_id[1],meal)

    return new_list


recipes = db.collection(u'temp').stream()


if (difference.days<= 3):

    print("2.difference.days ", difference.days)
    new_list = []
    newDayList = selectionDay["day"][difference.days:]
    deleteDayList = selectionDay["day"][:difference.days]
    print("********************", newDayList)

    print("3.deleteDayList ", deleteDayList)

    for recipe in recipes:
        recipe_ref = db.collection(u'temp').document(recipe.id).get().to_dict()
        # print("--------------------------------------------", recipe_ref)
        # to copy value not reference

        meal_time_list = recipe_ref["meal_time"][:]
        if(len(meal_time_list)==0):
            continue
        meal=recipe_ref["name"]
        user_id=recipe_ref["uid"]
        print(f'{meal}-->{meal_time_list}-->{user_id}')

        for item in deleteDayList:
            meal_time_list = update_meal_time(item, "remove", meal_time_list,recipe.id,user_id,meal)
            # print("removing for item", item)

        print(meal_time_list)
        print(newDayList[0], "Today")
        if(len(meal_time_list)==0):
            continue
        meal_time_list = update_meal_time(
            newDayList[0], "Today", meal_time_list,recipe.id,user_id,meal)
        print(newDayList[1], "Tomorrow")
        if(len(meal_time_list)==0):
            continue
        meal_time_list = update_meal_time(
            newDayList[1], "Tomorrow", meal_time_list,recipe.id,user_id,meal)
        # print(meal_time_list)
        # db.collection(u'temp').document(recipe.id).update(
        #     {"meal_time": meal_time_list})
    # db.collection(u'days').document("selectionDay").set(payload)
    # for uid in uid_list:
    #
    # addMeals.addMeals(day4.strftime('%Y-%m-%d'), uid)
else:
    # print("fuck")
    for recipe in recipes:
        recipe_ref = db.collection(u'temp').document(recipe.id).get().to_dict()
        # for item in recipe_ref["meal_time"]:
        #     db.collection(u'temp').document(recipe.id).update(
        #         {"meal_time": firestore.ArrayRemove([item])})
    # db.collection(u'days').document("selectionDay").delete()
    # db.collection(u'days').document("selectionDay").set(payload)
    # for uid in uid_list:
    # addMeals.addMeals(today.strftime('%Y-%m-%d'), uid)
    # addMeals.addMeals(tomorrow.strftime('%Y-%m-%d'), uid)
    # addMeals.addMeals(day3.strftime('%Y-%m-%d'), uid)
    # addMeals.addMeals(day4.strftime('%Y-%m-%d'), uid)

    # to horizontally ddeploy for all UIDS,addd for loop of UIDs to each addMeals statements
