import re
from Addstudent import student
from manage import manage_attendance
from close import Logout
Userlist=["Anushri"]
Emaillist=["anushri12@gmail.com"]
Passwordlist=["Anu123@#"]
class Register():
    @classmethod
    def signup(self):
        print("\t\t\t\t\t\tSignup\t\t\t\t\t\t")
        Username = input("Enter Username : ")
        Email = input("Enter Email : ")
        if re.match(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[@.])",Email):
            #print("Valid Email")
            password=input("Enter password: ")
            if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[*@#$!%^&{}])(?=.*[0-9])",password):
                #print("Strong password")
                Reenter_password=input("Reenter Password : ")
                if(Reenter_password == password):
                    print("\t\t\t\t\tRegistration is successful\t\t\t\t\t")
                    Userlist.append(Username)
                    Emaillist.append(Email)
                    Passwordlist.append(password)
                    Register.login(self)
                else:
                    print("Not matched")
            else:
                print("Weak password")
        else:
            print("Invalid Email")
    def login(self):
        print("\t\t\t\t\t\tLogin\t\t\t\t\t\t")
        User_name = input("Enter Username : ")
        E_mail = input("Enter Email : ")
        pass_word = input("Enter Password : ")
        if User_name in Userlist:
            if E_mail in Emaillist:
                if pass_word in Passwordlist:
                    print("\t\t\t\t\tLogin successful\t\t\t\t\t")
                    print("\t\t\t\tStaff dashboard\t\t\t\t")
                    print("1 - Addstudent  2 - view Students details,3 - Students leave apply,4 - Logout : ")
                    try:
                        number=int(input())
                        if(number==1):
                            student.addstudent(self)
                        elif(number==2):
                            student.viewdetails(self)
                        elif(number==3):
                            manage_attendance.manage(self)
                        elif(number==4):
                            Logout.logout(self)
                        else:
                            print("Enter valid number")
                    except ValueError:
                        print("Enter an integer")
                else:
                    print(" Invalid Username or password")
            else:
                print("Invalid Username or password")
        else:
            print("Invalid Username or password")
    