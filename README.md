# APK static analysis

Topic: Analysis APK application using static analysis and create an automatic tool and getting report.

Coding project for Malware Analysis NT137. Taking big inspiration from [AndroPyTool](https://github.com/alexMyG/AndroPyTool) and [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF).

Tools: apktool

### Folder
- sample/: Place your APK file. <APK's name> folder contains components of APK file after extract.
- tool/: contain tools use for analysing
- report/: contain report from the result.

### Installation

```python
pip install -r requirements.txt
``` 

### Usage

```python
__APK Static Analysis Tool__
usage: main.py [-h] -s NAME [-vt VT_API_KEY] [--package] [--permission] [--activity] [--service] [--receiver]
               [--library] [--provider] [--string] [-o OUTPUT]

Analysis an APK file from inspection and analysis. Inspection: Filename; Size; MD5; SHA256; SHA1. Static analysis:
SDKVersionRecommend; Permisssions; Packages; Activities; ...

options:
  -h, --help            show this help message and exit
  -s NAME, --source NAME
                        APK's name
  -vt VT_API_KEY, --virustotal_api_key VT_API_KEY
                        Analyse applications with the VirusTotal service. It must be followed by a VirusTotal API key.
  --package             Dump package visibility being used in APK.
  --permission          Dump permissions being used in APK.
  --activity            Dump activities path being used in APK.
  --service             Dump services being used in APK.
  --receiver            Dump BroadcastReceiver action being used in APK.
  --library             Dump shared libraries being used in APK.
  --provider            Dump content providers being used in APK.
  --string              Dump hard-coded and dumy strings being used in APK.
  -o OUTPUT, --output OUTPUT
                        Write result to file.
```

### Option
- `-s /--source` : File path (must be provided)
- `-vt / --virustotal_api_key <API_KEY>`: Using virusTotal API for getting file scan report. Default: False
- `--package`: Dump package visibility being used in APK. Default: False
- `--permission`: Dump permissions being used in APK. Default: False
- `--activity`: Dump activities path being used in APK. Default: False
- `--service`: Dump services being used in APK. Default: False
- `--receiver`: Dump BroadcastReceiver action being used in APK. Default: False
- `--library`: Dump shared libraries being used in APK. Default: False
- `--provider`: Dump content providers being used in APK. Default: False
- `--string`: Dump hard-coded and dumy strings being used in APK. Default: False
- `-o, --output`: Write result to file. Default: False

### How to use

```python
python main.py -s ./sample/File.apk -s <FILE_PATH> [-vt] [-o <FILE_NAME>] [--package] [--permission] [--activity] [--service] ...
```

### To-do-list

- [ ] Crawl APICalls; Android API and Signer Cert. 
- [ ] Adjustment to run on Linux. Only run on Windows yet

### Demonstration

[Link](https://youtu.be/UAtxa_rqTzU)
