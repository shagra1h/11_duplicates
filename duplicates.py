import os
import os.path


def check_path_exsistence(target_path):
    if os.path.exists(target_path):
        return target_path


def group_files_by_size(dir_name):
    files_grouped_by_size = {}
    for path, dirs, files in os.walk(dir_name):
        for filename in files:
            full_path = os.path.join(path, filename)
            filesize = os.path.getsize(full_path)
            if filesize in files_grouped_by_size:
                files_grouped_by_size[filesize].append(full_path)
            else:
                files_grouped_by_size[filesize] = [full_path]
    return files_grouped_by_size


def count_duplicates(filelist, aim_file):
    duplicates = 1
    for target in filelist:
        if os.path.split(aim_file)[1] == os.path.split(target)[1] and target != aim_file:
            duplicates += 1
    return duplicates

def eliminate_unique_files(files_grouped_by_size):
    amount_of_duplicates = 1
    processed_files = {}
    for filesize, filelist in files_grouped_by_size.items():
        for file1 in filelist:
            amount_of_duplicates = count_duplicates(filelist, file1)
            if amount_of_duplicates != 1:
                if filesize in processed_files:
                    processed_files[filesize].append(file1)
                else:
                    processed_files[filesize] = [file1]
    return processed_files

if __name__ == '__main__':
    while True:
        target_directory = input("Enter directory to find duples: \n")
        if check_path_exsistence(target_directory) is None:
            print("Incorrect path! Try again!")
        else:
            break
    print("Analyzing files... \n")
    files_in_target_dir = group_files_by_size(target_directory)
    files_in_target_dir = eliminate_unique_files(files_in_target_dir)
    if files_in_target_dir:
        for filesize, filelist in files_in_target_dir.items():
            print("Found duplicates, size =", filesize)
            print('\n'.join(filelist), '\n')
    else:
        print("No duplicates found!")
