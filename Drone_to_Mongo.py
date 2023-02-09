from djitellopy import tello
from time import sleep
from pymongo import MongoClient
import datetime
import os

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
print(drone.get_temperature())

# drone.takeoff()
# drone.send_rc_control(0, 50, 0, 0)
# sleep(2)
# drone.send_rc_control(0, 0, 0, 0)
# drone.land()

drone_data = {"drone_battery": drone.get_battery(),
              "drone_temperature": drone.get_temperature(),
              "text": "Testing Drone!",
              "date": datetime.datetime.utcnow()}

# connect to the given wifi network
os.system('networksetup -setairportnetwork en0 KIKI2.4 ''thalentusxxxxx''')
sleep(10)

client = MongoClient()
client = MongoClient("mongodb+srv://xxxxxx:xxxxxx@cluster0.u17s2jz.mongodb.net/?retryWrites=true&w=majority")

db = client.drone_db

drone_collection = db.drone_collection
drone_data_id = drone_collection.insert_one(drone_data).inserted_id
