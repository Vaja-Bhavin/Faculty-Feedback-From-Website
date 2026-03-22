import faculty as f
import pickle as p
import json as j
import os
import matplotlib.pyplot as plt
import pandas as pd
with open("Data/faculty.json","r") as f1:
    FAC = j.load(f1)

with open("Data/subject.json","r") as f1:
    SUB = j.load(f1)


odd_sem = {"1":("1","3","5"),"2":("2","4","6")}

class form:

    def __init__(self):
        self.facultys=[]
        while True:
            term = input("1:Odd, 2:Even \nEnter Term: ")
            if term in ("1","2"):
                break
            print("Enter Valid Choise")

        self.term = term
        while True:
            valid = odd_sem[term]
            sem = input(f"Enter Sem {valid}:")
            if sem in valid:
                break
            print("Enter Valid Choise")
        self.sem = sem
        self.year = int(input("Enter Year: "))
        self.dir_name = str(f"{str(self.sem)}_{str(self.year)}")

        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
            f1 = open(f"{self.dir_name}/data.dat","wb")
            f1.close()
            self.add_faculty()
        else:
            print("Form Already Exist!")

    def add_faculty(self):
        try:
            n = int(input("Enter Number of Faculty: "))
        except ValueError:
            print("Enter Valid Answer!")
        else:
            for i in range(n):
                for key,val in FAC.items():
                    print(f"Key:-{key} Id:{val["Id"]},Name:{val["Name"]}")

                print(f"\n{i+1}st Faculty")
                id = int(input("Enter Key: "))
                name = FAC[str(id)]["Name"]
                divsub = {}
                print()
                print("Now Enter Subject For Division.")

                sub = SUB[str(self.sem)]

                for key,val in sub.items():
                    print(f"{key}:Sub Code-{val["Code"]},Sub Name-{val["Name"]}")
                print("If Faculty Don't Take Lacture In Particular Div Enter '0'! ")
                

                for div in ["A","B","C"]:
                    sub2 = int(input(f"Enter Subject For {div}: "))
                    if sub2 == 0:
                        continue
                    divsub[div]=sub[str(sub2)]
                print()
                # print(divsub)
                qua = 12
                temp = len(divsub)
                if temp == 3:
                    if divsub["A"] != divsub["B"]:
                        qua +=12
                        if divsub["B"] != divsub["C"]:
                            if divsub["A"] != divsub["C"]:
                                qua +=12
                    else:
                        if divsub["A"] != divsub["C"]:
                            qua +=12
                elif temp == 2:
                    temp1 = divsub.keys()
                    if "A" in temp1:
                        if "B" in temp1:
                            if divsub["A"] != divsub["B"]:
                                qua+=12
                        else:
                            if divsub["A"] != divsub["C"]:
                                qua+=12
                    else:
                        if divsub["B"] != divsub["C"]:
                            qua+=12
                # qua = len(divsub)*12
                print(qua)
                fn = self.dir_name+"/"+name+".csv"
                fac = f.faculty(id,name,divsub,qua,fn)
                self.facultys.append(fac)
            self.save_to_file()

    def save_to_file(self):
        with open(f"{self.dir_name}/data.dat","wb") as f1:
            p.dump(self,f1)


    @classmethod
    def Show_Graph(cls):
        id,fnl = [],[]
        sem = int(input("Enter Sem: "))
        year = int(input("Enter Year: "))
        try:
            data = form.load_from_file(sem,year)
        except FileNotFoundError:
            print("Feedback Not Available!")
            return
        
        for fac in list(data.facultys):
            id.append(fac.name)
            fn = fac._find_score()
            fnl.append(fn)
        plt.bar(id,fnl)
        plt.show()


    @classmethod
    def Show_Data(self):
        sem = int(input("Enter Sem: "))
        year = int(input("Enter Year: "))
        try:
            data = form.load_from_file(sem,year)
        except FileNotFoundError:
            print("Feedback Not Available!")
            return
        for fac in list(data.facultys):
            fac.Show_Data()
            print()
        
    @classmethod
    def Show_Score(cls):
        sem = int(input("Enter Sem: "))
        year = int(input("Enter Year: "))
        try:
            data = form.load_from_file(sem,year)
        except FileNotFoundError:
            print("Feedback Not Available!")
            return

        
        for fac in list(data.facultys):
            fs = fac._find_score()
            print(f"Id: {fac.id}\nName: {fac.name}\nFinal Score: {fs}\n")

    @classmethod
    def load_from_file(cls,sem,year):
        dir_name = f"{sem}_{year}"
        
        with open(f"{dir_name}/data.dat","rb") as f1:
            data =p.load(f1)
            return data
        
    def generate_grade_file(self):
        fdata = {
            "ID":[],
            "Name":[],
            "Grade":[]
               }
        for fac in self.facultys:
            temp = float(str(fac._find_score())[:4])
            fdata["ID"].append(fac.id)
            fdata["Name"].append(fac.name)
            fdata["Grade"].append(temp)
        df = pd.DataFrame(fdata)
        df["x25 Ratio"] = df["Grade"]*5
        df.to_csv(f"{self.dir_name}/Grade File.csv",index=False)
        print("Grade File Successfully Generated.")
        print()