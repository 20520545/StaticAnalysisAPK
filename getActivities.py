def extract_all_activities(manifest_path):
    activities = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            for line in manifest_file:
                if "<activity " in line:
                    parts = line.split(" ")
                    for obj in parts:
                        if("android:name=" in obj):
                            activities.append(obj.split("\"")[1])
                            
            manifest_file.close()
        return set(activities)
    except Exception as e:
        print(f"Error extracting activities: {e}")
        return 1
