import unittest

from backend.app import Staff

class TestStaff(unittest.TestCase):

    # positive test case -> HR and Manager has access, Staff does not have access
    def test_HR_have_access(self):
        Staff1 = Staff(1, "Elijah", "Khor", "HR Team", "HR and Admin", "Singapore", "elijah@email.com", "HR")
        assert Staff1.have_access() == True

    def test_Manager_have_access(self):
        Staff2 = Staff(2, "Raphael", "Goh", "Senior Engineer", "Engineering Operation Division", "Singapore", "raphael@email.com", "Manager")
        assert Staff2.have_access() == True

    def test_Staff_have_access(self):
        Staff3 = Staff(3, "Wei Sheng", "Ang", "Junior Engineer", "Engineering Operation Division", "Singapore", "weisheng@email.com", "Staff")
        assert Staff3.have_access() == False

    # positive test case -> assert True if all fields are not empty, not null and primary key is unique
    # checks that staff is created into database correctly, queried, and then deleted
    def test_create_staff(self):
        Staff5 = Staff(7, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        current_number_of_staff = len(Staff5.retrieve_all_Staff_ID())
        assert Staff5.create_staff() == True
        assert current_number_of_staff+1 == len(Staff5.retrieve_all_Staff_ID())
        assert Staff5.delete_staff() == True

    # negative test case -> assert False if primary key is not unique
    def test_create_staff_negative(self):
        Staff5 = Staff(6, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff5.create_staff() == False

    # negative test case -> assert False for any empty Strings
    def test_create_staff_empty_Staff_ID(self):
        Staff4 = Staff("", "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Staff_FName(self):
        Staff4 = Staff(1, "", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Staff_LName(self):
        Staff4 = Staff(1, "Daryl", "", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Role_Name(self):
        Staff4 = Staff(1, "Daryl", "Teo", "", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Dept(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Country(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Email(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_empty_Access_Rights(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "")
        assert Staff4.create_staff() == False

    # negative test case -> assert False for any Null values
    def test_create_staff_null_Staff_ID(self):
        Staff4 = Staff(None, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Staff_FName(self):
        Staff4 = Staff(1, None, "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Staff_LName(self):
        Staff4 = Staff(1, "Daryl", None, "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Role_Name(self):
        Staff4 = Staff(1, "Daryl", "Teo", None, "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Dept(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", None, "Singapore", "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Country(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", None, "daryl@email.com", "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Email(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", None, "Staff")
        assert Staff4.create_staff() == False

    def test_create_staff_null_Access_Rights(self):
        Staff4 = Staff(1, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", None)
        assert Staff4.create_staff() == False
