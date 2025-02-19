import calendar
from datetime import datetime

events = {}

def display_calendar(year, month):
    print(calendar.month(year, month))

def add_event():
    date = input("Enter the date (YYYY-MM-DD): ")
    event = input("Enter the event: ")
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]
    print("Event added.")

def view_events():
    date = input("Enter the date (YYYY-MM-DD): ")
    if date in events:
        print(f"Events on {date}:")
        for e in events[date]:
            print(f"- {e}")
    else:
        print("No events on this date.")

def main():
    while True:
        print("1. Display Calendar")
        print("2. Add Event")
        print("3. View Events")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            display_calendar(year, month)
        elif choice == "2":
            add_event()
        elif choice == "3":
            view_events()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
