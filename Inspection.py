

import hashlib
import os
import yaml 
import sys

def sha256(filename):
    h = hashlib.sha256()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def sha1(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':   
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()
def md5(filename):
    h = hashlib.md5()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
    return h.hexdigest()



def DisplayInfo(fileName:str):
    try:
        fileInfo = os.stat(fileName)
        md5sum = md5(fileName)
        sha256sum = sha256(fileName)
        sha1sum = sha1(fileName)
        Info=""
        Info+=('''FILE INFO\n''')
        Info+=(f'[+] File Name: {fileName.split("/")[-1]}\n')
        Info+=(f'[+] Size: {format(fileInfo.st_size / (1024 * 1024), ".2f")} MB\n')
        Info+=(f'[+] MD5: {md5sum}\n')
        Info+=(f'[+] SHA256: {sha256sum}\n')
        Info+=(f'[+] SHA1: {sha1sum}\n')
        filePath= fileName.split("/")[-1].split('.')[0]
        fileNamewithoutExtension= fileName.split('/')[2].split('.')[0]
        with open(f'./{filePath}/{fileNamewithoutExtension}/AndroidManifest.xml', 'r') as file:
            line= file.readline().split(" ")
            for element in line:
                if("package=" in element):
                    Info+= ("[+] Package name: "+element.split("\"")[1]+"\n")
                    break
        prime_service=""
        with open(f'./{filePath}/{fileNamewithoutExtension}/apktool.yml', 'r') as file:
            prime_service = yaml.safe_load(file)
            file.close()
            
        for item, value in prime_service['sdkInfo'].items():
            Info+=(f"[+] {item}: {value}\n")
        return Info
    except Exception as e:
        print(e)
        sys.exit(1)
