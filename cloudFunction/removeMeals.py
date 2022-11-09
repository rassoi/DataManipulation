import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#import random
#import datetime
#from chooseMeal import lunch, brakefast, dinner

def mealRemover():
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            r'C:\Users\Siddhant Bhatt\Downloads\rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    #doc_ref=db.collection(u'recipes').document(mealId).get()
    docs=db.collection("meal_ingred").stream()
    for doc in docs:
        if(doc.to_dict()['user_uid']=='Gw6DP7h1xnN0h4IH5sAI7kxOT0K3'):
            bla=db.collection(u'meal_ingred').document(doc.id).get().to_dict()
            print(doc.id)
            print(bla)
            #print(f'{doc.id}==>{doc.to_dict()}')
            # db.collection(u'meal_ingred').document(doc.id).update({'status': 'unavailable'})
            # db.collection(u'meal_ingred').document(doc.id).update({'meal_count': 0})
            # db.collection(u'meal_ingred').document(doc.id).update({'audit': 0})
            # db.collection(u'meal_ingred').document(doc.id).update({'recipe_names':[]})
            break
    return 

mealRemover()