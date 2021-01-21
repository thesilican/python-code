import PIL.ImageGrab

top_left = [0, 0]
bottom_right = [100, 511]

img = PIL.ImageGrab.grab(all_screens=True)
img = img.crop(top_left + bottom_right)
img.save("out.png")
