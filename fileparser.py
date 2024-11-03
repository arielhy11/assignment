import re
from typing import Optional
from pathlib import Path
import rangepatterns
from components.filecomponent import FileComponent
import config
from components import exceptions


class FileParser:
    def __init__(self):
        self.__temperaturePattern = re.compile( rangepatterns.getTemperaturePatterns() )
        self.__voltagePattern = re.compile( rangepatterns.getVoltagePatterns() )

    def __parseLineForTemperature(self, line: str) -> Optional[ list[ tuple[ float, float ] ] ]:
        line = line.strip()
        matches = self.__temperaturePattern.findall( line )
        if matches:
            return [(float(match[0]), float(match[1])) for match in matches]
        return None

    def __parseLineForVoltage(self, line: str) -> Optional[ list[ tuple[ float, float ] ] ]:
        line = line.strip()
        matches = self.__voltagePattern.findall(line)
        if matches:
            return [(float(match[0]), float(match[1])) for match in matches]
        return None

    def __moreThanOneRangeInALineAndTheyDiffer( self, rangesList: list[ tuple[ float, float ] ] ):
        if not rangesList or len( rangesList ) <= 1:
            return False
        first_range = rangesList[ 0 ]
        for voltage_range in rangesList[ 1: ]:
            if voltage_range != first_range:
                return True
        return False

    def __wasTemperatureFound( self, fileComponent: FileComponent ) -> bool:
        return fileComponent.getTemperatureRange() != ( None, None )

    def __temperatureSearchHandler( self, line: str, fileComponent: FileComponent ) -> None:
        temperatureRanges = self.__parseLineForTemperature( line )
        if not temperatureRanges:
            return
        if self.__moreThanOneRangeInALineAndTheyDiffer( temperatureRanges ):
            raise exceptions.TwoTemperaturesInOneFileThatDoNotMatchException
        temperatureRange = temperatureRanges[ 0 ]
        if temperatureRange and not self.__wasTemperatureFound( fileComponent ):
            fileComponent.setTemperatureRange( temperatureRange[ 0 ], temperatureRange[ 1 ] )
        elif temperatureRange and self.__wasTemperatureFound( fileComponent ):
            if fileComponent.getTemperatureRange() != temperatureRange:
                fileComponent.setTemperatureRange( None, None )
                raise exceptions.TwoTemperaturesInOneFileThatDoNotMatchException
            
    def __wasVoltageFound( self, fileComponent: FileComponent ) -> bool:
        return fileComponent.getVoltageRange() != ( None, None )

    def __voltageSearchHandler( self, line: str, fileComponent: FileComponent ) -> None:
        voltageRanges = self.__parseLineForVoltage( line )
        if not voltageRanges:
            return
        if self.__moreThanOneRangeInALineAndTheyDiffer( voltageRanges ):
            raise exceptions.TwoVoltagesInOneFileThatDoNotMatchException
        voltageRange = voltageRanges[ 0 ]
        if voltageRange and not self.__wasVoltageFound( fileComponent ):
            fileComponent.setVoltageRange( voltageRange[ 0 ], voltageRange[ 1 ] )
        elif voltageRange and self.__wasVoltageFound( fileComponent ):
            if fileComponent.getVoltageRange() != voltageRange:
                fileComponent.setVoltageRange( None, None )
                raise exceptions.TwoVoltagesInOneFileThatDoNotMatchException

    def __checkIfTemperatureOrVoltageNotInFile( self, fileComponent: FileComponent ) -> None:
        if not self.__wasTemperatureFound( fileComponent ):
            raise exceptions.TemperatureNotFoundInFile()
        if not self.__wasVoltageFound( fileComponent ):
            raise exceptions.VoltageNotFoundInFile()

    def __parseFile(self, filePath: str) -> FileComponent:
        fileComponent = FileComponent()
        fileComponent.setName( Path( filePath ).stem )

        with open( filePath, 'r' ) as file:
            for line in file:
                try:
                    self.__temperatureSearchHandler( line, fileComponent )
                except Exception as e:
                    print( f"{e} {filePath}" )  
                    return fileComponent
                try:
                    self.__voltageSearchHandler( line, fileComponent )
                except Exception as e:
                    print( f"{e} {filePath}" )  
                    return fileComponent

        try:
            self.__checkIfTemperatureOrVoltageNotInFile( fileComponent )
        except Exception as e:
            print ( f"{e} {filePath}" )
            return fileComponent

        return fileComponent

    def fileComponentsFromDir(self) -> list[ FileComponent ]:
        fileComponents = []

        filesDirectory = Path( config.FOLDER_OF_RAW_FILES ).resolve()
        for filePath in filesDirectory.glob("*.txt"):
            fileComponent = self.__parseFile( str ( filePath ) )
            print( str( fileComponent ) )
            fileComponents.append( fileComponent )
        return fileComponents
