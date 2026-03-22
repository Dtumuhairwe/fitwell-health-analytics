import json
import os
import random

def fetch_data():
    """
    Returns mock fitness data that mirrors the Wger API structure.
    Swap this out for a real API call when network allows.
    """
    print("Loading fitness data...")

    exercises = [
        {"id": 1, "name": "Running", "category": "Cardio"},
        {"id": 2, "name": "Push Ups", "category": "Strength"},
        {"id": 3, "name": "Cycling", "category": "Cardio"},
        {"id": 4, "name": "Squats", "category": "Strength"},
        {"id": 5, "name": "Yoga", "category": "Flexibility"},
        {"id": 6, "name": "Pull Ups", "category": "Strength"},
        {"id": 7, "name": "Swimming", "category": "Cardio"},
        {"id": 8, "name": "Plank", "category": "Strength"},
        {"id": 9, "name": "Stretching", "category": "Flexibility"},
        {"id": 10, "name": "Jump Rope", "category": "Cardio"},
    ]

    # Simulate weekly workout logs for 8 weeks
    weekly_logs = []
    for week in range(1, 9):
        weekly_logs.append({
            "week": f"Week {week}",
            "cardio_sessions": random.randint(1, 3),
            "strength_sessions": random.randint(1, 3),
            "flexibility_sessions": random.randint(0, 2),
            "calories_burned": random.randint(1800, 2600),
            "sleep_score": random.randint(55, 90),
            "mental_health_score": random.randint(55, 85),
        })

    print(f"✅ Loaded {len(exercises)} exercises and {len(weekly_logs)} weekly logs!")
    return {"exercises": exercises, "weekly_logs": weekly_logs}

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open("data/fitness_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Saved to data/fitness_data.json")

if __name__ == "__main__":
    data = fetch_data()
    save_data(data)