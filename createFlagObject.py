#!/usr/bin/python3
# coding=utf-8
import time
import requests
import json

class CreateFlagObject():
    def __init__(self, token, flag):
        self.headers = {"token": ""}
        self.headers["token"] = token
        self.flagJson = {
        }
    
    def createFlag(self):
        url = "http://192.168.44.72/v1/policy/object"
        response = requests.post(url, headers=self.headers, params=self.flagJson)
        flagJsonData = json.loads(response.text)
        return flagJsonData

if __name__ == '__main__':
    flagObject = CreateFlagObject()
    time.sleep(3)