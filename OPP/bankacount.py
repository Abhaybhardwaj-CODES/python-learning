class back_account:
    def __init__(self, fullname, fathername, address, adhar_no):
        self.fullname = fullname
        self.fathername = fathername
        self.address = address
        self.adhar_no = adhar_no
    def display(self):
        print("Full Name:", self.fullname)
        print("Father Name:", self.fathername)
        print("Address:", self.address)
        print("Adhar No:", self.adhar_no)
        print("Account Created Successfully")