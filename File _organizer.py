import os
import shutil

source_folder = input("Enter Folder Path: ")

extensions = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3"],
}

for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder,file)

    if os.path.isfile(file_path):

        moved = False

        for folder,exts in extensions.items():

            if any(file.lower().endswith(ext) for ext in exts):

                folder_path = os.path.join(source_folder,folder)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                shutil.move(file_path,os.path.join(folder_path,file))
                print(file,"moved to",folder)

                moved = True
                break

        if moved==False:
            other_folder=os.path.join(source_folder,"Others")

            if not os.path.exists(other_folder):
                os.mkdir(other_folder)

            shutil.move(file_path,os.path.join(other_folder,file))

print("File Organization Completed Successfully")