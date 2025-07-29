import time
from datetime import datetime, timedelta
import random

class Train:
    def __init__(self, name, route):
        self.name = name
        self.route = route  # list of (station_name, distance_km_from_start)
        self.current_index = 0
        self.speed_kmh = 60  # You can randomize or change this later
        self.start_time = datetime.now()

    def get_status(self):
        if self.current_index >= len(self.route):
            return f"🚉 Train {self.name} has completed its journey."

        station_name, station_dist = self.route[self.current_index]
        eta = self.start_time + timedelta(hours=station_dist / self.speed_kmh)
        return (f"🚆 Train {self.name} is heading to {station_name} "
                f"({station_dist} km). ETA: {eta.strftime('%H:%M:%S')}")

    def update_location(self):
        # Simulate train movement
        if self.current_index < len(self.route) - 1:
            self.current_index += 1
        else:
            print(f"✅ Train {self.name} has reached its final destination.")

def simulate_tracking(train, interval_sec=2):
    print("📡 Starting Train Tracking System...\n")
    while train.current_index < len(train.route):
        print(train.get_status())
        train.update_location()
        time.sleep(interval_sec)
    print("📍 Tracking complete.")

# Define a sample route (station_name, distance_from_start in km)
sample_route = [
    ("Budapest", 0),
    ("Kecskemét", 86),
    ("Szeged", 175),
    ("Makó", 220)
]

# Create train object
train_1 = Train("IC 707", sample_route)

# Start simulation
simulate_tracking(train_1)
