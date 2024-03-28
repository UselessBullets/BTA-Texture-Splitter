import os
import inspect
from PIL import Image

scriptDirectory: str = os.path.dirname(os.path.abspath( 
  inspect.getfile(inspect.currentframe()))) # Directory the script is being run from

inputDirectory: str = scriptDirectory + "\Input" #Here you define your directory path where all the images are located
outputDirectory: str = scriptDirectory + "\Output" #Here you define your directory path where all images will be saved
settingsDirectory: str = scriptDirectory + "\Settings" #Here you define your directory path where settings are saved

os.makedirs(inputDirectory, exist_ok=True)
os.makedirs(outputDirectory, exist_ok=True)
os.makedirs(settingsDirectory, exist_ok=True)

logList = list()

def splitSheet(imageName: str, configLocation: str, outputFolder: str, textureWidthTiles:int ):
    atlas = Image.open(os.path.join(inputDirectory, imageName))

    file = open(settingsDirectory + "/" + configLocation, "r")
    config = file.readlines()
    file.close()

    tileSize = atlas.width / textureWidthTiles

    for line in config:
        try:
          # allow for comments in file
          if (line.lstrip(" ").startswith("#")):
              continue
          split = line.replace("\n", "").split(" - ")

          # skip improperly formatted lines or empty ones
          if (len(split) < 2 or len(line) == 0):
              continue
          
          pos = split[0]
          name = split[1]
          sizeX = 1
          sizeY = 1
          if (len(split) > 2):
              sizeX, sizeY = split[2].split(",")
              sizeX = int(sizeX)
              sizeY = int(sizeY)
          
          x, y = pos.split(",")
          x = int(x)
          y = int(y)
          cropped = atlas.crop((x * tileSize, y * tileSize, (x + sizeX) * tileSize, (y + sizeY) * tileSize))
          saveLocation= os.path.join(outputDirectory, outputFolder + "/{:03}.png")
          os.makedirs(outputDirectory + "/" + outputFolder, exist_ok=True)
          cropped.save(saveLocation.format(name))
          print("image saved to " + saveLocation.format(name))
        except:
            val = "Failed to process line '" + line + "' skipping!"
            print(val)
            logList.append(val)

splitSheet("terrain.png", "blocks.txt", "block", 32)
splitSheet("items.png", "items.txt", "item", 32)
splitSheet("particles.png", "particles.txt", "particle", 16)
splitSheet("kz.png", "paintings.txt", "art", 32)
splitSheet("icons.png", "icons.txt", "icons", 256)

for line in logList:
    print(line)