from pypresence import Presence
import time
import requests
from datetime import datetime

RPC = Presence(939209176180224030,pipe=0) 
RPC.connect() 

while True:
    data = requests.get("https://api.slam.nl/api/getStreams?brand=slam").json()
    now = datetime.now()
    RPC.update(details=f"Time: {now.strftime('%H:%M:%S')} CET (15s check) ", state=f"SLAM is streaming: {data['data']['streams'][0]['metadata']['nowTitle']}, by: {data['data']['streams'][0]['metadata']['nowArtist']}", large_image="logo", large_text="SLAM!")
    time.sleep(15)