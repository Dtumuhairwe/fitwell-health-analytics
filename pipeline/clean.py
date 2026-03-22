import json
import os

def load_data():
    """
    Loads the raw data we saved in fetch.py
    """
    with open("data/fitness_data.json", "r") as f:
        data = json.load(f)
    print(f"✅ Loaded data with {len(data['weekly_logs'])} weekly logs")
    return data

def clean_weekly_logs(data):
    """
    Cleans and structures the weekly logs for the dashboard.
    - Makes sure all numbers are integers
    - Caps scores between 0 and 100
    - Adds a total sessions column
    """
    cleaned = []
    for log in data["weekly_logs"]:
        cleaned.append({
            "week": log["week"],
            "cardio": max(0, int(log["cardio_sessions"])),
            "strength": max(0, int(log["strength_sessions"])),
            "flexibility": max(0, int(log["flexibility_sessions"])),
            "total_sessions": int(log["cardio_sessions"]) + 
                            int(log["strength_sessions"]) + 
                            int(log["flexibility_sessions"]),
            "calories": min(5000, max(0, int(log["calories_burned"]))),
            "sleep_score": min(100, max(0, int(log["sleep_score"]))),
            "mental_score": min(100, max(0, int(log["mental_health_score"])))
        })
    print(f"✅ Cleaned {len(cleaned)} weekly records")
    return cleaned

def save_clean_data(cleaned):
    """
    Saves the cleaned data — this is what the dashboard will use
    """
    os.makedirs("data", exist_ok=True)
    with open("data/clean_data.json", "w") as f:
        json.dump(cleaned, f, indent=2)
    print("✅ Clean data saved to data/clean_data.json")

if __name__ == "__main__":
    data = load_data()
    cleaned = clean_weekly_logs(data)
    save_clean_data(cleaned)