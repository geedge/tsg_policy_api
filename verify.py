#!/usr/bin/python3
# coding=utf-8
import time
import requests
import json
import subprocess
import createIpObject
import createFqdnObject
import createFlagObject
import createRule

class Verify():
    def __init__(self):
        self.password = ""
        self.token = ""
        self.test_pc_ip = ""
    
    def startVerify(self, user, password):
        self.encryptPwd(password)
        self.login(user)    
        # action_list中罗列全部组合，按行读取，每读取一行就执行一次验证
        with open("D:/Document/Project-TSG/Feature/Func-TestSecurityAction/action_list.txt") as f:
            line = f.readline()
            while line:
                print(line)
                # line = f.readline()
                list_temp = line.split(",")
                flag = 0
                if len(list_temp[1]) != 0 and flag == 0:
                    self.test_pc_ip = list_temp[1]
                    flag += 1
                elif len(list_temp[7]) != 0 and flag == 0:
                    self.test_pc_ip = list_temp[7]
                    flag += 1
                self.dispatchConfig(list_temp)
                self.verifyResult()
                
    def encryptPwd(self, pwd):
        url = "http://192.168.44.72/v1/user/encryptpwd"
        pwJson = {"password": ""}
        pwJson["password"] = pwd
        response = requests.get(url, params=pwJson)
        data = json.loads(response.text)
        self.password = data["data"]["encryptpwd"]

    def login(self, user):
        url = "http://192.168.44.72/v1/user/login"
        loginJson = {"username": "", "password": ""}
        loginJson["username"] = user
        loginJson["password"] = self.password
        response = requests.post(url, params=loginJson)
        jsonData = json.loads(response.text)
        self.token = jsonData["data"]["token"]

    def dispatchConfig(self, configure):
        # 按顺序进行拆分action_1st, ip_1st, app_1st, sni_1st, flag_stage0_1st, flag_later_1st, action_2nd, ip_2nd, app_2nd, sni_2nd, flag_stage0_2nd, flag_later_2nd
        # 创建第一条rule
        if len(configure[1]) != 0:
            ipObject_1 = createIpObject.CreateIpObject(self.token, configure[1])
            ipInfo_1 = ipObject_1.createIp()
        else:
            ipInfo_1 = ""
        if len(configure[2]) != 0:
            fqdnObject_1 = createFqdnObject.CreateFqdnObject(self.token, configure[2], configure[3])
            fqdnInfo_1 = fqdnObject_1.createFqdn()
        else:
            fqdnInfo_1 = ""
        if len(configure[4]) != 0:
            flagObject_1 = createFlagObject.CreateFlagObject(self.token, configure[4])
            flagInfo_1 = flagObject_1.createFlag()
        else:
            flagInfo_1 = ""
        rule_1 = createRule.CreateSecurityRule(self.token, ipInfo_1, fqdnInfo_1, flagInfo_1)
        rule_1.createRule()
        time.sleep(3)
        # 创建第二条rule
        if len(configure[7]) != 0:
            ipObject_2 = createIpObject.CreateIpObject(self.token, configure[7])
            ipInfo_2 = ipObject_2.createIp()
        else:
            ipInfo_2 = ""
        if len(configure[8]) != 0:
            fqdnObject_2 = createFqdnObject.CreateFqdnObject(self.token, configure[8], configure[9])
            fqdnInfo_2 = fqdnObject_2.createFqdn()
        else:
            fqdnInfo_2 = ""
        if len(configure[10]) != 0:
            flagObject_2 = createFlagObject.CreateFlagObject(self.token, configure[10])
            flagInfo_2 = flagObject_2.createFlag()
        else:
            flagInfo_2 = ""
        rule_2 = createRule.CreateSecurityRule(self.token, ipInfo_2, fqdnInfo_2, flagInfo_2)
        rule_2.createRule()
        time.sleep(3)
    
    def verifyResult(self):
        # 触发流量
        subprocess.Popen("curl www.baidu.com", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 验证结果
        print(1111111)

if __name__ == "__main__":
    verifyRes = Verify()
    verifyRes.startVerify("zhaokun", "zhaokun1")