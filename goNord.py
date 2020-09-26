#!/usr/bin/env python3

from ImageGoNord import NordPaletteFile, GoNord
import sys, os

def main():
    dirOld = "/home/mir/Pictures/wallhaven/"
    dirNew = "/home/mir/Pictures/newWall/"
    for root, dirs, files in os.walk(dirOld):
        for file in files:
            imagePath = dirOld + file
            name = file.split(".", 1)
            oName = name[0] + "-Nord." + name[1]
            savePath = dirNew + oName

            # E.g. Replace pixel by pixel
            go_nord = GoNord()
            image = go_nord.open_image(imagePath)
            go_nord.convert_image(image, save_path=savePath)
        
            # E.g. Avg algorithm and less colors
            go_nord.enable_avg_algorithm()
            go_nord.reset_palette()
            go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
            go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
        
            # You can add color also by their hex code
            go_nord.add_color_to_palette("#FF0000")
        
            image = go_nord.open_image(imagePath)
            go_nord.convert_image(image, save_path=savePath)
        
            # E.g. Resized img no Avg algorithm and less colors
            go_nord.disable_avg_algorithm()
            go_nord.reset_palette()
            go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
            go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
        
            image = go_nord.open_image(imagePath)
            resized_img = go_nord.resize_image(image)
            go_nord.convert_image(resized_img, save_path=savePath)
        
            # E.g. Quantize
        
            image = go_nord.open_image(imagePath)
            go_nord.reset_palette()
            go_nord.set_default_nord_palette()
            quantize_image = go_nord.quantize_image(image, save_path=savePath)
        
            # To base64
            go_nord.image_to_base64(quantize_image, "jpeg")


if __name__ == "__main__":
    main()
