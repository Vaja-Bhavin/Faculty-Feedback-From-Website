fn = ["faculty.json","subject.json"]
import json as j

def arrangeFac(data:dict):
    temp = {}
    for key,value in zip(range(1,len(data)+1),data.values()):
        temp[str(key)] = value
    # for value in data.values():
    #     temp[str(value["Id"])] = value
    return temp

def arrangeSub(data:dict):
    temp1 = {}
    for key1,value1 in data.items():
        temp2 = {}
        for key,value in zip(range(1,len(value1)+1),value1.values()):
            temp2[str(key)] = value
        temp1[key1] = temp2
    return temp1

def loadData(filename):
    with open(f"Data/{filename}") as f:
        data = j.load(f)
    return data

def dumpData(data,filename):
    with open(f"Data/{filename}","w") as f:
        j.dump(data,f)

def displayFac():
    data = loadData(fn[0])
    print("\nFacultys: ")
    for key,value in data.items():
        print(f"{key}:- Id: {value["Id"]},Name: {value["Name"]}")
    print()

def displaySub(sem):
    data = loadData(fn[1])[sem]
    print("\nSubject Of Sem {}:".format(sem))
    for key,value in data.items():
        print(f"Key:{key}:- Code: {value["Code"]},Name: {value["Name"]}")
    print()
    

def addFaculty():
    data = loadData(fn[0])
    while True:
        id = int(input("Enter Id: "))
        name = input("Enter Name: ")
        print(f"\nData:- \nId: {id}, Name: {name}")
        a = input("1:Proceed, 2:Edit\nEnter Your Operation: ")
        if a=="1":
            break
        elif a=="2":
            pass
        else:
            print("Enter Valid Operation!")
    data[id] = {"Id":id,"Name":name}
    data = arrangeFac(data)
    dumpData(data,fn[0])
    displayFac()

def removeFaculty():
    data = dict(loadData(fn[0]))
    for key,value in data.items():
        print(f"{key}:- Id: {value["Id"]}, Name: {value["Name"]}")
    while True:
        no = (input("Enter No.: "))
        print(f"Selected Faculty:-\nId: {data[no]["Id"]}, Name: {data[no]["Name"]}")
        a = input("1:Proceed, 2:Reselect\nEnter Your Operation: ")
        if a=="1":
            break
        elif a=="2":
            pass
        else:
            print("Enter Valid Operation!")
    data.pop(str(no))
    data = arrangeFac(data)
    dumpData(data,fn[0])
    displayFac()
# fac done

def addSubject():
    data = loadData(fn[1])
    sem = int(input("Enter Sem: "))
    while True:
        code = input("Enter Code: ")
        name = input("Enter Name: ")
        print(f"Data:- Code: {code},Name: {name}")
        a = input("1:Proceed, 2:Edit\nEnter Your Operation: ")
        if a=="1":
            break
        elif a=="2":
            pass
        else:
            print("Enter Valid Operation!")
    data[str(sem)][code[-2::]] = {"Code":code,"Name":name}
    data = arrangeSub(data)
    dumpData(data,fn[1])
    displaySub(str(sem))
    # print(data)

def removeSubject():
    data = dict(loadData(fn[1]))
    sem = int(input("Enter Sem: "))
    temp = data[str(sem)]
    for key,value in temp.items():
        print(f"Key:{key}:- Code: {value["Code"]},Name: {value["Name"]}")
    while True:
        id= (input("Enter Key: "))
        print(f"Selected Data:-\nCode: {temp[id]["Code"]}, Name: {temp[id]["Name"]}")
        a = input("1:Proceed, 2:Reselect\nEnter Your Operation: ")
        if a=="1":
            break
        elif a=="2":
            pass
        else:
            print("Enter Valid Operation!")
    data[str(sem)].pop(str(id))
    data = arrangeSub(data)
    dumpData(data,fn[1])
    displaySub(str(sem))
    # print(data)



def editData():
    while True:
        print("1:Edit Faculty,\n2:Edit Subject,\n3:Back.")
        a = (input("Enter Operation: "))
        print()
        if a =="1":
            while True:
                print("1:Add Faculty,\n2:Remove Faculty,\n3:Display,\n4:Back.")
                choise = (input("Enter Operation: "))
                print()
                if choise=="1":
                    addFaculty()
                elif choise=="2":
                    removeFaculty()
                elif choise == "3":
                    displayFac()
                elif choise=="4":
                    break
                else:
                    print("Enter Valid Operation!\n")
        elif a=="2":
            while True:
                print("1:Add Subject,\n2:Remove Subject,\n3:Display,\n4:Back.")
                choise = (input("Enter Operation: "))
                print()
                if choise=="1":
                    addSubject()
                elif choise=="2":
                    removeSubject()
                elif choise=="3":
                    displaySub((input("Enter The Sem:")))
                elif choise=="4":
                    break
                else:
                    print("Enter Valid Operation!\n")
        elif a=="3":
            break
        else:
            print("Enter Valid Operation!\n")
            

# editData()


# with open("Data/faculty.json","r") as f1:
#     FAC = j.load(f1)
# print(arrangeFac(FAC))

# with open("Data/subject.json","r") as f1:
#     SUB = j.load(f1)
# print(arrangeSub(SUB))

# addFaculty()
# removeFaculty()
# addSubject()
# removeSubject()