import student as s
import form as fm
from Data import editData

while True:
    a = (input("1: Student,\n2: Faculty.\nWho Are You: "))
    if a in ("1","2"):
        a = int(a)
        break
    print("Enter Valid Option!\n")
print()
if a==1:
    b = input("Do You Want To Give Feedback(Y/N): ")
    if b in ("Y","y"):
        print()
        enno = int(input("Enter En No:"))
        name = input("Enter Name: ")
        sem = int(input("Enter Sem:"))
        while True:
            div = input("Enter Your Division(A,B,C):")
            if div in ("A","B","C"):
                break
            print("Enter Valid Answer!")
        year = int(input("Enter Year:"))
        s2 = s.student(enno,name,sem,div,year)
        try:
            s2.givfeedback()
        except KeyboardInterrupt:
            print("Please Fill Form Before Leaving")
elif a==2:
    while True:
        c = int(input("1:Show Data,\n2:Show Score,\n3:Show Graph,\n4:Create New Form,\n5:Edit Data,\n6:Generate Grade File\n0:Exit.\nEnter Your Operation: "))
        print()
        if c==1:
            fm.form.Show_Data()
        elif c==2:
            fm.form.Show_Score()
        elif c==3:
            fm.form.Show_Graph()
        elif c==4:
            fm.form()
        elif c==5:
            editData()
        elif c==6:
            semTemp = int(input("Enter Sem: "))
            yearTemp = int(input("Enter Year: "))
            try:
                data = fm.form.load_from_file(semTemp,yearTemp)
            except FileNotFoundError:
                print("Feedback Not Available!")
                print()
                continue
            data.generate_grade_file()
        elif c==0:
            break
        else:
            print("Enter Valid Operation!")