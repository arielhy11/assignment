class TemperatureRange:
    def __init__( self ) -> None:
        self.__minimumTemperature: float = None
        self.__maximumTemperature: float = None

    def setTemperatureRange( self, minimum: float, maximum: float ) -> None:
        self.__minimumTemperature = minimum
        self.__maximumTemperature = maximum

    def getTemperatureRange( self ) -> tuple[ float, float ]:
        return ( self.__minimumTemperature, self.__maximumTemperature )