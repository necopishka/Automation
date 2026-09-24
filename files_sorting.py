from pathlib import Path
import shutil


target_dir = Path(input("Input a directory path: "))
if target_dir.exists():                                 #Check the path validation

    if len(list(target_dir.iterdir())) == 0:
        input("The directory is empty. Press enter to exit.")
        exit()


    for file in target_dir.iterdir():
        if file.is_file():
            folder_file_name = file.stem                 #file name before "."
            new_folder_file_name = target_dir / folder_file_name
            new_folder_file_name.mkdir(parents=True, exist_ok=True)
            shutil.move(file, new_folder_file_name)

        else: continue

    print("Done.")
    input("Press enter to exit.")



else:
    print("The path is not valid. Please enter a valid path.")
    input("Press enter to exit.")
    exit()

