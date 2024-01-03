import requests
import json
from Inspection import sha256
import os
import sys

def virusTotal(API_key:str, FILE_PATH: str):
    url = "https://www.virustotal.com/api/v3/files/"

    headers = {
        "accept": "application/json",
        "x-apikey": API_key
    }
    files = {"file": (os.path.basename(FILE_PATH), open(os.path.abspath(FILE_PATH), "rb"))}
    
    file_report= requests.get(url+sha256(FILE_PATH),headers= {'x-apikey':API_key})

    if("NotFound" in file_report.text):
        # Upload file for scanning and get result
        print("[+] Submitting file for scanning...")
        upload_url= requests.get(url+"upload_url", headers= headers)
        upload_url=json.loads(upload_url.text)["data"]
        send= requests.post(upload_url,files= files, headers= headers)
        result= requests.get(json.loads(send.text)["data"]["links"]["self"],headers= headers)
        result= json.loads(result.text)["data"]["links"]["item"]
        result= requests.get(result, headers= headers)
        return result.text

    else:
        # Send available information taken from hash
        return file_report.text
