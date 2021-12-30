import os
import fitz
import PySimpleGUI as psg  # for showing progress bar
from frontend import *

doc = fitz.open('all-my-pics-embedded.pdf')  # PDF with the pictures
imgdir = r"img"  # where my files are

imglist = os.listdir(imgdir)  # list of pictures
imgcount = len(imglist)  # pic count
imglist.sort()  # nicely sort them

for i, f in enumerate(imglist):
    img = open(os.path.join(imgdir, f), "rb").read()  # make pic stream
    doc.embfile_add(img, f, filename=f,  # and embed it
                    ufilename=f, desc=f)
    psg.EasyProgressMeter("Embedding Files",  # show our progress
                          i + 1, imgcount)

page = doc.new_page()  # at least 1 page is needed

doc.save("all-my-pics-embedded.pdf")
