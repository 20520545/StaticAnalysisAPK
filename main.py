
# Reference: https://github.com/alexMyG/AndroPyTool

import os
import sys
from pprint import pprint
import argparse
from checkFile import checkFile
from checkJava import checkJavaInstall
from Inspection import DisplayInfo
from getPermission import extract_all_permissions
from getPackage import extract_all_packages
from getPermission import extract_all_permissions
from getActivities import extract_all_activities
from getServices import extract_all_services
from getReceivers import extract_all_receivers
from getProviders import extract_all_providers
from getLibraries import extract_all_libraries
from strings import extract_strings
from virusTotal import virusTotal
import analyze_apk

# Inspection
#  Filename, md5, sha256m sha1, label, AVClass; Virustotal reports

# Static analysis
# Package name; system commands; permissions; activities, opcodes; services; Main Activity;
# Receivers; API Calls; Strings

####
Name='''
APK static analysis
20520545
'''

   



if (__name__=="__main__"):
    ## Write system arguements:
    print("__APK Static Analysis Tool__")
    parser = argparse.ArgumentParser(
        description='''
        Analysis an APK file from inspection and analysis.
        Inspection: Filename; Size; MD5; SHA256; SHA1.
        Static analysis: SDKVersionRecommend; Permisssions; Packages; Activities; 

        ...''',

        epilog="[+] Exiting..."
    )
    parser.add_argument('-s','--source',help='APK\'s name',dest='name',required=True)
    parser.add_argument('-vt', '--virustotal_api_key', help='Analyse applications with the VirusTotal service. It must be followed by a VirusTotal API key.',dest='vt_api_key', required=False)
    parser.add_argument('--package', help='Dump package visibility being used in APK.',dest='package',  action='store_true')
    parser.add_argument('--permission', help='Dump permissions being used in APK.',dest='permission',  action='store_true')
    parser.add_argument('--activity', help='Dump activities path being used in APK.',dest='activity',  action='store_true')
    parser.add_argument('--service', help='Dump services being used in APK.',dest='service',  action='store_true')
    parser.add_argument('--receiver', help='Dump BroadcastReceiver action being used in APK.',dest='receiver',  action='store_true')
    parser.add_argument('--library', help='Dump shared libraries being used in APK.',dest='provider',  action='store_true')
    parser.add_argument('--provider', help='Dump content providers being used in APK.',dest='library',  action='store_true')
    parser.add_argument('--string', help='Dump hard-coded and dumy strings being used in APK.',dest='string',  action='store_true')
    parser.add_argument('-o','--output', help='Write result to file.',dest='output')

    
    if len(sys.argv)== 1:
        parser.print_help()
        sys.exit(0)
    args= parser.parse_args()
    fileName= args.name
    permission= args.permission
    activity= args.activity
    service= args.service
    receiver= args.receiver
    provider= args.provider
    library= args.library
    package= args.package
    string= args.string
    output= args.output
    vT= args.vt_api_key

    if (not checkJavaInstall()):  
        print("[+] Java is not installed on the device. Exiting ...")  
        sys.exit(1)
    if (not checkFile(fileName)):
        print("[+] Checking your APK file's name again or it's not even exist. Exiting ...")
        sys.exit(1)


    print("[+] Running with: "+fileName)
    
    fileNamewithoutExtension= "./sample/"+fileName.split('/')[2].split('.')[0]
    filePath= fileName.split('.')[1]
    
    # Check if APK is being analyze
    if(not os.path.isdir(fileNamewithoutExtension)):
        analyze_apk.analyze_apk(fileName,fileNamewithoutExtension) 
    # Basic inspection (always)
    print(DisplayInfo(fileName))

    if(permission):
        print("__APK\'s permission__")
        print(extract_all_permissions(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(package):
        print("__APK\'s package__")
        print(extract_all_packages(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(activity):
        print("__APK\'s activities__")
        print(extract_all_activities(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(service):
        print("__APK\'s services__")
        print(extract_all_services(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(receiver):
        print("__APK\'s receivers__")
        print(extract_all_receivers(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(provider):
        print("__APK\'s providers__")
        print(extract_all_providers(f'{fileNamewithoutExtension}/AndroidManifest.xml'))
    if(library):
        print("__APK\'s libraries__")
        extract_all_libraries(f'{fileNamewithoutExtension}/AndroidManifest.xml')
    if(string):
        print("__APK\'s variables and DUMMY variables__")
        print(extract_strings(f'{fileNamewithoutExtension}/res/values/strings.xml'))
    if (output != None):
        with open("./report/"+output+".txt",'w', encoding="utf-8") as file:
                if(permission):
                    file.write("__APK\'s permission__\n")
                    result= extract_all_permissions(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(package):
                    file.write("__APK\'s package__\n")
                    result= extract_all_packages(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(activity):
                    file.write("__APK\'s activities__\n")
                    result= extract_all_activities(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(service):
                    file.write("__APK\'s services__\n")
                    result= extract_all_services(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(receiver):
                    file.write("__APK\'s receivers__\n")
                    result= extract_all_receivers(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(provider):
                    file.write("__APK\'s providers__\n")
                    result= extract_all_providers(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(library):
                    file.write("__APK\'s libraries__\n")
                    result= extract_all_libraries(f'{fileNamewithoutExtension}/AndroidManifest.xml')
                    for line in result:
                        file.write(line+'\n')
                if(string):
                    file.write("__APK\'s variables and DUMMY variables__\n")
                    result= extract_strings(f'{fileNamewithoutExtension}/res/values/strings.xml')
                    print(result)
                    for key,value in result.items():
                        file.write(f'{key}: {value} \n')
                file.close()
                print("Report write to ./report/"+output+".txt")
    if(vT != None ):
        if( len(vT)!= 64):
            print ('ERROR! - invalid vt_key file. Please, provide a virustotal key!')
            sys.exit(0)
        else:
            vTreport= virusTotal(vT, fileName)
            prompt= input("Do you want to write VirusTotal report to file? Y/N\n")
            if(prompt.upper()== "Y"):
                with open("./report/report.txt","w") as file:
                    for line in vTreport:
                        file.write(line)
                print("VirusTotal report write to ./report/report.txt")
            else:
                print(vTreport)


