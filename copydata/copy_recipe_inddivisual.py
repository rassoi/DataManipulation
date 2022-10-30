# from xml.dom.minidom import Document
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/food-a6f8e-firebase-adminsdk-rryaq-a64be88eaf.json')
    default_app = firebase_admin.initialize_app(cred)
    cred2 = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app2 = firebase_admin.initialize_app(cred2, name="new2")

db = firestore.client(default_app)
db2 = firestore.client(default_app2)
users = db2.collection(u'users').stream()

user_id = "kHTCMuY98CS8wPCOaSYOUxIjdjL2"

recipes = db.collection(u'recepies').stream()
for i, doc in enumerate(recipes):
    if i % 2 == 0:
        categoryName = ["Healthy", "Desi", "All"]
    if i % 3 == 0:
        categoryName = ["Healthy", "Summer", "All"]
    else:
        categoryName = ["Thali", "Summer", "All"]
    print(doc.id)
    a = f'{doc.id}'
    doc_ref = db.collection(u'recepies').document(doc.id).get().to_dict()
    name = doc_ref["name"]
    image = doc_ref["name"]
    ref = db2.collection('recipes').document(doc.id)
    # Creating ingred_names
    ingred_ref = db.collection(u'recepies').document(
        doc.id).collection(u'ingreds').stream()
    ingreds = ""
    for ingred_doc in ingred_ref:
        ingred_ref = db.collection(u'Ingridients').document(
            ingred_doc.id).get().to_dict()
        ingreds = ingred_ref["english"]+"+"+ingred_doc.id+"+" + \
            ingred_ref["hindi"]+"+"+ingred_ref["img"]+"*"+ingreds

    # Creating recipie's imagelink
    # https: // img.youtube.com/vi/Vmrppjpr_M4/0.jpg
    # https: // youtu.be/Vmrppjpr_M4

    a_split = doc_ref["yt"].split("/")
    img_link = "https://img.youtube.com/vi/"+a_split[-1]+"/0.jpg"
    # Creating namedAsArray
    name = doc_ref["name"]
    main_list = []

    name_split = name.split(" ")
    for word in name_split:
        print(word)
        j = ""
        for char in word.lower():
            j = j+char
            main_list.append(j)
    main_list.append(name)
    main_list.append(" ")
    main_list.append("")
    main_list_with_category = main_list
    for category in categoryName:

        main_list_with_category = main_list_with_category + \
            [category+x for x in main_list]

    recipe_payload = {
        "name": doc_ref["name"],
        "image": img_link,
        "name_hindi": doc_ref["name"],
        "categoryName": categoryName,
        "desc": doc_ref["desc"],
        "ingred_names": ingreds,
        "nameAsArray": main_list_with_category,
        "recipe_id": doc.id,
        "ref": ref,
        "youtube_link": doc_ref["yt"],
        "uid": user_id,
        "day": [],
        "meal_time": [],
        "status": "notLive",
        "counter": 1,
        "fav": False,
        "which_meal": [],
        "dates": []

    }
    # print(recipe_payload)

    db2.collection(u'temp').document(user_id+doc.id).set(recipe_payload)
    ingreds = db.collection(u'recepies').document(
        doc.id).collection(u'ingreds').stream()
    for ingredDoc in ingreds:
        ingredId = f'{ingredDoc.id}'
        ingred_payload = db.collection(
            u'Ingridients').document(ingredId).get().to_dict()

        db2.collection(u'temp').document(user_id+doc.id).collection(
            u'ingreds').document(ingredDoc.id).set(ingred_payload)
