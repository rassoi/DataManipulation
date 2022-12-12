def updateDay():
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

    today = datetime.datetime.today()

    tomorrow = today+datetime.timedelta(days=1)

    day3 = today+datetime.timedelta(days=2)

    day4 = today+datetime.timedelta(days=3)

    day5 = today+datetime.timedelta(days=4)

    day = ["Today", "Tomorrow", day3.strftime(
        '%A'), day4.strftime('%A'), day5.strftime('%A')]
    date = [today.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'),
            day3.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d'), day4.strftime('%Y-%m-%d')]
    payload = {
        "day": day,
        "date": date,
        "type": "list"
    }
    selectionDay = db.collection(u'days').document(
        "selectionDay").get().to_dict()
    print("0. current Days ", selectionDay)
    print("0.5. New Days ", payload)
    difference = datetime.datetime.fromisoformat(
        payload["date"][0]) - datetime.datetime.fromisoformat(selectionDay["date"][0])
    print("1.difference ", difference)
    # , "qgAmuXBvsRMXpQDUvxS0FraQiQH3"
    uid_list = ["qnxzsG184Gfp17RDnvGdAg6DFu23"]
    # , "qgAmuXBvsRMXpQDUvxS0FraQiQH3"

    def ingredRemover(ingred_id, meal, day, meal_time, recipe_id):

        meal_entry = meal+' : '+day+' : ' + meal_time + ' + '+recipe_id
        batch = db.batch()
        ingred_ref = db.collection(u'meal_ingred').document(ingred_id)
        batch.update(
            ingred_ref, {u'recipe_names': firestore.ArrayRemove([meal_entry])})
        batch.commit()
        meal_length_for_ingred = len(db.collection(u'meal_ingred').document(
            ingred_id).get().to_dict()['recipe_names'])
        batch = db.batch()
        batch.update(ingred_ref, {u'meal_count': meal_length_for_ingred})
        if(meal_length_for_ingred == 0):
            batch.update(ingred_ref, {u'status': 'unavailable'})
            batch.update(ingred_ref, {u'audit': '0'})
        batch.commit()

        return

    def update_meal_time(day, action, meal_time_list, recipe_id, user_id, meal):
        new_list = meal_time_list[:]
        j = 0
        for i in range(len(meal_time_list)):
            # print("Checking :", meal_time_list[i])
            # print(day)
            if day in meal_time_list[i]:

                if action == "remove":
                    new_list.remove(new_list[i-j])
                    db.collection(u'temp').document(recipe.id).update(
                        {"meal_time": firestore.ArrayRemove([meal_time_list[i]])})
                    j = j+1
                    # print("removing : ", new_list[i-j])

                    #meal_entry=meal_name+' : '+Day+' : '+ mealtime + ' + '+mealId
                    #     {"meal_time": firestore.ArrayUnion([a])})
                    ingreds = db.collection(u'temp').document(
                        recipe_id).get().to_dict()['ingred_names']
                    ingreds_list = ingreds.split('*')
                    for ingred in ingreds_list:
                        ingred_id = ingred.split('+')
                        if(len(ingred) > 1):
                            pass
                            # ingredRemover(
                            #     user_id+ingred_id[1], meal, day, meal_time_list[i], recipe_id)
                else:
                    # print("****", new_list)
                    db.collection(u'temp').document(recipe.id).update(
                        {"meal_time": firestore.ArrayRemove([meal_time_list[i]])})
                    a = new_list[i-j].replace(day, action)
                    # print("----", [a])
                    db.collection(u'temp').document(recipe.id).update(
                        {"meal_time": firestore.ArrayUnion([a])})
        if(len(new_list) == 0):
            ingreds = db.collection(u'temp').document(
                recipe_id).get().to_dict()['ingred_names']
            ingreds_list = ingreds.split('*')
            for ingred in ingreds_list:
                ingred_id = ingred.split('+')
                if(len(ingred) > 1):
                    # ingredRemover(user_id+ingred_id[1], meal)
                    pass

        return new_list

    if (difference.days <= 3):

        print("2.difference.days ", difference.days)
        new_list = []
        newDayList = selectionDay["day"][difference.days:]
        deleteDayList = selectionDay["day"][:difference.days]
        print("********************", newDayList)

        print("3.deleteDayList ", deleteDayList)

        recipes = db.collection(u'temp').stream()

        for recipe in recipes:
            recipe_ref = db.collection(u'temp').document(
                recipe.id).get().to_dict()
            # print("--------------------------------------------", recipe_ref)
            # to copy value not reference

            meal_time_list = recipe_ref["meal_time"][:]
            if(len(meal_time_list) == 0):
                continue
            meal = recipe_ref["name"]
            user_id = recipe_ref["uid"]
            print(f'{meal}-->{meal_time_list}-->{user_id}')

            for item in deleteDayList:
                meal_time_list = update_meal_time(
                    item, "remove", meal_time_list, recipe.id, user_id, meal)
                # print("removing for item", item)

            print(meal_time_list)
            print(newDayList[0], "Today")
            if(len(meal_time_list) == 0):
                continue
            meal_time_list = update_meal_time(
                newDayList[0], "Today", meal_time_list, recipe.id, user_id, meal)
            print(newDayList[1], "Tomorrow")
            if(len(meal_time_list) == 0):
                continue
            meal_time_list = update_meal_time(
                newDayList[1], "Tomorrow", meal_time_list, recipe.id, user_id, meal)
            # print(meal_time_list)
            # db.collection(u'temp').document(recipe.id).update(
            #     {"meal_time": meal_time_list})

        mealIngreds = db.collection(u'meal_ingred').stream()

        for ingred in mealIngreds:

            ingredDetails = db.collection(
                u'meal_ingred').document(ingred.id).get().to_dict()
            newRecipeList = []
            # recipeList = ingredDetails["recipe_names"][:]
            for item in ingredDetails["recipe_names"]:
                if "Today" in item:
                    print("today item", item, ingred.id)

                    db.collection(u'meal_ingred').document(ingred.id).update(
                        {"recipe_names": firestore.ArrayRemove([item])})
                elif newDayList[0] in item:
                    # remove
                    print("tommrow item", item)
                    db.collection(u'meal_ingred').document(ingred.id).update(
                        {"recipe_names": firestore.ArrayRemove([item])})
                    print(newDayList[0])
                    item = item.replace(newDayList[0], "Today")
                    db.collection(u"meal_ingred").document(ingred.id).update(
                        {u"recipe_names": firestore.ArrayUnion([item])})
                    # add
                elif newDayList[1] in item:
                    print("others item", item)
                    # remove
                    db.collection(u'meal_ingred').document(ingred.id).update(
                        {"recipe_names": firestore.ArrayRemove([item])})
                    item = item.replace(newDayList[1], newDayList[0])
                    db.collection(u"meal_ingred").document(ingred.id).update(
                        {u"recipe_names": firestore.ArrayUnion([item])})

                    # add
            recipeLen = len(db.collection(u'meal_ingred').document(
                ingred.id).get().to_dict()["recipe_names"])

            db.collection(u'meal_ingred').document(
                ingred.id).update({u'meal_count': recipeLen, u'status': 'unavailable', u'audit': 0})

        db.collection(u'days').document("selectionDay").set(payload)


updateDay()
