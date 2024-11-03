from fileparser import FileParser
import unittest
import re

class TestRangePatterns( unittest.TestCase ):

	def testTemperaturePatterns( self ):
		validTemperatures = [
			"agkj 25 °C to 30 °C",
			"20 C to 25 C ",
			"25 °C to 30 °C",
			"+ 25 °C to +30 °Cfad"
		]

		for temp in validTemperatures:
			with self.subTest( temp = temp ):
				print( temp )
				self.assertIsNotNone(FileParser()._FileParser__parseLineForTemperature(temp))
		
		invalidTemperatures = [
			"- °C to + 105 °C",
			"25° to 30 °C",
			"C to 30 °C",
			"° C to 30 °C",
			"25 °Cto 30 °C",
			"25 C to30 C"
		]

		for temp in invalidTemperatures:
			with self.subTest( temp = temp ):
				self.assertIsNone(FileParser()._FileParser__parseLineForTemperature(temp))

	def testVoltagePatterns( self ):
		# Valid voltage range patterns
		validVoltages = [
			"5 V to 12 V",
			" 5 V to 12 V ",
			"0.5 V to 1.5 V",
		]
		for voltage in validVoltages:
			with self.subTest( voltage = voltage ):
				self.assertIsNotNone(FileParser()._FileParser__parseLineForVoltage(voltage))

		invalidVoltages = [
			"5 to 12 V",
			"5 V to 12",
			"V to 12 V",
			" 5 V to 12"
		]
		for voltage in invalidVoltages:
			with self.subTest( voltage = voltage ):
				self.assertIsNone(FileParser()._FileParser__parseLineForVoltage(voltage))

if __name__ == '__main__':
	unittest.main()
