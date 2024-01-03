import os

def checkJavaInstall():
    try:
        exit_code = os.system('java -version  > NUL 2>&1')
        if exit_code == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
