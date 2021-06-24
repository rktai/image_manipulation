import os
from PIL import Image

# path
pathIn = "D:\\wd_diana\\mattock\\model\\4_phase2\\rerun_phase1\\rerun_s12_loov\\figures"
pathOut = pathIn + "\\cropped"
if not os.path.exists(pathOut):
        os.makedirs(pathOut)

# Create an Image object from an Image
imageName = "Ecw1_Phase 2, Load-step 83, Load-factor 89.000, Ploads.png"
imageObject = Image.open(pathIn + "\\" + imageName)

# Image info
width, height = imageObject.size

# Crop image portion (reference from top left point)
left = 0.05 * width
top = 0.45 * height
right = 0.95 * width
bottom = 0.65 * height

a = (left, top, right, bottom)
cropped = imageObject.crop(a)

# Display the cropped portion
cropped.show()

#
saveName = "cropped_" + imageName
cropped.save(pathOut + "\\" + saveName)