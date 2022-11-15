import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
from datetime import datetime
if not firebase_admin._apps:
        cred = credentials.Certificate(
            r'C:\Users\Siddhant Bhatt\Downloads\rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
def test():
    users_ref=db.collection(u'temp').stream()
    for user_ref in users_ref:
        if(len(db.collection(u'temp').document(user_ref.id).get().to_dict()[u'meal_time'])>0):
            print(user_ref.id)
test()