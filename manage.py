from Student import Stu_leave
import Addstudent
from close import Logout
class manage_attendance():
    def manage(self):
        Rollno,Days,Reason = Stu_leave.Stuleave(self)
        print("Roll No : ",Rollno)
        print("Number of Days : ",Days)
        print("Reason for leave : ",Reason)
        des=input("Approve/Cancel : ")
        if(des=="approve"):
            
            for i in range(len(Addstudent.Stu_ID)):
                
                if(Addstudent.Stu_ID[i]==Rollno):
                    Addstudent.Stu_atdpercent[i]=str(int(Addstudent.Stu_atdpercent[i])-int(Days))
                    print("Student name : ",Addstudent.Stu_name[i])
                    print("Student Email : ",Addstudent.Stu_Email[i])
                    print("No of leaves : ",Days)
                    print("Attendance Percent : ",Addstudent.Stu_atdpercent[i])
        else:
            print("Leave cancelled")
        Logout.logout(self)
# manage_atd.manage()