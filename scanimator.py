from PIL import Image

im = Image.open("image.jpeg")
# im.show()

height = 0
width = 0
x = width
y = height
box_width = 1080
box_height = 1920
image_name = "default"
id = "D"

x_c = 0
y_c = 0

while y < im.height:	
	while x < im.width:
		image_name = id + "-X" + str(x_c) + "Y" + str(y_c) + "-" + str(x) + ("_") + str(y) + "-CROP" #generates image name
		box = (x+324, y+576, x+box_width-324, y+box_height-576) #declares box dimensions
       
		region = im.crop(box) 
		if x + box_width < im.width and y + box_height < im.height: #deals with bug - last image is a cropped edge
			#region.rotate(90)
			region.save(image_name + ".jpeg")
		x = x + box_width #moves crop along
		x_c = x_c + 1 #iterates x coordiante
	y = y + box_height #moves y crop
	y_c = y_c + 1 #iterates y coordiniate
	x = 0
	x_c = 0
