import unittest
from models.membership import MembershipModel

class TestLibraryBusinessLogic(unittest.TestCase):
    def test_silver_tier_perks(self):
        max_books, loan_days, fee = MembershipModel.get_perks("Silver")
        self.assertEqual(max_books, 1)
        self.assertEqual(loan_days, 14)
        self.assertEqual(fee, 10)

    def test_platinum_fee_waiver(self):
        max_books, loan_days, fee = MembershipModel.get_perks("Platinum")
        self.assertEqual(max_books, 5)
        self.assertEqual(loan_days, 30)
        self.assertEqual(fee, 0)

    def test_fallback_tier(self):
        max_books, loan_days, fee = MembershipModel.get_perks("NonExistent")
        self.assertEqual(max_books, 1)

if __name__ == "__main__":
    unittest.main()