import json

class UserInfo:
    def __init__(self, path='', filename=''):
        #Initialize variables
        self.name = input("\nName: ")
        self.phone = input("Phone number: ")
        self.address = input("Address: ")
        self.path = path
        self.filename = filename

    def dump_info(self):
        # Get desired directory and file name from the user.
        self.path = input("\nDesired path: ")
        self.filename = input("Desired file name: ")

    def compiled_info(self):
        # Make sure file is in .txt file format
        if '.txt' in self.name:
            self.fullpath = self.path + '/' + self.filename
        else:
            self.fullpath = self.path + '/' + self.filename + '.txt'

        self.userinfo = f"{self.name}," + f"{self.phone}," + f"{self.address}"
    
    def json_pass(self):
        try:
            with open(self.fullpath, 'w') as f:
                json.dump(self.userinfo, f)   
        except FileNotFoundError:
            print("Please double check directory path.")
        else:
            print("\nSuccess!!")