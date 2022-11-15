import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#import random
#import datetime
#from chooseMeal import lunch, brakefast, dinner

def ingredRemover2(ingred_id,meal):
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            r'C:\Users\Siddhant Bhatt\Downloads\rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    #doc_ref=db.collection(u'recipes').document(mealId).get()

  
    db.collection(u'meal_ingred').document(ingred_id).update({u'recipe_names': firestore.ArrayRemove([meal])})
    meal_length=len(db.collection(u'meal_ingred').document(ingred_id).get().to_dict()['recipe_names'])
    db.collection(u'meal_ingred').document(ingred_id).update({'meal_count':meal_length})
    if(meal_length==0):
        db.collection(u'meal_ingred').document(ingred_id).update({'status': 'unavailable'})
        db.collection(u'meal_ingred').document(ingred_id).update({'audit': 0})
    
    return 

#ingredRemover('Gw6DP7h1xnN0h4IH5sAI7kxOT0K3rice')