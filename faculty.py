import pandas as pd
temp1 = [0,0,0,0,0,0]
class filesys:
    def __init__(self,fn):
        # self.fn = f"Data/{fn}.csv"
        self.fn = fn
        self.data = {
            "q1":temp1,
            "q2":temp1,
            "q3":temp1,
            "q4":temp1,
            "q5":temp1,
            "q6":temp1,
            "q7":temp1,
            "q8":temp1,
            "q9":temp1,
            "q10":temp1,
            "q11":temp1,
            "q12":temp1,
            "Total":[0,0,0,0,0,None],
            "Point":[5,4,3,2,1,None],
            "Score":[0,0,0,0,0,0]
        }
        self.data = pd.DataFrame(self.data,index=["Excellent","Very Good","Good","Poor","Very Poor","Total"])
        self.data.to_csv(fn)
class faculty(filesys):
    def __init__(self,id,name,divsub,qua,fn):
        self.id= id
        self.name=name
        self.divsub = divsub
        self.qua = qua
        
        filesys.__init__(self,fn)

    
    def Show_Data(self):
        # df=pd.DataFrame(self.data,index=["Excellent","Very Good","Good","Poor","Very Poor","Total"])
        # df.to_csv(self.fn)
        # self.data = pd.read_csv(self.fn)
        print(f"Id: {self.id}\nName: {self.name}\nDiv-Sub: {self.divsub}\nFile Name: {self.fn}")
        print(self.data)

    
    def _find_score(self):
        # df = pd.read_csv(self.fn)
        df = self.data
        fs = df.at[5,"Score"]/(self.qua*df["q12"][5])
        return fs
    
