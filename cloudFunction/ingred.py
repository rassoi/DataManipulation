

import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

c = "{'oldValue': {'createTime': '2022-08-07T08:59:59.083727Z', 'fields': {'categoryName': {'arrayValue': {'values': [{'stringValue': 'Healthy'}, {'stringValue': 'All'}]}}, 'counter': {'integerValue': '0'}, 'dates': {'arrayValue': {}}, 'day': {'arrayValue': {}}, 'fav': {'booleanValue': False}, 'image': {'stringValue': 'https://storage.googleapis.com/rassoi-767af.appspot.com/images/recipes/sprout_mung_salad.jpg'}, 'ingred_names': {'stringValue': 'Tomato+tomato+टमाटर+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/tomato.jpg*Spring Onion Leaves+spring_onion_leaves+प्याज के पत्ते+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/spring_onion_leaves.jpg*Salt+salt+ नमक+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/salt.jpg*pomegranate+pomegranate+अनार+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/pomegranate.jpg*Onion+onion+प्याज़+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/onion.jpg*Mung Beans+mung_beans+मूंग+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/mung_beans.jpg*Lemon+lemon+ नींबू+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/lemon.jpg*Cucumber+cucumber+ खीरा+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/cucumber.jpg*Capsicuum+capsicum+शिमला मिर्च+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/capsicum.jpg*Black Pepper Powder+black_pepper_powder+ काली मिर्च पाउडर+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/black_pepper_powder.jpg*'}, 'meal_time': {'arrayValue': {}}, 'name': {'stringValue': 'Mung Sprout Salad'}, 'nameAsArray': {'arrayValue': {'values': [{'stringValue': 'm'}, {'stringValue': 'mu'}, {'stringValue': 'mun'}, {'stringValue': 'mung'}, {'stringValue': 's'}, {'stringValue': 'sp'}, {'stringValue': 'spr'}, {'stringValue': 'spro'}, {'stringValue': 'sprou'}, {'stringValue': 'sprout'}, {'stringValue': 's'}, {'stringValue': 'sa'}, {'stringValue': 'sal'}, {'stringValue': 'sala'}, {'stringValue': 'salad'}, {'stringValue': 'Mung Sprout Salad'}, {'stringValue': ' '}, {'stringValue': ''}, {'stringValue': 'Healthym'}, {'stringValue': 'Healthymu'}, {'stringValue': 'Healthymun'}, {'stringValue': 'Healthymung'}, {'stringValue': 'Healthys'}, {'stringValue': 'Healthysp'}, {'stringValue': 'Healthyspr'}, {'stringValue': 'Healthyspro'}, {'stringValue': 'Healthysprou'}, {'stringValue': 'Healthysprout'}, {'stringValue': 'Healthys'}, {'stringValue': 'Healthysa'}, {'stringValue': 'Healthysal'}, {'stringValue': 'Healthysala'}, {'stringValue': 'Healthysalad'}, {'stringValue': 'HealthyMung Sprout Salad'}, {'stringValue': 'Healthy '}, {'stringValue': 'Healthy'}, {'stringValue': 'Allm'}, {'stringValue': 'Allmu'}, {'stringValue': 'Allmun'}, {'stringValue': 'Allmung'}, {'stringValue': 'Alls'}, {'stringValue': 'Allsp'}, {'stringValue': 'Allspr'}, {'stringValue': 'Allspro'}, {'stringValue': 'Allsprou'}, {'stringValue': 'Allsprout'}, {'stringValue': 'Alls'}, {'stringValue': 'Allsa'}, {'stringValue': 'Allsal'}, {'stringValue': 'Allsala'}, {'stringValue': 'Allsalad'}, {'stringValue': 'AllMung Sprout Salad'}, {'stringValue': 'All '}, {'stringValue': 'All'}]}}, 'name_hindi': {'stringValue': ' अंकुरित मूंग सलाद'}, 'recipe_id': {'stringValue': 'sprout_mung_salad'}, 'ref': {'referenceValue': 'projects/rassoi-767af/databases/(default)/documents/recipes_temp/sprout_mung_salad'}, 'status': {'stringValue': 'notLive'}, 'uid': {'stringValue': 'qnxzsG184Gfp17RDnvGdAg6DFu23'}, 'which_meal': {'arrayValue': {}}, 'youtube_link': {'stringValue': 'https://www.youtube.com/watch?v=u3dw0dooJP4'}}, 'name': 'projects/rassoi-767af/databases/(default)/documents/temp/qnxzsG184Gfp17RDnvGdAg6DFu23sprout_mung_salad', 'updateTime': '2022-09-18T16:59:06.821751Z'}, 'updateMask': {'fieldPaths': ['dates', 'counter', 'meal_time']}, 'value': {'createTime': '2022-08-07T08:59:59.083727Z', 'fields': {'categoryName': {'arrayValue': {'values': [{'stringValue': 'Healthy'}, {'stringValue': 'All'}]}}, 'counter': {'integerValue': '1'}, 'dates': {'arrayValue': {'values': [{'stringValue': '2022-09-18'}]}}, 'day': {'arrayValue': {}}, 'fav': {'booleanValue': False}, 'image': {'stringValue': 'https://storage.googleapis.com/rassoi-767af.appspot.com/images/recipes/sprout_mung_salad.jpg'}, 'ingred_names': {'stringValue': 'Tomato+tomato+टमाटर+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/tomato.jpg*Spring Onion Leaves+spring_onion_leaves+प्याज के पत्ते+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/spring_onion_leaves.jpg*Salt+salt+ नमक+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/salt.jpg*pomegranate+pomegranate+अनार+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/pomegranate.jpg*Onion+onion+प्याज़+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/onion.jpg*Mung Beans+mung_beans+मूंग+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/mung_beans.jpg*Lemon+lemon+ नींबू+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/lemon.jpg*Cucumber+cucumber+ खीरा+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/cucumber.jpg*Capsicuum+capsicum+शिमला मिर्च+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/capsicum.jpg*Black Pepper Powder+black_pepper_powder+ काली मिर्च पाउडर+https://storage.googleapis.com/rassoi-767af.appspot.com//images/ingredients/black_pepper_powder.jpg*'}, 'meal_time': {'arrayValue': {'values': [{'stringValue': 'TodayBrakefast'}]}}, 'name': {'stringValue': 'Mung Sprout Salad'}, 'nameAsArray': {'arrayValue': {'values': [{'stringValue': 'm'}, {'stringValue': 'mu'}, {'stringValue': 'mun'}, {'stringValue': 'mung'}, {'stringValue': 's'}, {'stringValue': 'sp'}, {'stringValue': 'spr'}, {'stringValue': 'spro'}, {'stringValue': 'sprou'}, {'stringValue': 'sprout'}, {'stringValue': 's'}, {'stringValue': 'sa'}, {'stringValue': 'sal'}, {'stringValue': 'sala'}, {'stringValue': 'salad'}, {'stringValue': 'Mung Sprout Salad'}, {'stringValue': ' '}, {'stringValue': ''}, {'stringValue': 'Healthym'}, {'stringValue': 'Healthymu'}, {'stringValue': 'Healthymun'}, {'stringValue': 'Healthymung'}, {'stringValue': 'Healthys'}, {'stringValue': 'Healthysp'}, {'stringValue': 'Healthyspr'}, {'stringValue': 'Healthyspro'}, {'stringValue': 'Healthysprou'}, {'stringValue': 'Healthysprout'}, {'stringValue': 'Healthys'}, {'stringValue': 'Healthysa'}, {'stringValue': 'Healthysal'}, {'stringValue': 'Healthysala'}, {'stringValue': 'Healthysalad'}, {'stringValue': 'HealthyMung Sprout Salad'}, {'stringValue': 'Healthy '}, {'stringValue': 'Healthy'}, {'stringValue': 'Allm'}, {'stringValue': 'Allmu'}, {'stringValue': 'Allmun'}, {'stringValue': 'Allmung'}, {'stringValue': 'Alls'}, {'stringValue': 'Allsp'}, {'stringValue': 'Allspr'}, {'stringValue': 'Allspro'}, {'stringValue': 'Allsprou'}, {'stringValue': 'Allsprout'}, {'stringValue': 'Alls'}, {'stringValue': 'Allsa'}, {'stringValue': 'Allsal'}, {'stringValue': 'Allsala'}, {'stringValue': 'Allsalad'}, {'stringValue': 'AllMung Sprout Salad'}, {'stringValue': 'All '}, {'stringValue': 'All'}]}}, 'name_hindi': {'stringValue': ' अंकुरित मूंग सलाद'}, 'recipe_id': {'stringValue': 'sprout_mung_salad'}, 'ref': {'referenceValue': 'projects/rassoi-767af/databases/(default)/documents/recipes_temp/sprout_mung_salad'}, 'status': {'stringValue': 'notLive'}, 'uid': {'stringValue': 'qnxzsG184Gfp17RDnvGdAg6DFu23'}, 'which_meal': {'arrayValue': {}}, 'youtube_link': {'stringValue': 'https://www.youtube.com/watch?v=u3dw0dooJP4'}}, 'name': 'projects/rassoi-767af/databases/(default)/documents/temp/qnxzsG184Gfp17RDnvGdAg6DFu23sprout_mung_salad', 'updateTime': '2022-09-18T18:20:56.707871Z'}}"


def hello_firestore(event):

    # resource_string = context.resource
    # print out the resource string that triggered the function
    # print(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object

    # print(str(event))
    c = str(event)
    d = ast.literal_eval(c)

    if d["oldValue"]['fields']["meal_time"]['arrayValue']:

        oldvalue_len = len(d["oldValue"]['fields']
                           ["meal_time"]['arrayValue']['values'])
        old_value = d["oldValue"]['fields']["meal_time"]['arrayValue']['values']
    else:
        old_value = []
        oldvalue_len = 0

    if d["value"]['fields']["meal_time"]['arrayValue']:

        newvalue_len = len(d["value"]['fields']["meal_time"]
                           ['arrayValue']['values'])
        new_value = d["value"]['fields']["meal_time"]['arrayValue']['values']
    else:
        new_value = []
        newvalue_len = 0

    new_value_list = []
    for item in new_value:
        new_value_list.append(item['stringValue'])
    old_value_list = []
    for item in old_value:
        old_value_list.append(item['stringValue'])

    if list(set(new_value_list) - set(old_value_list)):
        action = "added"
    else:
        action = "deleted"
    recipe_status_changed = d["value"]['fields']["recipe_id"]['stringValue']
    recived_uid = d["value"]['fields']["uid"]['stringValue']

    recipe = db.collection(u'temp').stream()

    for doc in recipe:
        recipe_detail = db.collection(u'temp').document(doc.id).get().to_dict()
        recipe_id1 = recipe_detail["recipe_id"]
        user_id = recipe_detail["uid"]
        # print(user_id)
        if recipe_id1 == recipe_status_changed and recived_uid == user_id:
            recipe_name = recipe_detail["name"]
            meal_day = recipe_detail["day"]
            meal_time = recipe_detail["meal_time"]
            a_split = recipe_detail["ingred_names"].split("*")
            # print(len(a_split))
            for i in range(len(a_split)):
                if i != len(a_split)-1:
                    b_split = a_split[i].split("+")
                    inged_id = b_split[1]
                    inged_name = b_split[0]
                    inged_name_hindi = b_split[2]
                    inged_img = b_split[3]
                    doc_name = user_id+inged_id
                    if db.collection(u'meal_ingred').document(doc_name).get().exists:
                        ingred_detail = db.collection(
                            u'meal_ingred').document(doc_name).get().to_dict()
                        # print("ingred_detail", ingred_detail)
                        recipe_names = ingred_detail["recipe_names"]
                        if action == "added":
                            if recipe_name in recipe_names:
                                # print(
                                #     "item already exists"
                                # )
                                pass

                            else:
                                recipe_names.append(recipe_name)
                                print("----------", recipe_names, recipe_name,
                                      ingred_detail["recipe_names"], type(ingred_detail["recipe_names"]))
                                db.collection(u'meal_ingred').document(
                                    doc_name).update({u"recipe_names": firestore.ArrayUnion([recipe_name])})

                                db.collection(u'meal_ingred').document(
                                    doc_name).update({u"meal_count": firestore.Increment(1)})

                        if action == "deleted":
                            if recipe_name in recipe_names:
                                recipe_names.remove(recipe_name)
                                print("----------", recipe_names, recipe_name,
                                      ingred_detail["recipe_names"], type(ingred_detail["recipe_names"]))
                                db.collection(u'meal_ingred').document(
                                    doc_name).update({u"recipe_names": firestore.ArrayRemove([recipe_name])})
                                db.collection(u'meal_ingred').document(
                                    doc_name).update({u"meal_count": firestore.Increment(-1)})

                            else:
                                # print(
                                #     "item not present"
                                # )
                                pass

                    else:

                        ingred_payload = {
                            u'inged_id': inged_id,
                            u'english': inged_name,
                            u'hindi': inged_name_hindi,
                            u'img': inged_img,
                            u'recipe_names': [recipe_name],
                            u'user_uid': user_id,
                            u"status": "unavailable",
                            u"meal_count": len([recipe_name])
                        }
                        print(ingred_payload)

                        db.collection(u'meal_ingred').document(
                            doc_name).set(ingred_payload)


hello_firestore(c)
