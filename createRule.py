#!/usr/bin/python3
# coding=utf-8
import time
import requests
import json

class CreateSecurityRule():
    def __init__(self, token):
        self.headers = {"token": ""}
        self.headers["token"] = token
        self.ruleJson = {
        }
    
    def createRule(self):
        url = "http://192.168.44.72/v1/policy/object"
        response = requests.post(url, headers=self.headers, params=self.ruleJson)
        ruleJsonData = json.loads(response.text)
        return ruleJsonData

if __name__ == '__main__':
    securityRule = CreateSecurityRule()
    time.sleep(1)