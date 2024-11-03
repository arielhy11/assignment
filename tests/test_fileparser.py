import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
from fileparser import FileParser

class TestFileParser( unittest.TestCase ):
    def setUp( self ):
        self.parser = FileParser()
        
    def test_ParseValidFile( self ):
        fileContent = """
        -25°C to 30°C
        5V to 12V
        """
        
        with patch( "builtins.open", mock_open( read_data=fileContent ) ):
            fileComponent = self.parser._FileParser__parseFile( "mocked_file_path" )
            
            self.assertEqual( fileComponent.getTemperatureRange(), ( -25.0, 30.0 ) )
            self.assertEqual( fileComponent.getVoltageRange(), ( 5.0, 12.0 ) )

    def test_FileWithDuplicateMatchingTemperatures( self ):
        fileContent = """
        25°C to 30°C
        Some text
        25°C to 30°C
        5V to 12V
        """
        
        mockFile = mock_open( read_data=fileContent )
        realPath = Path( "dummy_path" )
        
        with patch( 'builtins.open', mockFile ):
            with patch.object( Path, 'stem', return_value="test_file" ):
                fileComponent = self.parser._FileParser__parseFile( str( realPath ) )
                self.assertEqual( fileComponent.getTemperatureRange(), ( 25.0, 30.0 ) )

    def test_FileWithDuplicateMatchingVoltages(self):
        fileContent = """
        Some text
        5V to 12V
        25°C to 30°C
        5V to 12V
        """

        mockFile = mock_open(read_data=fileContent)
        realPath = Path("dummy_path")

        with patch('builtins.open', mockFile):
            with patch.object(Path, 'stem', return_value="test_file"):
                fileComponent = self.parser._FileParser__parseFile(str(realPath))
                self.assertEqual( fileComponent.getVoltageRange(), ( 5.0, 12.0 ) )

    def test_FileWithDuplicateMismatchingTemperatures( self ):
        fileContent = """
        25°C to 30°C
        Some text
        20°C to 35°C
        """
        
        mockFile = mock_open( read_data=fileContent )
        realPath = Path( "dummy_path" )
        
        with patch( 'builtins.open', mockFile ):
            with patch.object( Path, 'stem', return_value="test_file" ):
                fileComponent = self.parser._FileParser__parseFile( str( realPath ) )
                self.assertEqual( fileComponent.getTemperatureRange(), ( None, None ) )

    def test_FileWithDuplicateMismatchingVoltages(self):
        fileContent = """
        Some text
        5V to 12V
        25°C to 30°C
        5V to 13V
        """

        mockFile = mock_open(read_data=fileContent)
        realPath = Path("dummy_path")

        with patch('builtins.open', mockFile):
            with patch.object(Path, 'stem', return_value="test_file"):
                fileComponent = self.parser._FileParser__parseFile(str(realPath))
                self.assertEqual( fileComponent.getVoltageRange(), ( None, None ) )

    def test_FileWithoutTemperature( self ):
        fileContent = """
        Some text
        5V to 12V
        """
        
        mockFile = mock_open( read_data=fileContent )
        realPath = Path( "dummy_path" )
        
        with patch( 'builtins.open', mockFile ):
            with patch.object( Path, 'stem', return_value="test_file" ):
                fileComponent = self.parser._FileParser__parseFile( str( realPath ) )
                self.assertEqual( fileComponent.getTemperatureRange(), ( None, None ) )

    def test_FileWithoutVoltage( self ):
        fileContent = """
        Some text
        25°C to 30°C
        """
        
        mockFile = mock_open( read_data=fileContent )
        realPath = Path( "dummy_path" )
        
        with patch('builtins.open', mockFile):
            with patch.object(Path, 'stem', return_value="test_file"):
                fileComponent = self.parser._FileParser__parseFile(str(realPath))
                self.assertEqual(fileComponent.getVoltageRange(), (None, None))

    def test_FileWithDuplicateMismatchingVoltagesInSameLine(self):
        fileContent = """
        6V to 12V 5V to 13V
        25°C to 30°C
        """

        mockFile = mock_open(read_data=fileContent)
        realPath = Path("dummy_path")

        with patch('builtins.open', mockFile):
            with patch.object(Path, 'stem', return_value="test_file"):
                fileComponent = self.parser._FileParser__parseFile(str(realPath))
                self.assertEqual(fileComponent.getVoltageRange(), (None, None))

    def test_FileWithDuplicateMismatchingTemperaturesInSameLine(self):
        fileContent = """
        25°C to 30°C 20°C to 35°C
        Some text
        """

        mockFile = mock_open(read_data=fileContent)
        realPath = Path("dummy_path")

        with patch('builtins.open', mockFile):
            with patch.object(Path, 'stem', return_value="test_file"):
                fileComponent = self.parser._FileParser__parseFile(str(realPath))
                self.assertEqual(fileComponent.getTemperatureRange(), (None, None))

if __name__ == '__main__':
    unittest.main()