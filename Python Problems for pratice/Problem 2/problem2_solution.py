import xlrd
import numpy as np
import pandas as pd
import time
import sys

# Class readwritetoexcel convert the an excel file into multi-dimensional array using numpy.


class readwritetoexcel:

    # Function __init__() or constructor call the specific function according to the user's choice.
    def __init__(self, choice):
        if choice == 1:
            self.readfromfile()
        elif choice == 2:
            print("You are exit from the program.")
            exit()
        else:
            print("Please enter valid choice.")

    # Function readfromfile() take the excel file from the console then convert in to
    # multi-dimensional array using numpy.

    def readfromfile(self):
        while 1:
            filename = input("Enter excel file name with extension (only xlsx format).")
            newfilename = "new" + filename
            try:
                book = xlrd.open_workbook(filename)
                sheetname = book.sheet_names()
                sheet = book.sheet_by_name(sheetname[0])
                # Read the whole an excel data and then save in the self.data variable.
                self.data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
                print("Reading data from the " + filename + " file.")
                # Function loading animation on console.
                self.loading()
                print("Data has been read successfully.")
                print("Now creating multi-dimension array using numpy.")
                # Convert the data excel data in the numpy array.
                self.data = np.array(self.data, dtype=np.int64)
                # Function loading animation on console.
                self.loading()
                print("Array has been created successfully.")
                print(self.data)
                print("Now saving multi-dimension array in the new excel file named as " + newfilename + ".")
                self.writetofile(newfilename)
                # Function loading animation on console.
                self.loading()
                print("New file has been created successfully named as " + newfilename + ".")
                break
            except FileNotFoundError:
                print("Wrong file name or path name.")
                continue

    # Function writetofiel() write the numpy array into an excel file.

    def writetofile(self,filename):
        df = pd.DataFrame (self.data)
        df.to_excel(filename, index=False)

    # Function loading() give loading animation on screen or console.

    def loading(self):
        animation = "|/-\\"

        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()


print("""This is the small program which create multi-dimension array from read data from excel file and back to save to new excel file or exceting file.
1.Want to convert excel file data in mutli-dimension array.
2.Exit from the program.""")

while 1:
    try:
        choice = input("Your choice number:- ")
        readwritetoexcel(int(choice))
    except ValueError:
            print("Please enter valid choice.")
