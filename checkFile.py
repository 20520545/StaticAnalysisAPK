import magic
import os
def checkFile(file):
    try:
        if (("zip" in magic.from_file(file)) and (file.endswith(".apk")) and (os.path.exists(file))):
            return False
        return True
    except Exception as e:
        return False