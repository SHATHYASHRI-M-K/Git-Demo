class Stu_leave:
    def Stuleave(self):      
        print("Enter Apply leave for leave : ")
        leave=input()
        if leave=="apply":
            Rollno=input("Enter Rollno : ")
            days=input("Enter no.of.days : ")
            Reason=input("Enter reason : ")
            return (Rollno,days,Reason)  
        else:
            print("Present")
    