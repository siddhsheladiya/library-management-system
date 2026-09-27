import sys
from database.connection import get_connection
from models.book import BookModel
from models.membership import MembershipModel
from models.borrower import BorrowerModel

def view_books_cli(conn):
    all_books = BookModel.get_all_books(conn)
    print("\n-------------------------------------------------------------")
    print("BOOK CATALOG")
    print("-------------------------------------------------------------")
    if not all_books:
        print("No books available in the database.")
    else:
        for row in all_books:
            status = "Available" if row[3].lower() == "yes" else "Checked Out"
            print(f"- {row[0]} | Author: {row[1]} | Genre: {row[2]} | Status: {status}")
    print("-------------------------------------------------------------")

def borrow_book_cli(conn):
    print("\n--- BORROW A BOOK ---")
    name = input("Enter your name: ").strip()
    book_name = input("Enter the book name: ").strip()
    if not name or not book_name:
        print("Error: Name and Book Name cannot be blank.")
        return
    _, msg = BorrowerModel.borrow_book(conn, name, book_name)
    print(f"\n{msg}")

def return_book_cli(conn):
    print("\n--- RETURN A BOOK ---")
    name = input("Enter your name: ").strip()
    book_name = input("Enter the book name: ").strip()
    if not name or not book_name:
        print("Error: Name and Book Name cannot be blank.")
        return
    _, msg = BorrowerModel.return_book(conn, name, book_name)
    print(f"\n{msg}")

def view_membership_plans_cli():
    print("\n================ MEMBERSHIP TIERS & PERKS ================")
    print("1. Silver   - Rs 100 | Limit: 1 Book | 14 Days | Fine: Rs 10/day")
    print("2. Gold     - Rs 200 | Limit: 3 Books | 21 Days | Fine: Rs 5/day")
    print("3. Platinum - Rs 300 | Limit: 5 Books | 30 Days | Fine: FREE (Rs 0)")
    print("==========================================================")

def buy_membership_cli(conn):
    print("\n--- BUY / UPGRADE MEMBERSHIP ---")
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be blank.")
        return
    view_membership_plans_cli()
    choice = input("Select plan (1/2/3): ").strip()
    _, msg = MembershipModel.buy_membership(conn, name, choice)
    print(f"\n{msg}")

def user_profile_cli(conn):
    print("\n--- USER PROFILE ---")
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be blank.")
        return
    tier = MembershipModel.get_user_tier(conn, name)
    max_books, loan_days, fee_per_day = MembershipModel.get_perks(tier)
    records = BorrowerModel.get_user_history(conn, name)

    print("\n---------------- PROFILE DETAILS ----------------")
    print(f"Name:             {name}")
    print(f"Membership Tier:  {tier}")
    print(f"Allowed Books:    {max_books}")
    print(f"Borrowing Period: {loan_days} Days")
    print(f"Late Fee Rate:    {'Waived (Free)' if fee_per_day == 0 else f'Rs {fee_per_day} per day'}")
    print("\nBorrowing History:")
    if not records:
        print("  No borrowing history found.")
    else:
        for item in records:
            print(f"  * {item[0]} (Borrowed: {item[1]} | Due/Returned: {item[2]} | Status: {item[3]})")
    print("-------------------------------------------------")

def main():
    try:
        conn = get_connection()
    except Exception as e:
        print(f"Database Connection Error: {e}")
        print("Please check database/connection.py and make sure MySQL service is running.")
        sys.exit(1)

    while True:
        print("\n==========================================")
        print("        LIBRARY MANAGEMENT SYSTEM         ")
        print("==========================================")
        print("1. View Book Catalog")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Membership Plans & Perks")
        print("5. Buy / Upgrade Membership")
        print("6. View User Profile")
        print("7. Exit")
        print("==========================================")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            view_books_cli(conn)
        elif choice == "2":
            borrow_book_cli(conn)
        elif choice == "3":
            return_book_cli(conn)
        elif choice == "4":
            view_membership_plans_cli()
        elif choice == "5":
            buy_membership_cli(conn)
        elif choice == "6":
            user_profile_cli(conn)
        elif choice == "7":
            print("\nThank you for using the Library Management System. Goodbye!")
            conn.close()
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()