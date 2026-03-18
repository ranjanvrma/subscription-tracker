from db import get_connection
from datetime import datetime, timedelta

def add_subscription():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Subscription Name: ")
    category = input("Category: ")
    try:
        cost = float(input("Cost: "))
    except ValueError:
        print("Invalid cost, please enter a number.")
        return
    billing_cycle = input("Billing Cycle (Monthly, Yearly): ")
    start_date = input("Start Date (DD-MM-YYYY): ")
    
    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")

    if billing_cycle.lower() ==  "monthly":
        next_renewal = start_date_obj + timedelta(days=30)
    elif billing_cycle.lower() == "yearly":
        next_renewal = start_date_obj + timedelta(days=365)
    else:
        print("Invalid billing cycle. Please enter 'Monthly' or 'Yearly'.")
        return
    
    query = """
    insert into subscriptions
    (name, category, cost, billing_cycle, start_date, next_renewal)
    values (%s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        category,
        cost,
        billing_cycle,
        start_date_obj,
        next_renewal.date()
    )

    cursor.execute(query, values)
    conn.commit()

    print("Subscription added!")

    cursor.close()
    conn.close()

def remove_subscription():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        subscription_id = int(input("Enter Subscription ID to remove: "))
    except ValueError:
        print("Invalid ID")
        return
    cursor.execute("delete from subscriptions where id = %s", (subscription_id,))
    conn.commit()

    print("Subscription removed!")

    cursor.close()
    conn.close()
    
def view_subscriptions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from subscriptions")
    results = cursor.fetchall()

    if not results:
        print("No subscriptions found.")
    else:
        print("\nYour Subscriptions:")
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Cost: {row[3]} | Billing Cycle: {row[4]} | Start Date: {row[5]} | Next Renewal: {row[6]}")
    
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n ----Subscription Tracker----")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Remove Subscription")
        print("4. Exit")
        choice = input("Choose Option: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            view_subscriptions()    
        elif choice == "3":
            remove_subscription()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()