from unittest import TestCase
from src.accounting import salaried_employee


class TestSalariedEmployee(TestCase):
    def test_create_receipt(self):
        sal_emp = salaried_employee.SalariedEmployee('1', 'Bob', 'Smith', '120000', '10', '100', 'DD', '12 Z St', 'Ville', 'ST', '00000')
        sal_emp.create_receipt('1', 'Smith', 'book', '1', '1000', 1000)
        tlen = sal_emp.get_number_receipts()
        self.assertEqual(tlen, 1)

    def test_calc_pay(self):
        sal_emp = salaried_employee.SalariedEmployee('1', 'Bob', 'Smith', '120000', '10', '100', 'DD', '12 Z St', 'Ville', 'ST', '00000')
        sal_emp.create_receipt('1', 'Smith', 'book', '1', '1000', 1000)
        output = sal_emp.calc_pay()
        self.assertTrue(output)
