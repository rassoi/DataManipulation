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
        r'/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


current_date = datetime.datetime.today()
today = current_date+datetime.timedelta(days=-1)
tomorrow = current_date

day3 = current_date+datetime.timedelta(days=1)

day4 = current_date+datetime.timedelta(days=2)

day5 = current_date+datetime.timedelta(days=3)

day = ["Today", "Tomorrow", day3.strftime(
    '%A'), day4.strftime('%A'), day5.strftime('%A')]
date = [today.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'),
        day3.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d')]
payload = {
    "day": day,
    "date": date,
    "type": "list"
}
# print(payload)
db.collection(u'days').document("selectionDay").set(payload)
