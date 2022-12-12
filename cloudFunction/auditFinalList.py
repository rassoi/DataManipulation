

uid = "W8OFHeLYz0fXWWrXCdSt1uYo8ll2"

# clear


def generateBuyList(uid):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            r'/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    del_ingredients = db.collection(u'ingredBuy').where(
        u'uid', u'==', uid).stream()

    for item in del_ingredients:
        db.collection(u'ingredBuy').document(item.id).delete()

    # add
    ingredients = db.collection(u'meal_ingred').where(
        u'user_uid', u'==', uid).where(u'audit', u'==', 1).where(u'status', u'==', u'unavailable').stream()
    print("hi")
    for item in ingredients:
        docid = item.id
        doc_ref = db.collection(u'meal_ingred').document(
            item.id).get().to_dict()
        payload = {
            "name": doc_ref["english"],
            "img": doc_ref["img"],
            "recipe_names": doc_ref["recipe_names"],
            "price": doc_ref["price"],
            "desc": doc_ref["desc"],
            "parishiblity": doc_ref["parishiblity"],
            "uid": uid,
            "buingStatus": False,
        }

        db.collection(u'ingredBuy').document(docid).set(payload)


generateBuyList(uid)
