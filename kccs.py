import requests
from requests.structures import CaseInsensitiveDict
import time
import json
import os
url = "https://us-central1-kandy-city-centre.cloudfunctions.net/temporaryBookSeats"
seatId =os.getenv('SEATID2')
sId=os.getenv('SHID')
headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "en-GB,en;q=0.9,en-US;q=0.8"
headers["Connection"] = "keep-alive"
headers["Content-Length"] = "56"
headers["Content-Type"] = "application/json"
headers["Host"] = "us-central1-kandy-city-centre.cloudfunctions.net"
headers["Origin"] = "https://kccmultiplex.lk"
headers["Referer"] = "https://kccmultiplex.lk/"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "cross-site"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
headers["sec-ch-ua-mobile"] = "?0"

data1 = '{"data":{"seatIds":'+seatId+',"scheduleId":"'+sId+'"}}'

while 1:
    #print('type')
    resp = requests.post(url, headers=headers, data=data1)

    try:
        data=resp.json()
        
        if data['result']['type']=="success":
            print(data['result']['type'])
            time.sleep(600)
        else:
            print(data)
            time.sleep(5)
    except Exception as e:
        print(e)
