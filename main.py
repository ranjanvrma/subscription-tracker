from db import get_connection
from datetime import datetime, timedelta

def add_subscription():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Subscription Name: ")
    category = input("Category: ")
    cost = float(input("Cost: "))
    billing_cycle = input("Billing Cycle (Monthly, Yearly): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")

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

def view_subscriptions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from subscriptions")
    results = cursor.fetchall()

    for row in results:
        print(row)
    
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n ----Subscription Tracker----")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Exit")
        choice = input("Choose Option: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            view_subscriptions()    
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()