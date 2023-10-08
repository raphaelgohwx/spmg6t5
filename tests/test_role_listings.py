import unittest
from datetime import date

from backend.app import Role_Listing

class TestRoleListing(unittest.TestCase):
    
    # positive test case -> assert True if all fields are not empty, not null, primary key is unique and date is in the future
    # checks that role listing is created into database correctly, queried, and then deleted
    def test_create_Role_Listing(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2023-12-10", "IT Team description is here", "IT")
        current_number_of_role_listing = len(Role_Listing1.retrieve_all_role_listing_ID())
        assert Role_Listing1.create_Role_Listing() == "Success"
        assert current_number_of_role_listing+1 == len(Role_Listing1.retrieve_all_role_listing_ID())
        assert Role_Listing1.delete_Role_Listing() == True

    # negative test case -> date is in the past
    def test_create_Role_Listing_reject_past_date(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2022-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: Date closed is in the past."

    # boundary test case -> date is today
    def test_create_Role_Listing_reject_today_date(self):
        today_date_str = date.today().strftime("%Y-%m-%d")
        Role_Listing2 = Role_Listing(10, "IT Team", today_date_str, "IT Team description is here", "IT")
        assert Role_Listing2.create_Role_Listing() == "Error: Date closed is in the past."

    # negative test case -> assert False if primary key is not unique
    def test_create_Role_Listing_reject_duplicate_primary_key(self):
        Role_Listing1 = Role_Listing(1, "IT Team", "2023-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: Role Listing ID already exists."

    # negative test case -> assert False for any empty Strings
    def test_create_Role_Listing_empty_Role_Listing_ID(self):
        Role_Listing1 = Role_Listing("", "IT Team", "2023-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_empty_Role_Name(self):
        Role_Listing1 = Role_Listing(10, "", "2023-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_empty_Date_Closed(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_empty_Role_Description(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2023-12-10", "", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_empty_Dept(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2023-12-10", "IT Team description is here", "")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    # negative test case -> assert False for any Null values
    def test_create_Role_Listing_null_Role_Listing_ID(self):
        Role_Listing1 = Role_Listing(None, "IT Team", "2023-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_null_Role_Name(self):
        Role_Listing1 = Role_Listing(10, None, "2023-12-10", "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_null_Date_Closed(self):
        Role_Listing1 = Role_Listing(10, "IT Team", None, "IT Team description is here", "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."

    def test_create_Role_Listing_null_Role_Description(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2023-12-10", None, "IT")
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."
    
    def test_create_Role_Listing_null_Dept(self):
        Role_Listing1 = Role_Listing(10, "IT Team", "2023-12-10", "IT Team description is here", None)
        assert Role_Listing1.create_Role_Listing() == "Error: One or more fields are empty."


