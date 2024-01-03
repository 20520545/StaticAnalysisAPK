def extract_all_services(manifest_path):
    services = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<service" in line:
                    parts = line.split(" ")
                    for obj in parts:
                        if("android:name=" in obj):
                            services.append(obj.split("\"")[1])
                            
            manifest_file.close()
        return services
    except Exception as e:
        print(f"Error extracting services: {e}")
        return 1