import sys
import os, time
import cognitive_face as CF
from global_variables import personGroupId
import urllib
import sqlite3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Key = '0b7a1c04ee454103aacf4c1bd9f4d028'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)    

def get_person_id():
    person_id = ''
    extractId = str(sys.argv[1])[4:]
    connect = sqlite3.connect("Face-DataBase.db")
    c = connect.cursor()
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    c.execute(cmd)
    row = c.fetchone()
    person_id = row[2]
    connect.close()
    return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
            print(filename)
            imgurl = urllib.request.pathname2url(os.path.join(imageFolder, filename))
            # print('file:'+imgurl)
            res = CF.face.detect(os.path.join(imageFolder, filename))
            # print(res)
            if len(res) != 1:
                print ("No face detected in image")
            else:
                res = CF.person.add_face(os.path.join(imageFolder, filename), personGroupId, person_id)
                print('detected')
                #print(res)  
            #time.sleep(6)