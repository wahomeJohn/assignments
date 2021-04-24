def StudentDetails():
    studentFname = input("Enter student first  name")
    studentLname = input("Enter student last  name")
    studentId        = input("Enter student Id")
    studentEmail    =input("Enter student Email")
    studentsex      =input("Enter student sex")
    StudentFullname = studentFname + " " + studentLname

    print("Student Name: " + StudentFullname, "Student Id : " + studentId, "student Email : " + studentEmail,"studentsex :" + studentsex )
def MailingAddress():
    address = int(input("Enter address"))
    city = input("Enter city :")
    country = input("Enter city :")
    region = input("Enter region. A for Africa or O for others :")
    print("Mailing Address :"+ address + " " + city + " " + country + " " + region)
def CalculateScore():
    quiz1 = int(input("Enter quiz1 points : "))
    quiz2 = int(input("Enter quiz2 points  : "))
    quiz3 = int(input("Enter quiz2 points: "))
    test1 = int(input("Enter test1 points : "))
    test2 = int(input("Enter test2 points : "))
    zoom1 = int(input("Enter zoom1 points : "))
    zoom2 = int(input("Enter zoom2 points : "))
    zoom3 = int(input("Enter zoom3 points: "))
    assignment= int(input("Enter assignment attempted :"))
    avearagepoints = (quiz1 + quiz2 + quiz3 + test1 +test2)/5
    zoompoints = zoom1 + zoom2 + zoom3
    totalpoints = avearagepoints + zoompoints + assignment
    return totalpoints

while region == "A":
    if student_sex == male:
        if totalpoints >= 80:
            print("Scholarship Awarded")
        else:
            print("No Scholarship")
    elif student_sex == female:
        if totalpoints >= 76:
            print("Scholarship Awarded")
        else:
            print("No Scholarship")

StudentDetails()
MailingAddress()