# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentID","Rollno","name","mobno"])

# studentID = int(input("Enter student id:"))
# Rollno = int(input("Enter Roll No :"))
# name = input("Enter Name :")
# mobno = int(input("Enter your mob no :"))
# a.writerow([studentID,Rollno,name,mobno])
# print("student record has save") 


#--------------------------------------------------------------------------------------

import csv
s = open("SRL.csv", "a", newline="")
a = csv.writer(s)
a.writerow(["Student_Name","RollNo","mobNo","p1","p2","p3","total","percentage","email","Result"])

# student_Name = int(input("Enter student Name:"))
# RollNo = int(input("Enter Roll number:"))
# mobNo = int(input("Enter mobile number:"))
# p1 = int(input("Enter Marks of P1 :"))
# p2 = int(input("Enter Marks of P2 :"))
# p3 = int(input("Enter Marks of P3 :"))

# total = (p1+p2+p3)
# percentage = (total/3)*100
