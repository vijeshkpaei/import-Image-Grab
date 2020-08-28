
#vijesh
from PIL import Image 
import glob, os
directory = "/home/vijesh/test/"
for infile in glob.glob("*.JPG"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(directory + file + ".png", "PNG")
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(directory + file + ".png", "PNG") 
for infile in glob.glob("*.JPEG"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(directory + file + ".png", "PNG")
for infile in glob.glob("*.jpeg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(directory + file + ".png", "PNG")


#find . -type f -iname \*.jpeg -delete
