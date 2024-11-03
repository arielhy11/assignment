import main
import unittest
from components.filecomponent import FileComponent


class TestMatchingConditions(unittest.TestCase):
    def setUp( self ):
        fileComponentA = FileComponent()
        fileComponentA.setName( "a" )
        fileComponentA.setTemperatureRange( -10, 10 )
        fileComponentA.setVoltageRange( 60, 120 )

        fileComponentB = FileComponent()
        fileComponentB.setName( "b" )
        fileComponentB.setTemperatureRange( -10, 10 )
        fileComponentB.setVoltageRange( None, None )

        fileComponentC = FileComponent()
        fileComponentC.setName( "c" )
        fileComponentC.setTemperatureRange( 0, 40 )
        fileComponentC.setVoltageRange( 50, 80 )

        self.fileComponents = [ fileComponentA, fileComponentB, fileComponentC]


    def test_match( self ):
        main.Main._Main__createFileComponentsList = lambda _: self.fileComponents
        self.main = main.Main()
        self.main.matchOperatingConditionsToFileComponents( 5, 65 )
