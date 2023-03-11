from close import Logout
from manage import manage_attendance
Student_ID=["191EC111","191EC112","191EC113","191EC114","191EC115"]
Student_name=["Abi","Akash","Ajith","Dhanush","Keerthi"]
Student_Email=["abi111@gmail.com","akash112@gmail.com","ajith113@gmail.com","dhanush114@gmail.com","Keerthi115@gmail.com"]
Student_leave=[1,3,0,2,0]
Student_attendance=[99,97,100,98,100]
class student():
    def viewdetails(self):
        Stuid=input("Student's ID : ")
        for i in range(len(Student_ID)):
            if(Student_ID[i]==Stuid):
                print("Student name : "+Student_name[i])
                print("Student Email : ",Student_Email[i])
                print("No of leaves : ",Student_leave[i])
                print("Attendance Percent : ",Student_attendance[i])
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
                        Logout.logout(self=None)
                    else:
                        print("Enter valid number")
                except ValueError:
                    print("Enter an integer")
    def addstudent(self):
        Student_ID.append(input("Student ID : "))
        Student_name.append(input("Student name : "))
        Student_Email.append(input("Student Email : "))
        Leave=input("No of leaves : ")
        Student_leave.append(Leave)
        atd=str(100-(int(Leave)))
        Student_attendance.append(atd)
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
                Logout.logout(self=None)
            else:
                print("Enter given number")
        except ValueError:
            print("Enter an integer")
    
    


