from datetime import datetime

class MembershipModel:
    TIERS = {
        "Silver":   {"price": 100, "max_books": 1, "loan_days": 14, "fine_per_day": 10},
        "Gold":     {"price": 200, "max_books": 3, "loan_days": 21, "fine_per_day": 5},
        "Platinum": {"price": 300, "max_books": 5, "loan_days": 30, "fine_per_day": 0},
    }

    @staticmethod
    def get_perks(tier):
        """Return max_books, loan_days, and late_fee_per_day."""
        info = MembershipModel.TIERS.get(tier, MembershipModel.TIERS["Silver"])
        return info["max_books"], info["loan_days"], info["fine_per_day"]

    @staticmethod
    def get_user_tier(conn, name):
        """Find the user's membership tier from the database. Default to Silver."""
        cursor = conn.cursor()
        query = "SELECT MembershipType FROM memberships WHERE Name = %s ORDER BY PurchaseDate DESC LIMIT 1"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result is not None else "Silver"

    @staticmethod
    def buy_membership(conn, name, tier_choice):
        plans = {"1": ("Silver", 100), "2": ("Gold", 200), "3": ("Platinum", 300)}
        if tier_choice not in plans:
            return False, "Invalid choice selected."

        tier_name, price = plans[tier_choice]
        today = datetime.today().date()
        cursor = conn.cursor()

        insert_query = "INSERT INTO memberships (Name, MembershipType, Price, PurchaseDate) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (name, tier_name, price, today))

        update_query = "UPDATE borrower_list SET Membership = %s WHERE LOWER(Name) = LOWER(%s)"
        cursor.execute(update_query, (tier_name, name))

        conn.commit()
        cursor.close()
        return True, f"Success! {name} has upgraded to the {tier_name} plan for Rs {price}."