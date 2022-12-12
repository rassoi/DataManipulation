
import datetime
import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import messaging


if not firebase_admin._apps:
    cred = credentials.Certificate(
        r'/Users/manishsingh/Documents/Study/meal_entry_python1/rassoi-767af-firebase-adminsdk-q09j7-a66f37f511.json')
    default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def send_token_push(title, body, tokens):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        tokens=tokens
    )
    messaging.send_multicast(message)


def abc():
    test_list = []
    ids_ref = db.collection(u'users').stream()
    for id_ref in ids_ref:
        if(id_ref.id == 'qnxzsG184Gfp17RDnvGdAg6DFu23'):
            fcm_token = ''
            fcm_tokens_ref = db.collection(u'users').document(
                id_ref.id).collection(u'fcm_tokens').stream()
            for fcm_token_ref in fcm_tokens_ref:
                fcm_token = db.collection(u'users').document(id_ref.id).collection(
                    u'fcm_tokens').document(fcm_token_ref.id).get().to_dict()['fcm_token']
                # fcm_token=fcm_token_ref.id
                break
            print(f"the fcm token is {fcm_token}")
            test_list += [fcm_token]
            print(type(test_list))
            print(test_list)
            # subscribe_news(test_list)
            send_token_push('Taaza Taaza Khaana',
                            'Aaj hi apne meals karo schedule!!!', test_list)
            break
            #send_topic_push('Taaza Taaza Khaana', 'abhi Karo apne meals schedule aur maid banayegi Taaza Khaana. Bina tension ke phuk sakte ho!!!')
            #send_token_push('notfication!!!','this is a default notificqtion',test_list)
        # print(id_ref.id)
    return


abc()
