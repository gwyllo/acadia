import Image
import os
import os.path
import shutil

folder_path = "drawings"

images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

if not os.path.exists("data/small/"):
	os.makedirs("data/small/")

if not os.path.exists("data/big/"):
	os.makedirs("data/big/")

for image in images:
	old_path = os.path.join(folder_path,image)
	
	img = Image.open(old_path)
	
	if(img.size[0]<200):
		new_path = os.path.join("data/small/",image)
		os.rename(old_path,new_path)
	else:
		print "big" + image
		new_path = os.path.join("data/big/",image)
		os.rename(old_path,new_path)

