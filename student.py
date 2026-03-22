import faculty as f
import pandas as pd
import pickle as p
import form as  form
# from form import form
# fac = f.faculties
qua = ["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12"]
qua = {"q1":"Has The Teacher Covered entire syllabus as pre- described by University/College/Board",
       "q2":"Has the teacher covered relevant topics beyond syllabus",
       "q3":"Effectiveness of teacher in terms of (a) Technical/Course Content",
       "q4":"Effectiveness of teacher in terms of (b) Communication skills",
       "q5":"Effectiveness of teacher in terms of (c) Use of teaching aids",
       "q6":"Pace on which contents were covered",
       "q7":"Motivation and Inspiration for students to learn",
       "q8":"Support for the development of students skill (a) Practical demonstration",
       "q9":"Support for the development of students skill (b) Hands on trainning",
       "q10":"Clarity of expectations of students",
       "q11":"Feedback provided on students progress",
       "q12":"Willingness to offer help and advice to students"
       }

class student:
    DivFac = {"A":[1,3,4,5],
              "B":[1,2,3,4,5],
              "C":[1,2,3,4,5]}
    def __init__(self,en,name,sem,div,cyear):
        self.en = en
        self.name = name
        self.sem = sem
        self.div = div
        self.cyear = cyear
           
    def givfeedback(self):
        try:
            data = form.form.load_from_file(self.sem,self.cyear)
        except FileNotFoundError:
            print("Feedback Not Available!")
            return
        
        for k in list(data.facultys):
            if self.div not in k.divsub:
                continue
            i = k
            print(f"faculty:{i.name}, Sub:{i.divsub[self.div]}")
            i.score = 0
            j = 1
            i.data = pd.read_csv(i.fn)
            while j < 13:
                temp2=list(qua.keys())[j-1]
                print(f"\n{qua[temp2]}")
                print("1) excellent,\n2) very good,\n3) good,\n4) poor,\n5) very poor.")
                try:
                    a = int(input("Give Feedback:"))
                except:
                    print("Enter Valid Answer!")
                else:    
                    if a in (1,2,3,4,5):
                        i.data.at[a-1,temp2] = i.data[temp2][a-1]+1
                        j+=1
                        i.data.at[5,temp2] = i.data[temp2][5]+1
                    else:
                        print("Enter Valid Answer")
            i.data["Total"] = sum([i.data["q1"],i.data["q2"],i.data["q3"],i.data["q4"],i.data["q5"],i.data["q6"],i.data["q7"],i.data["q8"],i.data["q9"],i.data["q10"],i.data["q11"],i.data["q12"]])
            i.data["Score"] = i.data["Point"]*i.data["Total"]
            i.data.at[5,"Total"] = None
            i.data.at[5,"Score"] = sum(i.data.loc[0:4,"Score"])
            # print(i.data)
            i.data.to_csv(i.fn,index=False)
            data.save_to_file()