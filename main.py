import os
import pandas as pd
import prettytable
import file_func


list_of_function = [
    {'index': 1, 'Name': 'Rename Files', 'Function': file_func.rename_file},
    {'index': 2, 'Name': 'Combine Excel', 'Function': file_func.combine_excel}
    ]


if __name__ == '__main__':
    print(file_func.art)
    print("Welcome to the windows little tools!")
    for i in range(0,len(list_of_function)):
        print(str(list_of_function[i]['index']) + ': ' + list_of_function[i]['Name'])
    corr_input = False
    while not corr_input:
        user_input = input("Please enter the function index to call: ")
        if user_input.isnumeric() and int(user_input)<2 :
            user_input = int(user_input)
            list_of_function[user_input-1]['Function']()
            corr_input = True
        
        else:
            print("Invalid input! Please enter the index of the funtion that you would like to execute: ")
