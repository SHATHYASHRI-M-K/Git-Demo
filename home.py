from register import Register
class Home():
    @classmethod
    def homepage(self):
        print("\t\t\t\tWelcome to Staff Dashboard\t\t\t\t")
        print("1 - Signup or 2 - Login")
        number=int(input("Signup/Login "))
        try:
            if(number==1):
                Register.signup()
            elif(number==2):
                Register.login(self)
            else:
                print("Enter valid number")
        except ValueError:
            print("Enter an integer")

        

        
            
    
            



    
