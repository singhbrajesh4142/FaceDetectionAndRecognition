import cognitive_face as CF
from global_variables import personGroupId
import os, urllib
import sqlite3
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



currentDate = time.strftime("%d_%m_%y")
			
			
Key = '0b7a1c04ee454103aacf4c1bd9f4d028'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
connect = sqlite3.connect("Face-DataBase.db")
c = connect.cursor()

	

currentDir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(currentDir, 'Cropped_faces')
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		imgurl = urllib.request.pathname2url(os.path.join(directory, filename))
		res = CF.face.detect(os.path.join(directory, filename))
		if len(res) != 1:
			print("No face detected.")
			continue
			
		faceIds = []
		for face in res:
			faceIds.append(face['faceId'])
		res = CF.face.identify(faceIds, personGroupId)
		for face in res:
			personId = face['candidates'][0]['personId']
			c.execute("SELECT * FROM Students WHERE personID = ?", (personId,))
			row = c.fetchall()				
			if len(row)==0:
				print("Unknown person", end = ' ')
				print(" in " + filename)
			else:
				personId = face['candidates'][0]['personId']
				c.execute("SELECT * FROM Students WHERE personID = ?", (personId,))
				row = c.fetchone()
				print(row[1] + " recognized", end = ' ')
				print(" in " + filename)
		
