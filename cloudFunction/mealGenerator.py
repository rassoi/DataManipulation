import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import datetime
from chooseMeal import lunch, brakefast, dinner


def get_meals():
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    def scheduleMeal(mealId, Day, mealTime, uid):

        db.collection(u'temp').document(uid+mealId).update(
            {u"meal_time": firestore.ArrayUnion([Day+mealTime])})

        print(mealId, Day, mealTime)

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
    today = today_date.strftime('%A')
    tomorrow = tomorrow_date.strftime('%A')
    day3 = date3.strftime('%A')
    day4 = date4.strftime('%A')

    uid = ["qnxzsG184Gfp17RDnvGdAg6DFu23", "qgAmuXBvsRMXpQDUvxS0FraQiQH3"]
    # recipes = db.collection(u'temp').stream()

    days = [day4, day3, "Tomorrow", "Today"]
    print(days)

    for uids in uid:
        print("starting for ::::::::::::::::::::::::::::::::::::::::::::::", uids)

        flag = 0
        # day = "Tommrow"
        print("hi")

        # print(day)
        flagDay4 = mealScheduledOrNot(days[0], uids)
        flagDay3 = mealScheduledOrNot(days[1], uids)
        flagDay2 = mealScheduledOrNot(days[2], uids)
        flagDay1 = mealScheduledOrNot(days[3], uids)
        if flagDay3 == 0:
            if flagDay4 == 0:

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
                    scheduleMeal(bf, day4, "Brakefast", uids)

                print(Lunch)
                for Lunch1 in Lunch:
                    # print(Lunch, day4, "Lunch", uids)
                    scheduleMeal(Lunch1, day4, "Lunch", uids)

                print(Dinner)
                for Dinner1 in Dinner:
                    # print(Dinner1, day4, "Dinner", uids)
                    scheduleMeal(Dinner1, day4, "Dinner", uids)

                # day3
                Lunch = lunch()
                Dinner = dinner()
                Brakefast = brakefast()

                if len(Lunch) == 4:
                    while Lunch[1] != Dinner[1]:
                        Dinner = dinner()
                else:
                    while len(Dinner) != 3:
                        Dinner = dinner()

                print(Brakefast)
                for bf in Brakefast:
                    print(bf, day3, "Brakefast", uids)
                    scheduleMeal(bf, day3, "Brakefast", uids)

                print(Lunch)
                for Lunch1 in Lunch:
                    print(Lunch1, day3, "Lunch", uids)
                    scheduleMeal(Lunch1, day3, "Lunch", uids)

                print(Dinner)
                for Dinner1 in Dinner:
                    print(Dinner1, day3, "Dinner", uids)
                    scheduleMeal(Dinner1, day3, "Dinner", uids)

        if flagDay2 == 0:
            if flagDay1 == 0:

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
                    scheduleMeal(bf, "Tomorrow", "Brakefast", uids)

                print(Lunch)
                for Lunch1 in Lunch:
                    # print(Lunch, day4, "Lunch", uids)
                    scheduleMeal(Lunch1, "Tomorrow", "Lunch", uids)

                print(Dinner)
                for Dinner1 in Dinner:
                    # print(Dinner1, day4, "Dinner", uids)
                    scheduleMeal(Dinner1, "Tomorrow", "Dinner", uids)

                # day3
                Lunch = lunch()
                Dinner = dinner()
                Brakefast = brakefast()

                if len(Lunch) == 4:
                    while Lunch[1] != Dinner[1]:
                        Dinner = dinner()
                else:
                    while len(Dinner) != 3:
                        Dinner = dinner()

                print(Brakefast)
                for bf in Brakefast:
                    # print(bf, "Today", "Brakefast", uids)
                    scheduleMeal(bf, "Today", "Brakefast", uids)

                print(Lunch)
                for Lunch1 in Lunch:
                    # print(Lunch1, day3, "Lunch", uids)
                    scheduleMeal(Lunch1, "Today", "Lunch", uids)

                print(Dinner)
                for Dinner1 in Dinner:
                    # print(Dinner1, day3, "Dinner", uids)
                    scheduleMeal(Dinner1, "Today", "Dinner", uids)


get_meals()
