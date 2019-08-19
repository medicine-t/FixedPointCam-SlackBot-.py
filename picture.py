import time
from datetime import datetime
import picamera
import requests
import HTU21DF
import os


with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    
    #Camera warm-up time
    time.sleep(2)
    filename = datetime.now().strftime('%Y%m%d%H%M%S')
    camera.capture('picture.jpg')
    token = 'YOURTOKEN'
 
    channel = 'BOTCHANNNELID'
    
    filename = 'picture.jpg'
    
    HTU21DF.htu_reset
    temperature = HTU21DF.read_temperature()
    temperature = round(temperature,2)
    humidity = HTU21DF.read_humidity()
    humidity = round(humidity,2)

    comment = str(temperature) + "degC\n" + str(humidity) + "%"
    files = {'file': open(file, 'rb')}
    param = {
        'token': token,
        'channels': channel,
        'filename': filename,
       
        'initial_comment': comment,
       
        'title': "SlackBot"
    }
 
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
    os.remove("picture.jpg")
    
