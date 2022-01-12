import time
import os
from datetime import datetime

DATA_DIR = "./video_data"

while True:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time}: Container still running")


    files_to_process = [f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))]

    if len(files_to_process) == 0:
        print("Directory is empty. No new files to process.")
    else:
        print("Directory is not empty")

        for file in files_to_process:
            print(file)
            output_filename = f"processed_{now}"
            file_to_process= f"{DATA_DIR}/{file}"
            current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
            command = f"python ./object_tracker.py --video {file_to_process} --output ./outputs/processed_{current_datetime}.avi --model yolov4 --dont_show --info"
            print(command)

            os.system(command)
            os.remove(os.path.join("", file_to_process))

        print("All new files are processed now.")
       

    
    time.sleep(60)
