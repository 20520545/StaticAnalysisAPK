def extract_all_providers(manifest_path):
    providers = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<provider" in line:
                    parts = line.split(" ")
                    for obj in parts:
                        if("android:name=" in obj):
                            providers.append(obj.split("\"")[1])
                            
            manifest_file.close()
        return providers
    except Exception as e:
        print(f"Error extracting providers: {e}")
        return 1