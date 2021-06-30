import os
from PIL import Image

# path
pathIn = "D:\\wd_diana\\mattock\\model\\4_phase2\\analysis15\\figures"
pathOut = pathIn + "\\cropped"
if not os.path.exists(pathOut):
        os.makedirs(pathOut)

# Create an Image object from an Image
# s10 228/225/211
# s11 194/203/161
# s12 195/192/160

fileIn = "Exx_rebarno2_Phase 2, Load-step 201, Load-factor 148.00, Ploads.png"
imageObject = Image.open(pathIn + "\\" + fileIn)

# Image info
width, height = imageObject.size

# Crop image portion (reference from top left point)
# left = 0.065 * width
# right = 0.95 * width
# top = 0.45 * height
# bottom = 0.68 * height

# left = 255
# right = 1385
# top = 270
# bottom = 380

left = 230
right = 1400
top = 270
bottom = 380


crop_settings = (left, top, right, bottom)
cropped = imageObject.crop(crop_settings)

# Display the cropped portion
# cropped.show()

#
fileOut = "cropped_" + fileIn
cropped.save(pathOut + "\\" + fileOut)