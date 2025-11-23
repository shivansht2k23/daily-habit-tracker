# Daily Habit Tracker - Shivansh Tripathi (Project 2)

import json
from datetime import datetime

HABIT_FILE = "habits.json"

def load_habits():
    try:
        with open(HABIT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_habits(habits):
    with open(HABIT_FILE, "w") as f:
        json.dump(habits, f, indent=4)

def mark_habit(habits):
    name = input("Enter habit name: ")
    today = datetime.now().strftime("%Y-%m-%d")

    if name not in habits:
        habits[name] = []

    habits[name].append(today)
    print(f"Marked '{name}' as completed for today!")
    save_habits(habits)

def view_habits(habits):
    if not habits:
        print("No habits tracked yet.")
        return

    for habit, dates in habits.items():
        print(f"- {habit}: {len(dates)} days completed")

def main():
    habits = load_habits()

    while True:
        print("\n--- Daily Habit Tracker ---")
        print("1. Mark a habit")
        print("2. View progress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            mark_habit(habits)
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
