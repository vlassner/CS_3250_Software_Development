'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: The ThermostatTestCase class
'''

import unittest 
from thermostat import Thermostat

class ThermostatTestCase(unittest.TestCase): 

    # TODO #1
    # pre-condition: a thermostat set to 75F
    # post-condition: a thermostat (actually) set to 75F 
    def test_thermostat_set_to_75(self):
        therm = Thermostat(75)
        self.assertEqual(75, therm.set_point)

    # TODO #2
    # pre-condition: a thermostat set to (any) temperature below Thermostat.MIN_SET_POINT
    # post-condition: a thermostat (actually) set to Thermostat.MIN_SET_POINT
    def test_thermostat_set_to_below_min_set_point(self):
        therm = Thermostat(40)
        self.assertEqual(60,therm.set_point)

    # TODO #3
    # pre-condition: a thermostat set to (any) temperature above Thermostat.MAX_SET_POINT
    # post-condition: a thermostat (actually) set to Thermostat.MAX_SET_POINT
    def test_thermostat_set_to_above_max_set_point(self):
        therm = Thermostat(110)
        self.assertEqual(90,therm.set_point)

    # TODO #4
    # pre-conditions: 
    #   * CURRENT_TEMPERATURE set to Thermostat.MIN_SET_POINT + 1
    #   * a thermostat set to Thermostat.MIN_SET_POINT 
    #   * a call to check_temperature
    # post-condition: CURRENT_TEMPERATURE equals to thermostat's set point
    def test_thermostat_temperature_decrease_by_one(self):
        therm  = Thermostat(91)
        therm.check_temperature
        self.assertEqual(90,therm.set_point)

    # TODO #5
    # pre-conditions: 
    #   * CURRENT_TEMPERATURE set to Thermostat.MAX_SET_POINT - 1
    #   * a thermostat set to Thermostat.MAX_SET_POINT 
    #   * a call to check_temperature
    # post-condition: CURRENT_TEMPERATURE equals to thermostat's set point
    def test_thermostat_temperature_increase_by_one(self):
        therm  = Thermostat(59)
        therm.check_temperature
        self.assertEqual(60,therm.set_point)

    # TODO #6 (+1 bonus)
    # pre-condition: a thermostat set to some (valid) set point value (like 75F) followed by a call to str
    # post-condition: the output from str should be 'Set Point: 75F'
    def test_thermostat_set_to_75_to_check_str(self):
        #therm = Thermostat(75)
        #self.assertEqual('Set Point: 75F', print(str(therm)))
        pass


if __name__ == '__main__':
    unittest.main()
    