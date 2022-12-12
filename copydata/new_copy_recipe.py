def hello_firestore():
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # resource_string = context.resource
    # print out the resource string that triggered the function
    # print(f"Function triggered by change to: {resource_string}.")
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    if not firebase_admin._apps:
        cred = credentials.Certificate(
            '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
        default_app = firebase_admin.initialize_app(cred, name="new2")

    db = firestore.client(default_app)

    uid = "W8OFHeLYz0fXWWrXCdSt1uYo8ll2"

    def populateData(uid):
        user_id_list = [uid]

        for user_id in user_id_list:
            recipes = db.collection(u'recipes_temp').stream()
            print(user_id)
            meal_id_list = []
            for i, doc in enumerate(recipes):
                meal_id_list.append(doc.id)
                doc_ref = db.collection(u'recipes_temp').document(
                    doc.id).get().to_dict()

                if doc_ref["status"] == "Published":
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
                            ingred_ref["hindi"]+"+" + \
                            ingred_ref["img"]+"*"+ingreds
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
                        "status": "Published",
                        "counter": 0,
                        "fav": False,
                        "which_meal": [],
                        "dates": [],
                        "longPreperation": 0,
                        "veg": doc_ref["veg"]

                    }

                    if db.collection(u'temp').document(user_id+doc.id).get().exists:
                        print("exists")
                        pass
                    else:

                        print(user_id+doc.id)
                        db.collection(u'temp').document(
                            user_id+doc.id).set(recipe_payload)

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
                # print(inged_name)
                try:
                    parishiblity = doc_ref["parishablity"]

                except:
                    print(inged_name)

                ingred_payload = {
                    u'inged_id': inged_id,
                    u'english': inged_name,
                    u'hindi': inged_name_hindi,
                    u'img': inged_img,
                    u'recipe_names': [],
                    u'user_uid': user_id,
                    u"status": "unavailable",
                    u"meal_count": 0,
                    u"audit": 0,
                    u"parishiblity": parishiblity,
                    u"price": 0,
                    u"desc": "",
                }

                doc_name = user_id+inged_id
                db.collection(u'meal_ingred').document(
                    doc_name).set(ingred_payload)
    populateData(uid)


hello_firestore()
