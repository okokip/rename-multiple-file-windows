import os
import pandas as pd
import prettytable


if __name__ == '__main__':
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
