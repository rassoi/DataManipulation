
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import random
bFWithChutney_list = ["Alu Parath",
                      "Gobi Parath", "Muly Paratha", "Suji Chilla", "Soft and Fluffy Raw"]
bF_list = ["Pancake", "Banana PanCake", "Poha",
           "Potato Sanwitch", "Mung Dal Sprout"]
bFChutney_list = ["green chatney", "red chutney"]


if not firebase_admin._apps:
    cred = credentials.Certificate(
        '/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
meals_list = []

gravySabji_list = []
drySaji_list = []
dal1_list = []
bF_list = []
bread_list = []
rice_list = []
chutney_list = []
masoorDalSabji_List = []
bFChutney_list = []

recipes = db.collection(u'recipes_temp').stream()
for doc in recipes:
    meals_list.append(doc.id)

for item in meals_list:
    recipe = db.collection(u'recipes_temp').document(item).get().to_dict()
    categoryName = recipe["categoryName"]
    if "dal" in categoryName:
        dal1_list.append(item)

    if "Breakfast" in categoryName:
        bF_list.append(item)

    if "Breads" in categoryName:
        bread_list.append(item)

    if "Dry Sabji" in categoryName:
        drySaji_list.append(item)
        try:
            subCategories = recipe["subCategories"]
            if "MungDalSabji" in subCategories:
                masoorDalSabji_List.append(item)
        except Exception as e:
            print(e)

    if "Gravy Sabji" in categoryName:
        gravySabji_list.append(item)

    if "Rice" in categoryName:
        rice_list.append(item)

    if "Side Dish" in categoryName:
        chutney_list.append(item)
        try:
            subCategories = recipe["subCategories"]
            if "BfChutney" in subCategories:
                bFChutney_list.append(item)
        except Exception as e:
            print(e)


print(len(dal1_list), dal1_list)
print(len(bF_list), bF_list)
print(len(bread_list), bread_list)
print(len(drySaji_list), drySaji_list)
print(len(gravySabji_list), gravySabji_list)
print(len(rice_list), rice_list)
print(len(chutney_list), chutney_list)
print(len(bFChutney_list), bFChutney_list)
print(len(masoorDalSabji_List), masoorDalSabji_List)
# try:
#     subCategories = recipe["subCategories"]
#     print(subCategories)
# except Exception as e:
#     print(e)
