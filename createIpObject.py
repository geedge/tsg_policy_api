#!/usr/bin/python3
# coding=utf-8
import time
import requests
import json

class CreateIpObject():
    def __init__(self, token, ip):
        # self.headers = {"token": ""}
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded', 'token': token}
        self.headers["token"] = token
        self.ipJson = {
            "opAction": "add",
            "returnData": 1,
            "objectList": [
                {
                    "isExclusion": 0,
                    "objectId": "",
                    "objectName": "test",
                    "objectType": "ip",
                    "objectSubType": "endpoint",
                    "iconColor": "",
                    "objectDesc": "",
                    "subObjectList": [],
                    "SubObjectID": [],
                    "memberType": 1,
                    "addItemList": [
                        {
                            "ip": "1.1.1.1",
                            "port": "0-65535",
                            "isSession": "endpoint",
                            "errInfos": [],
                            "ip1": "1.1.1.1",
                            "ip2": "1.1.1.1",
                            "ipFormat": "range",
                            "addrType": 4,
                            "line": 0
                        }
                    ],
                    "updateItemList": [],
                    "deleteItemIds": []
                }
            ],
            "vsysId": 1
        }
    
    def createIp(self):
        url = "http://192.168.44.72/v1/policy/object"
        response = requests.post(url, headers=self.headers, params=self.ipJson)
        ipJsonData = json.loads(response.text)
        return ipJsonData

if __name__ == '__main__':
    ipObject = CreateIpObject()
    time.sleep(3)