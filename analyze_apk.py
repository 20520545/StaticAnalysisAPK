import os 
import subprocess

def analyze_apk(apk_path, output_folder=""):
    try:
        if (output_folder==""):
            subprocess.run(['.\\tool\\apktool.bat', 'd', apk_path], check=True, input=b'\n')
        else:
            subprocess.run(['.\\tool\\apktool.bat', 'd', apk_path, '-o', output_folder], check=True, input=b'\n')
    except Exception as e:
        print("We encounter some problem while running program")
        print(e)

