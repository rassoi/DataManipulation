import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred, name="new2")

db = firestore.client(default_app)


# ,"qgAmuXBvsRMXpQDUvxS0FraQiQH3", "qnxzsG184Gfp17RDnvGdAg6DFu23"]
user_id_list = ["qgAmuXBvsRMXpQDUvxS0FraQiQH3"]

for user_id in user_id_list:
    ingredients = db.collection(u'ingredients').stream()
    print(user_id)
    meal_id_list = []
    for i, doc in enumerate(ingredients):

        doc_ref = db.collection(u'ingredients').document(
            doc.id).get().to_dict()
        inged_id = doc.id
        inged_name = doc_ref["english"]
        inged_name_hindi = doc_ref["hindi"]
        inged_img = doc_ref["img"]
        ingred_payload = {
            u'inged_id': inged_id,
            u'english': inged_name,
            u'hindi': inged_name_hindi,
            u'img': inged_img,
            u'recipe_names': [],
            u'user_uid': user_id,
            u"status": "unavailable",
            u"meal_count": 0,
            u"audit": 0
        }

        doc_name = user_id+inged_id
        db.collection(u'meal_ingred').document(
            doc_name).set(ingred_payload)
