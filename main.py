from components.filecomponent import FileComponent
from fileparser import FileParser


class Main:
    def __init__( self ) -> None:
        self.fileComponents = self.__createFileComponentsList()
        self.matchOperatingConditionsToFileComponents( 55, 15 )

    def __createFileComponentsList( self ) -> list[ FileComponent ]:
        return FileParser().fileComponentsFromDir()

    def matchOperatingConditionsToFileComponents( self, temperatureCondition: float, voltageCondition:float ) -> list[ FileComponent ]:
        matchingFileComponents = []
        for fileComponent in self.fileComponents:
            if fileComponent.conditionsMatch( temperatureCondition, voltageCondition ):
                matchingFileComponents.append( fileComponent )
                print( f"{ fileComponent.getName() } matched!" )

if __name__ == '__main__':
    Main()
