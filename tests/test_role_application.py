import unittest
from datetime import date

from backend.app import Role_Application

class TestRoleApplication(unittest.TestCase):

    # checks that role application is created into database correctly, queried, and then deleted
    def test_create_Role_Application(self):
        Role_Application1 = Role_Application(1, 1)
        assert Role_Application.create_role_application(self,Role_Application1.Role_Listing_ID, Role_Application1.Staff_ID) == "Role Application was created successfully!"
        assert Role_Application1.delete_role_application() == True
    
    def test_create_Role_Application_reject_no_active_role_listing(self):
        Role_Application2 = Role_Application(2,1)
        assert Role_Application.create_role_application(self, Role_Application2.Role_Listing_ID, Role_Application2.Staff_ID) == "Error: Role Listing ID does not exist or is closed."

    def test_create_Role_Application_reject_no_staff_ID(self):
        Role_Application3 = Role_Application(1,999)
        assert Role_Application.create_role_application(self, Role_Application3.Role_Listing_ID, Role_Application3.Staff_ID) == "Error: Staff ID does not exist."

    def test_create_Role_Application_reject_duplicate(self):
        Role_Application4 = Role_Application(1,1)
        assert Role_Application.create_role_application(self, Role_Application4.Role_Listing_ID, Role_Application4.Staff_ID) == "Role Application was created successfully!"
        Role_Application5 = Role_Application(1,1)
        assert Role_Application.create_role_application(self, Role_Application5.Role_Listing_ID, Role_Application5.Staff_ID) == "Error: Role Application already exists."
        assert Role_Application4.delete_role_application() == True

    # def test_create_Role_Application_empty_Role_Listing_ID(self):
    #     Role_Application6 = Role_Application("",1)
    #     assert Role_Application6.create_role_application() == "Error: One or more fields are empty."

    # def test_create_Role_Application_empty_Staff_ID(self):
    #     Role_Application7 = Role_Application(1,"")
    #     assert Role_Application7.create_role_application() == "Error: One or more fields are empty."

    # def test_create_Role_Application_null_Role_Listing_ID(self):
    #     Role_Application8 = Role_Application(None,1)
    #     assert Role_Application8.create_role_application() == "Error: One or more fields are empty."

    # def test_create_Role_Application_null_Staff_ID(self):
    #     Role_Application9 = Role_Application(1,None)
    #     assert Role_Application9.create_role_application() == "Error: One or more fields are empty."

    