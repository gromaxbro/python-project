import os
import shutil
print("enter the folder for scan")
pathh = input()

print("enter the folder for dublicate")
move_pathh = input()

files = os.listdir(pathh)

sizee = []
dub = []
pa = pathh+"/"
for size in files:
	file_size = os.path.getsize(pa+size)
	if file_size not in sizee:
		sizee.append(int(file_size))
	else:
		dub.append(int(file_size))
		print("dublicate := ",size," size:",file_size)
		shutil.move(pathh+"/"+size,move_pathh+"/"+size)
