import os
import shutil

def split_files(source_folder, folder_a, folder_b):
    # Get the list of files in the source folder
    file_list = os.listdir(source_folder)

    # Sort the files to ensure consistent splitting
    file_list.sort()

    # Calculate the number of files in each half
    total_files = len(file_list)
    half_point = total_files // 2

    # Create new folders if they don't exist
    if not os.path.exists(folder_a):
        os.makedirs(folder_a)
    if not os.path.exists(folder_b):
        os.makedirs(folder_b)

    # Copy files to Folder_A
    for file_name in file_list[:half_point]:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(folder_a, file_name)
        shutil.copy2(source_path, destination_path)

    # Copy files to Folder_B
    for file_name in file_list[half_point:]:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(folder_b, file_name)
        shutil.copy2(source_path, destination_path)

if __name__ == "__main__":
    source_folder = "/content/gdrive/MyDrive/agrisonic/Pest and Disease/train/train/cmd"  # Replace this with the path to the source folder
    folder_a = "/content/gdrive/MyDrive/agrisonic/Pest and Disease/Plant Diseases Dataset/cassava_train/Cassava___cmd"  # Replace this with the path to the new folder A
    folder_b = "/content/gdrive/MyDrive/agrisonic/Pest and Disease/Plant Diseases Dataset/cassava_valid/Cassava___cmd"  # Replace this with the path to the new folder B

    split_files(source_folder, folder_a, folder_b)
    print("Files split and copied successfully.")
