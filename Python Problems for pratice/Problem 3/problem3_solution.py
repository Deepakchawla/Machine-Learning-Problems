import pickle as pk
import re

# Class AddressBook take the basic user details from the console and save in the python memory as well as in the
# local disk.


class AddressBook:

    # addressbookdata is a dictionary varibale which holds the all details of user.
    addressbookdata = {"fname":{}, "lname":{}, "streetaddress":{}, "city":{}, "state": {}, "country":{}, "emailaddress":[], "addressdata":{}}

    # Function __init__() or constructor call the specific function according to the user's choice.
    def __init__(self, choice):
        while 1:
            if choice == 1:
                self.addtoaddressbook()
                break
            elif choice == 6:
                print("You are exit from the program.")
                exit()
            else:
                try:
                    pickle_in = open("problem3_data_file1.pickle", "rb+")
                    self.addressbookdata.update(pk.load(pickle_in))
                    pickle_in.close()
                    if choice == 2:
                        while 1:
                            try:
                                fieldname = input("Enter First Name: ")
                                print("Number of occurrences of a First Name is " + str(
                                    self.addressbookdata['fname'][self.createuniquekey(fieldname)][1]))
                                break
                            except KeyError:
                                print("Entered First Name is entered is not available in our database.")
                                continue
                            except FileNotFoundError:
                                print("Currently database is empty.")
                                break
                        break
                    elif choice == 3:
                        while 1:
                            fieldname = input("Enter Last Name: ")
                            try:
                                print("Number of occurrences of a Last Name is " + str(
                                    self.addressbookdata['lname'][self.createuniquekey(fieldname)][1]))
                                break
                            except KeyError:
                                print("Entered Last Name is entered is not available in our database.")
                                continue
                            except FileNotFoundError:
                                print("Currently database is empty.")
                                break
                        break
                    elif choice == 4:
                        while 1:
                            fieldname = input("Enter Street address: ")
                            try:
                                print("Number of occurrences of a Street address is " + str(
                                    self.addressbookdata['streetaddress'][self.createuniquekey(fieldname)][1]))
                                break
                            except KeyError:
                                print("Entered Street address is entered is not available in our database.")
                                continue
                            except FileNotFoundError:
                                print("Currently database is empty.")
                                break
                        break
                    elif choice == 5:
                        fieldname = input("Enter First Name, Last Name, Street address (should be comma (,) separated.): ")
                        fieldname = fieldname.split(',')
                        if self.createuniquekey(fieldname[0].strip()) not in self.addressbookdata['fname']:
                            print("Entered First Name is not in our database.")
                        else:
                            print("Number of occurrences of a First Name is " + str(
                                self.addressbookdata['fname'][self.createuniquekey(fieldname[0].strip())][1]))
                        if self.createuniquekey(fieldname[1].strip()) not in self.addressbookdata['lname']:
                            print("Entered Last Name is not in our database.")
                        else:
                            print("Number of occurrences of a Last Name is " + str(
                                self.addressbookdata['lname'][self.createuniquekey(fieldname[1].strip())][1]))

                        if self.createuniquekey(fieldname[2].strip()) not in self.addressbookdata['streetaddress']:
                            print("Entered Street Address is not in our database.")
                        else:
                            print("Number of occurrences of a Street Address is " + str(
                                self.addressbookdata['streetaddress'][self.createuniquekey(fieldname[2].strip())][1]))
                        break
                except EOFError:
                    break
                except FileNotFoundError:
                    print("Currently database is empty.Please chose option 1 to use this options.")
                    break

    # Function addtoaddressbook is takes the input from the user console then validate it fields then save in the disk.
    def addtoaddressbook(self):
        self.fname = input("First Name: ")
        # First Name validations.
        while not self.fieldnamevalidations(self.fname):
            self.fname = input("First Name: ")
        self.lname = input("Last Name: ")
        # Last Name validations.
        while not self.fieldnamevalidations(self.lname):
            self.lname = input("Last Name: ")
        self.streetaddress = input("Street Address: ")
        self.city = input("City: ")
        # City validations.
        while not self.fieldnamevalidations(self.city):
            self.city = input("City: ")
        self.state = input("State: ")
        # State validations.
        while not self.fieldnamevalidations(self.state):
            self.state = input("State: ")
        self.country = input("Country: ")
        # Country validations.
        while not self.fieldnamevalidations(self.country):
            self.country = input("Country: ")
        while 1:
            self.email = input("Email Address: ")
            # Function emailvalidate() for Email validations.
            while not self.emailvalidate(self.email):
                print("Please entered valid email address.")
                self.email = input("Email Address: ")
            if self.email in self.addressbookdata['emailaddress']:
                print("Email Address should be unique.")
                continue
            else:
                self.addressbookdata['emailaddress'].append(self.email)
                break
        while 1:
            self.mobilenumber = input("Mobile Number: ")
            if self.mobilenumber.isnumeric() and len(self.mobilenumber) == 10:
                if self.mobilenumber in self.addressbookdata['addressdata']:
                    print("Mobile Number should be unique.")
                    continue
                else:
                    break
            else:
                print("Please entered only numbers and length must be 10.")
                continue
        # Save entered data into the disk in .pickle file format.
        self.writetofile()

    # Function fieldnamevalidations() validate the fields name like user name, city, state,etc
    def fieldnamevalidations(self, name):
        if not name.isalpha():
            print("Please entered only alphabets.")
            return False
        return True

    # Function emailvalidate() validate the email address of the user.
    def emailvalidate(self, email):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        return False

    # Function writetofile() save the data in the disk and increase the a counter for the same field.
    def writetofile(self):
        if self.createuniquekey(self.fname) not in self.addressbookdata['fname']:
            self.addressbookdata['fname'].update({self.createuniquekey(self.fname): [self.fname, 1]})
        else:
            tempvalue =  self.addressbookdata['fname'][self.createuniquekey(self.fname)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['fname'].update({self.createuniquekey(self.fname): [self.fname, tempvalue]})

        if self.createuniquekey(self.lname) not in self.addressbookdata['lname']:
            self.addressbookdata['lname'].update({self.createuniquekey(self.lname): [self.lname, 1]})
        else:
            tempvalue =  self.addressbookdata['lname'][self.createuniquekey(self.lname)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['lname'].update({self.createuniquekey(self.lname): [self.lname, tempvalue]})

        if self.createuniquekey(self.streetaddress) not in self.addressbookdata['streetaddress']:
            self.addressbookdata['streetaddress'].update({self.createuniquekey(self.streetaddress): [self.streetaddress, 1]})
        else:
            tempvalue =  self.addressbookdata['streetaddress'][self.createuniquekey(self.streetaddress)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['streetaddress'].update({self.createuniquekey(self.streetaddress): [self.streetaddress, tempvalue]})

        if self.createuniquekey(self.city) not in self.addressbookdata['city']:
            self.addressbookdata['city'].update({self.createuniquekey(self.city): [self.city, 1]})
        else:
            tempvalue =  self.addressbookdata['city'][self.createuniquekey(self.city)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['city'].update({self.createuniquekey(self.city): [self.city, tempvalue]})

        if self.createuniquekey(self.state) not in self.addressbookdata['state']:
            self.addressbookdata['state'].update({self.createuniquekey(self.state): [self.state, 1]})
        else:
            tempvalue = self.addressbookdata['state'][self.createuniquekey(self.state)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['state'].update({self.createuniquekey(self.state): [self.state, tempvalue]})

        if self.createuniquekey(self.country) not in self.addressbookdata['country']:
            self.addressbookdata['country'].update({self.createuniquekey(self.country): [self.country, 1]})
        else:
            tempvalue =  self.addressbookdata['country'][self.createuniquekey(self.country)][1]
            tempvalue = tempvalue + 1
            self.addressbookdata['country'].update({self.createuniquekey(self.country): [self.country, tempvalue]})

        self.addressbookdata['addressdata'].update({self.mobilenumber: {"fname": self.createuniquekey(self.fname), "lname": self.createuniquekey(self.lname),
            "streestaddress": self.createuniquekey(self.streetaddress),"city": self.createuniquekey(self.city),"state": self.createuniquekey(self.state),
                "country": self.createuniquekey(self.country)}})

        pickle_out = open("problem3_data_file1.pickle", "ab+")
        pk.dump(self.addressbookdata, pickle_out)
        pickle_out.close()
        print("Your entered details has been saved successfully.")

    # Funtion createuniquekey() create a unique key for the different fields.
    def createuniquekey(self, value):
        return value + '_' + str(ord(value[0]))


print("""This is the small program which save your basic details in our address book and perform below functionality.
1.Want to add details in the address book.
2.Find number of occurrences of a First Name.
3.Find number of occurrences of a Last Name.
4.Find number of occurrences of a Street.
5.Find number of occurrences of First Name, Last Name and Street.
6.Exit from the program.""")

while 1:
    try:
        choice = input("Your choice number:- ")
        AddressBook(int(choice))
    except ValueError:
            print("Please enter valid choice.")
