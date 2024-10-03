import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print("13-1. 20203035 KIM김석준")

img = mpimg.imread("C:\Temp/mandrill.png")
print(img)

image_plot = plt.imshow(img)
plt.show()
