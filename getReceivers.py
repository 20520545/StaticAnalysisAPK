def extract_all_receivers(manifest_path):
    receivers = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<receiver" in line:
                    parts = line.split(" ")
                    for obj in parts:
                        if("android:name=" in obj):
                            receivers.append(obj.split("\"")[1])
                            
            manifest_file.close()
        return receivers
    except Exception as e:
        print(f"Error extracting receivers: {e}")
        return 1
