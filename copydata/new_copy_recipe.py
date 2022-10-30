import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred, name="new2")

db = firestore.client(default_app)


# ,"qgAmuXBvsRMXpQDUvxS0FraQiQH3", "qnxzsG184Gfp17RDnvGdAg6DFu23"]
user_id_list = ["qgAmuXBvsRMXpQDUvxS0FraQiQH3", "qnxzsG184Gfp17RDnvGdAg6DFu23"]

for user_id in user_id_list:
    recipes = db.collection(u'recipes_temp').stream()
    print(user_id)
    meal_id_list = []
    for i, doc in enumerate(recipes):
        meal_id_list.append(doc.id)
        doc_ref = db.collection(u'recipes_temp').document(
            doc.id).get().to_dict()
        name = doc_ref["name"]
        image = doc_ref["image"]
        ref = db.collection('recipes_temp').document(doc.id)

        ingred_ref = db.collection(u'recipes_temp').document(
            doc.id).collection(u'ingreds').stream()

        ingreds = ""
        for ingred_doc in ingred_ref:
            ingred_ref = db.collection(u'recipes_temp').document(
                doc.id).collection(u'ingreds').document(
                ingred_doc.id).get().to_dict()
            ingreds = ingred_ref["english"]+"+"+ingred_doc.id+"+" + \
                ingred_ref["hindi"]+"+"+ingred_ref["img"]+"*"+ingreds
            # print(ingreds)
        categoryName = doc_ref["categoryName"]
        name = doc_ref["name"]
        main_list = []

        name_split = name.split(" ")
        for word in name_split:
            # print(word)
            j = ""
            for char in word.lower():
                j = j+char
                main_list.append(j)
        main_list.append(name)
        main_list.append(" ")
        main_list.append("")
        main_list_with_category = main_list
        # print(main_list_with_category)
        for category in categoryName:

            main_list_with_category = main_list_with_category + \
                [category+x for x in main_list]
        # print(main_list_with_category)
        recipe_payload = {
            "name": doc_ref["name"],
            "image": doc_ref["image"],
            "name_hindi": doc_ref["name_hindi"],
            "categoryName": categoryName,
            "ingred_names": ingreds,
            "nameAsArray": main_list_with_category,
            "recipe_id": doc.id,
            "ref": ref,
            "youtube_link": doc_ref["youtube_link"],
            "uid": user_id,
            "day": [],
            "meal_time": [],
            "status": "notLive",
            "counter": 0,
            "fav": False,
            "which_meal": [],
            "dates": [],
            "longPreperation": 0

        }

        if db.collection(u'temp').document(user_id+doc.id).get().exists:
            print("exists")
            pass
        else:

            print(user_id+doc.id)
            db.collection(u'temp').document(
                user_id+doc.id).set(recipe_payload)
