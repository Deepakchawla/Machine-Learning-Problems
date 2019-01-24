import datetime

# Class NameDOB takes Name and Date of Birth from user console then search the DOB by user name and
# display it.


class NameDOB:

    data = {}

    # Function __init__() or constructor call the specific function according to the user's choice.
    def __init__(self, choice):
        if choice == 1:
            self.adddata()
        elif choice == 2:
            while 1:
                try:
                    print("DOB of entered name is " + self.searchbyname())
                    break
                except TypeError:
                    print("Search named is not available in our database.")
                    break
                except FileNotFoundError:
                    print("Currently database is empty.")
                    break
        elif choice == 3:
            print("You are exit from the program.")
            exit()
        else:
            print("Please enter valid choice.")

    # Function adddata() takes details from user via console and checks whether entered details in
    # valid format or not.
    def adddata(self):
            self.name = input("Enter your name: ")
            while not self.name.isalpha():
                print("Please entered only alphabets.")
                self.name = input("Enter your name: ")
            # Validation for date is in valid format or not.
            self.datevalidation()
            self.secret = input("Is this secret name?(yes/no): ")
            while 1:
                if self.secret == 'yes' or self.secret == 'y':
                    self.secretvalue = 1
                    break
                elif self.secret == 'no' or self.secret == 'n':
                    self.secretvalue = 0
                    break
                else:
                    print("Please enter yes or no only.")
                    self.secret = input("Is this secret name?(yes/no): ")
                    continue
            # Function writetofile() write all entered data in the file.
            self.writetofile()

    # Function datevalidation() validate the date is in valid format or not.
    def datevalidation(self):
        while 1:
            self.dob = input("Enter your Date of Birth(dd/mm/year): ")
            try:
                datetime.datetime.strptime(self.dob, "%d/%m/%Y")
                break
            except ValueError:
                print("Invalid Date")
                continue

    # Function writetofile() write all entered data in pickle file.
    def writetofile(self):
        self.data.update({self.name: {"DOB": self.dob, "secret": self.secretvalue}})
        import pickle as pk
        pickle_out = open("problem1_data_file.pickle", "ab+")
        pk.dump(self.data, pickle_out)
        pickle_out.close()
        print("Your entered details has been saved successfully.")

    # Function searchbyname() search entered name in the file and if name is secret then its return secret
    # otherwise return date of birth of that name which associated with it.
    def searchbyname(self):
        pickle_in = open("problem1_data_file.pickle", "rb+")
        import pickle as pk
        responsedata = {}
        while 1:
            try:
                responsedata.update(pk.load(pickle_in))
            except EOFError:
                break
        pickle_in.close()
        self.fname = input("Enter the name to be search: ")
        if responsedata.get(self.fname):
            if responsedata[self.fname]['secret'] == 1:
                return 'Secret'
            else:
                return responsedata[self.fname]["DOB"]


print("""This is the small program which save your basic details and you can search your all details by name only.
1.Want to add details in the database.
2.Search by name.
3.Exit from the program.""")
while 1:
    try:
        choice = input("Your choice number:- ")
        NameDOB(int(choice))
    except ValueError:
            print("Please enter valid choice.")
