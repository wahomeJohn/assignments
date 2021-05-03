#def StudentDetails():

studentFname    = input("Enter student first  name :")
studentLname    = input("Enter student last  name :")
studentId       = input("Enter student Id :")
student_sex     = input("Enter student sex :")
studentEmail    = studentFname + studentLname + "@gmail"
studentFullname = studentFname + " " + studentLname

#def MailingAddress():

address = input("Enter address:")
city = input("Enter city :")
country = input("Enter country :")
region = input("Enter region. A for Africa or O for others :")


#def CalculateScore():

quiz1 = int(input("Enter quiz1 points : "))
quiz2 = int(input("Enter quiz2 points : "))
quiz3 = int(input("Enter quiz2 points : "))
test1 = int(input("Enter test1 points : "))
test2 = int(input("Enter test2 points : "))
zoom1 = int(input("Enter zoom1 points : "))
zoom2 = int(input("Enter zoom2 points : "))
zoom3 = int(input("Enter zoom3 points : "))
assignment= int(input("Enter assignment attempted :"))
assignment_percent = (assignment/10)* 100
avearagepoints = (quiz1 + quiz2 + quiz3 + test1 +test2)/5
zoompoints = ((zoom1 + zoom2 + zoom3)/9)* 100
totalpoints = (avearagepoints + zoompoints + assignment_percent)/3
   # return totalpoints

print("Student Name: " + studentFullname, "Student Id : " + studentId, "student Email : " + studentEmail,"studentsex :" + student_sex )
print("Mailing Address :"+ address + " " + city + " " + country + " " + region)

while region == "A":
#def conditional():
    if student_sex == "male" and totalpoints >= 80:
           # if totalpoints >= 80:
        print(" Full Scholarship Awarded")
    elif student_sex == "female" and totalpoints >= 76:
        print("Full Scholarship Awarded")
    else:
        print("No Scholarship")

    break
