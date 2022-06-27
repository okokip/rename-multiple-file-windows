import os

if __name__ == '__main__':
    file_path = input("Absolute path of the files that would like to rename: ")
    files = os.listdir(file_path)
    count = 0
    invalid_input = True
    print("List of the files in the directory: ")
    print(files)
    while invalid_input:
        num_file = input("Please enter the number of files that you would like to rename? ")
        if (num_file.isalnum and (int(num_file) >0 and int(num_file) <= len(files))):
            num_file = int(num_file)
            for i in range(1,num_file+1):
                old_file_name = input(f'Please enter the {i} file name that you want to rename: ')
                if old_file_name in files:
                    new_file_name = input(f'Please enter the new file name for {old_file_name}: ')
                    print(f"Going to rename the file: {old_file_name}")
                    abs_file_path = file_path + '\\' + old_file_name
                    new_abs_file_name = file_path + '\\' + new_file_name
                    os.rename(abs_file_path,new_abs_file_name)
                    count += 1
            print('All file(s) has been Renamed!')
            invalid_input = False
        else:
            print("invalid input")
            invalid_input = True
    
