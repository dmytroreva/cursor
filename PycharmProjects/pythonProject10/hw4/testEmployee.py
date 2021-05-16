
from employee import Employee
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee('Dmytro', 'Reva', 12345)

    def test_email(self):
        self.assertEqual(self.test_employee.email, 'revadise@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.test_employee.fullname, 'Dmytro Reva')

    def test_apply_raise(self):
        self.test_employee.apply_raise()
        self.assertEqual(self.test_employee.pay, 10200)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock1):
        mock1.name.ok = True
        mock1.name.text = 'Okay = True'
        response = self.test_employee.monthly_schedule('April')
        print(response)

        self.assertEqual(response, 'Okay = True')
        mock1.name.ok = False
        response = self.test_employee.monthly_schedule('April')
        print(response)
        self.assertEqual(response, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()