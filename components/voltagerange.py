class VoltageRange:
    def __init__( self ) -> None:
        self.__minimumVoltage: float = None
        self.__maximumVoltage: float = None

    def setVoltageRange( self, minimum: float, maximum: float ) -> None:
        self.__minimumVoltage = minimum
        self.__maximumVoltage = maximum

    def getVoltageRange( self ) -> tuple[ float, float ]:
        return ( self.__minimumVoltage, self.__maximumVoltage )