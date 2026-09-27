from datetime import datetime, timedelta
from models.membership import MembershipModel
from models.book import BookModel

class BorrowerModel:
    @staticmethod
    def count_borrowed_books(conn, name):
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM borrower_list WHERE Name = %s AND Date_of_return >= CURDATE()"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def borrow_book(conn, name, book_name):
        user_tier = MembershipModel.get_user_tier(conn, name)
        max_books, loan_days, _ = MembershipModel.get_perks(user_tier)
        currently_borrowed = BorrowerModel.count_borrowed_books(conn, name)

        if currently_borrowed >= max_books:
            return False, f"Limit reached! As a {user_tier} member, you can borrow a maximum of {max_books} book(s)."

        avail = BookModel.check_availability(conn, book_name)
        if avail is None:
            return False, f"Error: Book '{book_name}' not found in the library."
        if avail.lower() != "yes":
            return False, f"Sorry, '{book_name}' is currently unavailable/checked out."

        today = datetime.today().date()
        due_date = today + timedelta(days=loan_days)

        cursor = conn.cursor()
        insert_query = """
            INSERT INTO borrower_list (Name, Book, Date_of_borrowing, Date_of_return, Compensation, Membership, Payment_mode)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, book_name, today, due_date, "None", user_tier, "None"))
        conn.commit()
        cursor.close()

        BookModel.update_availability(conn, book_name, False)
        return True, f"Book Borrowed Successfully!\nBorrower: {name} (Tier: {user_tier})\nBook: {book_name}\nDue Date ({loan_days} days): {due_date}"

    @staticmethod
    def return_book(conn, name, book_name):
        cursor = conn.cursor()
        select_query = """
            SELECT Date_of_return, Membership 
            FROM borrower_list 
            WHERE LOWER(Name) = LOWER(%s) AND LOWER(Book) = LOWER(%s)
            ORDER BY Date_of_borrowing DESC LIMIT 1
        """
        cursor.execute(select_query, (name, book_name))
        result = cursor.fetchone()

        if result is None:
            cursor.close()
            return False, f"No record found for user '{name}' borrowing '{book_name}'."

        due_date, tier = result[0], result[1]
        today = datetime.today().date()
        _, _, fee_per_day = MembershipModel.get_perks(tier)

        if today > due_date:
            days_late = (today - due_date).days
            total_fee = days_late * fee_per_day
            compensation = "Late (Fee Waived - Platinum Perk)" if total_fee == 0 else f"Late Fee (Rs {total_fee})"
        else:
            compensation = "None"

        update_borrower = """
            UPDATE borrower_list 
            SET Compensation = %s, Date_of_return = %s 
            WHERE LOWER(Name) = LOWER(%s) AND LOWER(Book) = LOWER(%s)
        """
        cursor.execute(update_borrower, (compensation, today, name, book_name))
        conn.commit()
        cursor.close()

        BookModel.update_availability(conn, book_name, True)
        return True, f"Book Returned Successfully!\nDue Date was: {due_date}\nReturn Date:  {today}\nCompensation: {compensation}"

    @staticmethod
    def get_user_history(conn, name):
        cursor = conn.cursor()
        cursor.execute("SELECT Book, Date_of_borrowing, Date_of_return, Compensation FROM borrower_list WHERE LOWER(Name) = LOWER(%s)", (name,))
        records = cursor.fetchall()
        cursor.close()
        return records