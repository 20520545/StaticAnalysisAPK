def extract_all_libraries(manifest_path):
    libraries = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<uses-library" in line:
                    parts = line.split(" ")
                    for obj in parts:
                        if("android:name=" in obj):
                            libraries.append(obj.split("\"")[1])
                            
            manifest_file.close()
        return libraries
    except Exception as e:
        print(f"Error extracting libraries: {e}")
        return 1