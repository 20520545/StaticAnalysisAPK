import os

def listFiles(output_folder):
    decoded_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(output_folder) for f in filenames]
    return decoded_files

