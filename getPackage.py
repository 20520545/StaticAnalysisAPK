def extract_all_packages(manifest_path):
    packages = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<package" in line:
                    obj = line.split("\"")[1]
                    packages.append(obj)
            manifest_file.close()
        return packages
    except Exception as e:
        print(f"Error extracting permissions: {e}")
        return 1