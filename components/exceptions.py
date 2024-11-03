class TwoTemperaturesInOneFileThatDoNotMatchException( Exception ):
    def __init__(self, message = "Two non-matching temperature ranges found in the file" ):
        super().__init__()

class TwoVoltagesInOneFileThatDoNotMatchException( Exception ):
    def __init__(self, message = "Two non-matching voltage ranges found in the file" ):
        super().__init__()

class TemperatureNotFoundInFile( Exception ):
    def __init__(self, message = "No temperature found in file" ):
        super().__init__( message )

class VoltageNotFoundInFile( Exception ):
    def __init__(self, message = "No voltage found in file" ):
        super().__init__( message )