#Reversed names uwu#
def reverse (Fname):
    revs_string = ""
    for i in Fname:
        revs_string = i+revs_string
    print("Reversed First name is",revs_string)

def reversed (Lname):
    revsd_string = ""
    for i in Lname:
        revsd_string = i+revsd_string
    print("Reversed Last name is",revsd_string)
Fname = input("Please input your first name ")
Lname = input("Please input your last name ")
print("You entered", Fname, Lname)
reverse(Fname)
reversed(Lname)

print("Another form of your reversed name is :",Lname, Fname)



