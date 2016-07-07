from unittest import TestCase
from src.accounting import timecard


class TestTimeCard(TestCase):
    def test_get_tcdate(self):
        tc = timecard.TimeCard('10/10/10','0800', '1700')
        test_date = tc.get_tcdate()
        self.assertTrue(test_date)

    def test_calculate_daily_pay(self):
        tc = timecard.TimeCard('10/10/10', '0800', '1600')
        test_pay = tc.calculate_daily_pay('25.25')
        self.assertEqual(test_pay, 202)

    def test_set_end_time(self):
        tc = timecard.TimeCard('10/10/10', '0800', '')
        tc.set_end_time('1500')
        self.assertEqual(tc.end_time, '1500')
