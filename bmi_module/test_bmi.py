import unittest
import assesment
import table1

l = [[171, 52], [180, 77], [167, 82], [170, 85], [171, 96], [155, 90], [155, 96]]


class TestBmi(unittest.TestCase):

    count_overweight = 0

    def check(self, bmi_value):        

        if bmi_value<= 18.4:
            self.assertEqual(table1.df['BMI Category'][0], 'Underweight')

        elif 18.5<= bmi_value <= 24.9:
            self.assertEqual(table1.df['BMI Category'][1], 'Normal weight')
            
        elif 25 <= bmi_value <= 29.9:
            self.assertEqual(table1.df['BMI Category'][2], 'Overweight')            

        elif 30 <=bmi_value<= 34.9:
            self.assertEqual(table1.df['BMI Category'][3], 'Moderately obese')

        elif 35<= bmi_value <= 39.9:
            self.assertEqual(table1.df['BMI Category'][4], 'Severely obese')

        elif bmi_value >= 40:
            self.assertEqual(table1.df['BMI Category'][5], 'Very severely obese')

    
    def check_overweight_count(self, bmi_value):
        if 25<= bmi_value <= 29.9:
            self.count_overweight = self.count_overweight+1           
            
    
    def test_bmi(self):
        
        for height, weight in l:
            bmi_value = assesment.calc_bmi(height, weight)
            self.check(bmi_value)


    def test_countOverweight(self):

        for height, weight in l:
            bmi = assesment.calc_bmi(height, weight)
            self.check_overweight_count(bmi)
        
        self.assertEqual(self.count_overweight, 2)         

   
if __name__ == '__main__':
    unittest.main()