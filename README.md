# BTA-Texture-Splitter
Splits BTA's old texture sheets into individual images


## Usage
Place texture atlases into the `Input` directory
Then run the `split.py` script (script uses the PIL library make sure you have it installed)
The individual textures will be stored in the `Output` directory

## Configuration
This texture splitter script is setup to be easily configurable each atlas has its own settings file inside of the `Settings` directory
```text
# x_pos,y_pos - texture_name - x_size,y_size
# x_size and y_size each default to 1 when not specified
# all numbers are specified in tiles

6,0 - wasteland
7,0 - geology
8,0 - cactus_bird
0,1 - pool - 2,1
2,1 - courbet - 2,1
```
