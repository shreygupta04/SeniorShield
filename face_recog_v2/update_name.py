import pyrebase

config = {
    "apiKey": "AIzaSyDP0mHM4XP-us0a3sHd5QojTSObnwXJDQo",
    "authDomain": "seniorshield-84d95.firebaseapp.com",
    "databaseURL": "https://seniorshield-84d95-default-rtdb.firebaseio.com",
    "projectId": "seniorshield-84d95",
    "storageBucket": "seniorshield-84d95.appspot.com",
    "messagingSenderId": "475934775503",
    "appId": "1:475934775503:web:077a1a5614ed4c2c63bfba"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("name").update({'name': })
