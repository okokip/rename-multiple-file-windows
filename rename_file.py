import os

if __name__ == '__main__':
    file_path = input("Absolute path of the files that would like to rename: ")
    files = os.listdir(file_path)
    count = 0
    for f in files:
        if f.endswith('.xlsx'):
            print(f"Going to rename the file: {f}")
            abs_file_path = file_path + '\\' + f
            new_abs_file_name = file_path + '\\' + str(count) + "-renamed.xlsx"
            os.rename(abs_file_path,new_abs_file_name)
            count += 1
    print('All excel files has been Renamed!')
