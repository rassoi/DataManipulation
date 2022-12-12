import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import datetime
from chooseMeal import lunch, brakefast, dinner
if not firebase_admin._apps:
    cred = credentials.Certificate(
        r'abc.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def getMeals(text):
        
    print(text)
    def addIngrediants(mealId, uid, Day, mealtime):
        doc_ref = db.collection(u'temp').document(uid+mealId).get()
        if doc_ref.exists:
            print("hi")
            meal_name = doc_ref.to_dict()['name']
            meal_entry = meal_name+' : '+Day+' : ' + mealtime + ' + '+mealId
            ingreds = doc_ref.to_dict()['ingred_names']
            ingreds_list = ingreds.split('*')
            for ingred in ingreds_list:
                ingred_id = ingred.split('+')
                print(ingred_id)
                if(len(ingred_id) > 1):
                    db.collection(u"meal_ingred").document(uid+ingred_id[1]).update(
                        {u"recipe_names": firestore.ArrayUnion([meal_entry])}

                    )
                    print(meal_entry)
                    meal_length = len(db.collection(u'meal_ingred').document(
                        uid+ingred_id[1]).get().to_dict()['recipe_names'])
                    db.collection(u"meal_ingred").document(uid+ingred_id[1]).update(
                        {u'meal_count': meal_length}
                    )
        else:
            print("document not found")

        return

    def scheduleMeal(mealId, Day, mealTime, uid):

        # meal_cnt=db.collection(u'meal_ingred').document(uid+mealId).get(
        #     {u"meal_time": firestore.ArrayUnion([Day+mealTime])})

        # meal_cnt=meal_cnt+1
        # db.collection(u'temp').document(uid+mealId).update(
        #     {u"meal_time": meal_cnt})
        db.collection(u'temp').document(uid+mealId).update(
            {u"meal_time": firestore.ArrayUnion([Day+mealTime])})

        #print(mealId, Day, mealTime)
        addIngrediants(mealId, uid, Day, mealTime)
        # print("yoyo\n")

    def mealScheduledOrNot(day, uids):
        flag = 0
        docs = db.collection(u'temp').where(u'uid', u'==', uids).stream()
        for doc in docs:
            # print("hi")
            # print(doc.id)
            doc_ref = db.collection(u'temp').document(
                doc.id).get().to_dict()
            # print(doc_ref)
            for meal_time in doc_ref["meal_time"]:
                if day in meal_time:
                    flag = 1
        return flag

    today_date = datetime.datetime.today()

    tomorrow_date = today_date+datetime.timedelta(days=1)

    date3 = today_date+datetime.timedelta(days=2)

    date4 = today_date+datetime.timedelta(days=3)
    date5 = today_date+datetime.timedelta(days=4)
    today = today_date.strftime('%A')
    tomorrow = tomorrow_date.strftime('%A')
    # day2 = "tommorow"z
    day3 = date3.strftime('%A')
    day4 = date4.strftime('%A')
    day5 = date5.strftime('%A')

    uid = ["qnxzsG184Gfp17RDnvGdAg6DFu23", "qgAmuXBvsRMXpQDUvxS0FraQiQH3"]
    # recipes = db.collection(u'temp').stream()

    days = ["", "Today", "Tomorrow", day3, day4, day5]
    print(days)

    def setMeals(uids, day):
        Lunch = lunch()
        Dinner = dinner()
        Brakefast = brakefast()

        if len(Lunch) == 4:
            while Lunch[1] != Dinner[1]:
                Dinner = dinner()
        else:
            while len(Dinner) != 3:
                Dinner = dinner()
        # day4

        print(Brakefast)
        for bf in Brakefast:
            # print(bf, day4, "Brakefast", uids)
            scheduleMeal(bf, day, "Brakefast", uids)

        print(Lunch)
        for Lunch1 in Lunch:
            # print(Lunch, day4, "Lunch", uids)
            scheduleMeal(Lunch1, day, "Lunch", uids)

        print(Dinner)
        for Dinner1 in Dinner:
            # print(Dinner1, day4, "Dinner", uids)
            scheduleMeal(Dinner1, day, "Dinner", uids)

        # day3
        # Lunch = lunch()
        # Dinner = dinner()
        # Brakefast = brakefast()

        # if len(Lunch) == 4:
        #     while Lunch[1] != Dinner[1]:
        #         Dinner = dinner()
        # else:
        #     while len(Dinner) != 3:
        #         Dinner = dinner()

        # print(Brakefast)
        # for bf in Brakefast:
        #     print(bf, day3, "Brakefast", uids)
        #     scheduleMeal(bf, day3, "Brakefast", uids)

        # print(Lunch)
        # for Lunch1 in Lunch:
        #     print(Lunch1, day3, "Lunch", uids)
        #     scheduleMeal(Lunch1, day3, "Lunch", uids)

        # print(Dinner)
        # for Dinner1 in Dinner:
        #     print(Dinner1, day3, "Dinner", uids)
        #     scheduleMeal(Dinner1, day3, "Dinner", uids)
    flag = 0
    for uids in uid:
        print("starting for ::::::::::::::::::::::::::::::::::::::::::::::", uids)

        flag = 0
        # day = "Tommrow"
        print("hi")

        # print(day)
        flagDay5 = mealScheduledOrNot(days[5], uids)
        flagDay4 = mealScheduledOrNot(days[4], uids)
        flagDay3 = mealScheduledOrNot(days[3], uids)
        flagDay2 = mealScheduledOrNot(days[2], uids)
        flagDay1 = mealScheduledOrNot(days[1], uids)

        print(flagDay3, flagDay2, flagDay1)
        if not(flagDay2 or flagDay3 or flagDay1):
            setMeals(uids, days[3])
            setMeals(uids, days[2])
            setMeals(uids, days[1])
            flag = 1
        print(flag, flagDay5, flagDay4, flagDay3)
        if not(flag or flagDay5 or flagDay4 or flagDay3):
            setMeals(uids, days[5])
            setMeals(uids, days[4])
            setMeals(uids, days[3])
