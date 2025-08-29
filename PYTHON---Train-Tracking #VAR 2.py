import time
import random

# Sample train database
trains = [
    {"id": 1, "route": "Budapest - Vienna", "departure": "10:30", "arrival": "13:00"},
    {"id": 2, "route": "Budapest - Berlin", "departure": "12:00", "arrival": "20:15"},
    {"id": 3, "route": "Budapest - Prague", "departure": "14:45", "arrival": "19:10"},
]

def show_trains():
    print("🚆 Train Tracker App 🚆")
    print("="*30)
    for train in trains:
        print(f"Train {train['id']} | {train['route']} | Dep: {train['departure']} | Arr: {train['arrival']}")

def track_train(train_id):
    train = next((t for t in trains if t['id'] == train_id), None)
    if not train:
        print("Train not found!")
        return
    print(f"Tracking Train {train['id']} - {train['route']}")
    for i in range(5):
        delay = random.choice([0, 5, 10])  # simulate delay
        print(f"Update {i+1}: Train is on route, delay {delay} minutes.")
        time.sleep(1)

if __name__ == "__main__":
    show_trains()
    choice = int(input("Enter train ID to track: "))
    track_train(choice)
