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


    