import os,shutil
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

folderPath = './pics'
croppedFol = './Cropped_faces'
for image in os.listdir(folderPath):
	if os.path.exists(croppedFol):
		shutil.rmtree(croppedFol)
	os.makedirs(croppedFol)
	os.system("python detect.py " + os.path.join(folderPath, image))
	os.system("python spreadsheet.py")
	os.system("python identify.py")
