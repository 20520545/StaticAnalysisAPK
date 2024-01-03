def extract_all_permissions(manifest_path):
    permissions = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "uses-permission" in line and "android:name" in line:
                    parts = line.split(" ")
                    for i in range(0,5+1):
                        if("android:name" in parts[i]):
                            result= parts[i].split("\"")[1]
                            permissions.append(result)
                            break
            manifest_file.close()
        return set(permissions)
    except Exception as e:
        print(f"Error extracting permissions: {e}")
        return 1