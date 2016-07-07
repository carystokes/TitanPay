from unittest import TestCase
from src.accounting import hourly_employee


class TestHourlyEmployee(TestCase):
    def test_clockin(self):
        hr_emp = hourly_employee.HourlyEmployee('1', 'Bob', 'Smith', '10.00', '100', 'DD', '12 Z St', 'Ville', 'ST', '00000')
        hr_emp.clockin('10/10/10', '0800')
        tlen = hr_emp.get_timeCard_length()
        self.assertEqual(tlen, 1)

    def test_clockout(self):
        hr_emp = hourly_employee.HourlyEmployee('1', 'Bob', 'Smith', '10.00', '100', 'DD', '12 Z St', 'Ville', 'ST', '00000')
        hr_emp.clockin('10/10/10', '0800')
        hr_emp.clockout('10/10/10', '1600')
        ttime = hr_emp.get_timeCard_end_time()
        self.assertEqual(ttime, '1600')

    def test_calc_pay(self):
        hr_emp = hourly_employee.HourlyEmployee('1', 'Bob', 'Smith', '10.00', '100', 'DD', '12 Z St', 'Ville', 'ST','00000')
        hr_emp.clockin('10/10/10', '0800')
        hr_emp.clockout('10/10/10', '1600')
        output = hr_emp.calc_pay()
        self.assertTrue(output)
