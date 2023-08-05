import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('zectaries/key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sic4-mentor-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/test')
button = db.reference("button")
print(ref.get())
print(ref.set({"nama" : "Mentor Angga"}))
print(button.set({"value" : 1}))
print(button.get())

dataButton = button.get()

print(dataButton["value"]);

