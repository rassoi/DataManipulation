import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random


# # Types
bFtype_list = ["bF_list"]*3 + ["bFWithChutney_list"]*1
# dalType_list = ["arhar", "chana dal"]*3 + ["yellow_mung"]*1

# # Options
dalNoDalType_list = ["dal"]*1 + ["noDal"]*2



if not firebase_admin._apps:
    cred = credentials.Certificate(
        'abc.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
meals_list = []

gravySabji_list = []
drySaji_list = []
dalType_list = []
bF_list = []
bread_list = []
rice_list = []
chutney_list = []
masoorDalSabji_List = []
bFChutney_list = []
bFWithChutney_list = []

recipes = db.collection(u'recipes_temp').stream()
for doc in recipes:
    meals_list.append(doc.id)

for item in meals_list:
    recipe = db.collection(u'recipes_temp').document(item).get().to_dict()
    categoryName = recipe["categoryName"]
    if "dal" in categoryName:
        dalType_list.append(item)

    if "Breakfast" in categoryName:
        try:
            subCategories = recipe["subCategories"]
            if "bfWithChutney" in subCategories:
                bFWithChutney_list.append(item)

        except Exception as e:
            bF_list.append(item)
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





def lunch():

    rice_index = random.randint(0, len(rice_list)-1)
    lunch = [rice_list[rice_index]]

    dalNoDal_index = random.randint(0, len(dalNoDalType_list)-1)
    dalNoDal = dalNoDalType_list[dalNoDal_index]

    # print(dalNoDal_list[dalNoDal])
    if dalNoDal == "dal":
        dalType_index = random.randint(0, len(dalType_list)-1)
        dalType = dalType_list[dalType_index]
        # print(dalType)
        lunch.append(dalType)
        if dalType == "arhar" or dalType == "chana dal":
            drySaji_index = random.randint(0, len(drySaji_list)-1)
            drySaji = drySaji_list[drySaji_index]
            lunch.append(drySaji)
        else:
            masoorDalSabji_index = random.randint(
                0, len(masoorDalSabji_List)-1)
            masoorDalSabji = masoorDalSabji_List[masoorDalSabji_index]
            lunch.append(masoorDalSabji)
            # print(masoorDalSabji)

    else:
        gravySabji_index = random.randint(0, len(gravySabji_list)-1)
        gravySabji = gravySabji_list[gravySabji_index]
        # print(gravySabji)
        lunch.append(gravySabji)

    gravySabji_index = random.randint(0, len(gravySabji_list)-1)

    chutney_index = random.randint(0, len(chutney_list)-1)
    chutney = chutney_list[chutney_index]
    lunch.append(chutney)
    return(lunch)
    # print(lunch)


def dinner():
    dalNoDal_index = random.randint(0, len(dalNoDalType_list)-1)
    dalNoDal = dalNoDalType_list[dalNoDal_index]

    # rice_index = random.randint(0, len(rice_list)-1)

    bread_index = random.randint(0, len(bread_list)-1)
    dinner = [bread_list[bread_index]]

    # print(dalNoDal_list[dalNoDal])
    if dalNoDal == "dal":
        dalType_index = random.randint(0, len(dalType_list)-1)
        dalType = dalType_list[dalType_index]
        # print(dalType)
        dinner.append(dalType)
        if dalType == "arhar" or dalType == "chana":
            drySaji_index = random.randint(0, len(drySaji_list)-1)
            drySaji = drySaji_list[drySaji_index]
            dinner.append(drySaji)
        else:
            masoorDalSabji_index = random.randint(
                0, len(masoorDalSabji_List)-1)
            masoorDalSabji = masoorDalSabji_List[masoorDalSabji_index]
            dinner.append(masoorDalSabji)
            # print(masoorDalSabji)

    else:
        gravySabji_index = random.randint(0, len(gravySabji_list)-1)
        gravySabji = gravySabji_list[gravySabji_index]
        # print(gravySabji)
        dinner.append(gravySabji)

    gravySabji_index = random.randint(0, len(gravySabji_list)-1)

    chutney_index = random.randint(0, len(chutney_list)-1)
    chutney = chutney_list[chutney_index]
    dinner.append(chutney)
    return(dinner)
    print(dinner)


def brakefast():
    bFtype_index = random.randint(0, len(bFtype_list)-1)
    bFtype = bFtype_list[bFtype_index]
    if bFtype == "bF_list":
        bF_index = random.randint(0, len(bF_list)-1)
        bF = [bF_list[bF_index]]
    else:
        bF_index = random.randint(0, len(bFWithChutney_list)-1)
        bF = [bFWithChutney_list[bF_index]]
        bFChutney_index = random.randint(0, len(bFChutney_list)-1)
        bF.append(bFChutney_list[bFChutney_index])
    return(bF)



