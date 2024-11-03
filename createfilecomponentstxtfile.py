import main

mainComponent = main.Main()
with open("./file_components.txt", "w") as file:
    for fileComponent in mainComponent.fileComponents:
        file.write( str( fileComponent ) + "\n" )