from typing import Tuple
from components.temperaturerange import TemperatureRange
from components.voltagerange import VoltageRange


class FileComponent:
    def __init__( self ) -> None:
        self.__name: str = ""
        self.__operatingTemperatureRange = TemperatureRange()
        self.__operatingVoltageRange = VoltageRange()

    def getName( self ) -> str:
        return self.__name

    def setName( self, name: str ) -> None:
        self.__name = name

    def getTemperatureRange( self) -> TemperatureRange:
        return self.__operatingTemperatureRange.getTemperatureRange()

    def setTemperatureRange( self, minimum, maximum ) -> None:
        self.__operatingTemperatureRange.setTemperatureRange( minimum, maximum )

    def getVoltageRange( self) -> VoltageRange:
        return self.__operatingVoltageRange.getVoltageRange()

    def setVoltageRange( self, minimum, maximum ) -> None:
        self.__operatingVoltageRange.setVoltageRange( minimum, maximum )

    def __isValid( self ) -> bool:
        return self.getVoltageRange() != ( None, None ) and self.getTemperatureRange() != ( None, None )

    def conditionsMatch( self, temperatureCondition, voltageCondition ) -> bool:
        if not self.__isValid():
            return False
        temperatureRange = self.getTemperatureRange()
        voltageRange = self.getVoltageRange()
        return temperatureRange[ 0 ] < temperatureCondition < temperatureRange[ 1 ] and voltageRange[ 0 ] < voltageCondition < voltageRange[ 1 ]

    def __str__( self ) -> str:
        return (
            f"FileComponent(Name: {self.__name}, "
            f"TemperatureRange: {self.getTemperatureRange()}, "
            f"VoltageRange: {self.getVoltageRange()})"
        )
