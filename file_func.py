import os
import pandas as pd
import prettytable


art = """


                    .__                        
 __ __  ______ ____ |  |   ____   ______ ______
|  |  \/  ___// __ \|  | _/ __ \ /  ___//  ___/
|  |  /\___ \\  ___/|  |_\  ___/ \___ \ \___ \ 
|____//____  >\___  >____/\___  >____  >____  >
           \/     \/          \/     \/     \/ 


            
"""


def combine_excel():
	excel_path = input("Absolute path of the excel that would like to combine: ")
	files = os.listdir(excel_path)
	print("The list of file under the directory of " + excel_path + ": ")
	print(files)
	table = prettytable.PrettyTable()
	table.add_column("FileName",files)
	print(table)
	df = pd.DataFrame()
	file_name = input("What would be the name of the combined excel file? ")
	file_name = file_name if (file_name.endswith('.xlsx')) else (file_name + '.xlsx')
	print("The combined excel file name is: " + file_name)
	new_file_name = excel_path + "\\" + file_name
	with pd.ExcelWriter(new_file_name) as writer:
		for file in files:
			if file.endswith('.xlsx'):
				print(f'Working on: {file}')
				file_1 = excel_path + '\\' + f'{file}'
				df = pd.read_excel(file_1)
				df.to_excel(writer, sheet_name=f'{file}', index=False)


def rename_file():
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