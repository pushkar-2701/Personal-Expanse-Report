import csv
import datetime
import os

FILE = 'expenses.csv'
HEADER = ['Date', 'Amount', 'Category', 'Description']

# --- Helper Functions ---

def init_file():
    """Initializes CSV file with header if it doesn't exist."""
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            csv.writer(f).writerow(HEADER)
        print(f"✅ Created new expense file: {FILE}")

def get_data():
    """Reads all data rows from the CSV file."""
    try:
        with open(FILE, 'r', newline='') as f:
            # reader converts each line into a list of strings
            return list(csv.reader(f))[1:] # [1:] skips the header
    except FileNotFoundError:
        print(f"Error: File '{FILE}' not found.")
        return []

# --- Main Application ---

def main():
    init_file()
    
    while True:
        print("\n💰 Expense Tracker\n1. Add\n2. View\n3. Summary\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            try:
                amount = float(input("Amount ($): "))
                category = input("Category: ")
                description = input("Description: ")
                date = datetime.datetime.now().strftime('%Y-%m-%d')
                
                new_row = [date, amount, category, description]
                
                with open(FILE, 'a', newline='') as f:
                    csv.writer(f).writerow(new_row)
                print("Expense added.")
                
            except ValueError:
                print("Invalid amount. Please enter a number.")
            
        elif choice == '2':
            data = get_data()
            if not data:
                print("No expenses recorded.")
                continue
                
            print("\n--- All Expenses ---")
            for row in data:
                print(f"Date: {row[0]}, Amount: ${float(row[1]):.2f}, Category: {row[2]}, Desc: {row[3]}")

        elif choice == '3':
            data = get_data()
            if not data:
                print("No expenses recorded for summary.")
                continue
                
            summary = {}
            for _, amount_str, category, _ in data:
                try:
                    amount = float(amount_str)
                    summary[category] = summary.get(category, 0) + amount
                except ValueError:
                    continue # Skip invalid entries

            print("\n--- Category Summary ---")
            for cat, total in summary.items():
                print(f"{cat}: ${total:.2f}")

        elif choice == '4':
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()