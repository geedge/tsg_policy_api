#!/usr/bin/python3
# coding=utf-8
import time
import requests
import json

class CreateFqdnObject():
    def __init__(self, token, fqdn):
        self.headers = {"token": ""}
        self.headers["token"] = token
        self.fqdnJson = {
        }
    
    def createFqdn(self):
        url = "http://192.168.44.72/v1/policy/object"
        response = requests.post(url, headers=self.headers, params=self.fqdnJson)
        fqdnJsonData = json.loads(response.text)
        return fqdnJsonData

if __name__ == '__main__':
    fqdnObject = CreateFqdnObject()
    time.sleep(3)