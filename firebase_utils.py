import pyrebase

# Firebase configuration
config = {
    "apiKey": "YAIzaSyAknhVZ6pzTdODkjfYMl-zKGW2KoToH-4IASE_API_KEY",
    "authDomain": "radar-using.firebaseapp.com",
    "databaseURL": "https://radar-using-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "radar-using.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Function to fetch radar data from Firebase
def get_radar_data():
    data = db.child("RadarData").get().val()  # Replace with your path
    return data if data else {}  # Return empty dictionary if no data