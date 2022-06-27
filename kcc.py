import requests
from requests.structures import CaseInsensitiveDict
import time
import json
import os
letterDic= {'A':0, 'B':1, 'C':2, 'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'a':0, 'b':1, 'c':2, 'd':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
row={'c1':15 ,'c2':10,'c3':15}
def block(_id,seatIds,thetr):
    url = "https://us-central1-kandy-city-centre.cloudfunctions.net/temporaryBookSeats"
    
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
    while 1:
        for seat in seatIds:
          try:
            seat1=str(letterDic[seat[0]]*row[thetr]+int(seat[1:]))
            _captcha =requests.post('https://kcccap.herokuapp.com/kcc.php').text
            data =  '{"data":{"seatIds":['+seat1+'],"scheduleId":"'+_id+'","recaptchaToken":"'+_captcha+'"}}'
            resp = requests.post(url, headers=headers, data=data)
            data1=resp.json()
            print(data1)
          except Exception as e:
            print(data1)
    
            print('error (not booked one) '+str(e))

    '''data1 = '{"data":{"seatIds":[71, 69, 68, 70, 67, 66, 65, 53],"scheduleId":"c1-140422-1000"}}'
    data2 = '{"data":{"seatIds":[71, 69, 68, 70, 67, 66, 65, 53],"scheduleId":"c1-140422-1030"}}'
    while 1:
        #print('type')
        resp = requests.post(url, headers=headers, data=data1)
        resp1 = requests.post(url, headers=headers, data=data2)
        try:
            data=resp.json()
            
            if data['result']['type']=="success":
                print(data['result']['type'])
                time.sleep(600)
            else:
                print(data['result']['type'])
                time.sleep(5)
        except Exception as e:
            print(e)
    '''
    '''seatId=input("enter seat id: ")
    Hall=input("enter hall no: ")
    date=input("enter date 030322: ")
    Time=input("enter time 1030: ")
    data = '{"data":{"seatIds":[41],"scheduleId":"c1-030322-1030"}}' .'''
def getd(_name,_OName,thetr):
  



    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.1.1300830159.1645071118; _ga_0QXKQC7HNM=GS1.1.1649772399.13.1.1649773444.0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'movie': _name,
    }
    while 1:
     try:
      response = requests.get('https://kccmultiplex.lk/buy-tickets/', headers=headers, params=params)
      dic=response.text.split('__NEXT_DATA__" type="application/json">')[1].split('</script>')[0]
      dic=json. loads(dic)
      dic=dic["props"]["pageProps"][ "schedulesStrObjs"]
      for movie in dic:
             movie=json.loads(movie)
             if (movie["movie"]["name"]==_OName) and (movie["cinema"]["id"]==thetr):
                    return movie["id"] 
      print("not found")
     except Exception as e:
            print('error')
seatIds =os.getenv('SEATID').split(',')#
sName=os.getenv('SNAME').strip()
dName=os.getenv('DNAME').strip()
thetr=os.getenv('THETER').strip()
_id=getd(dName,sName,thetr)
print(_id)
block(_id,seatIds,thetr)
