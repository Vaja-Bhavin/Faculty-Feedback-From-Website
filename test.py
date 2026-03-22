import pandas as pd
# import faculty as f


# df1 = pd.read_csv("Data/Ravisir.csv")
# df2 = pd.read_csv("Data/NaykaMam.csv")
# df3 = pd.read_csv("Data/JignaMam.csv")
# df4 = pd.read_csv("Data/JaymitSir.csv")
# df5 = pd.read_csv("Data/JagadSir.csv")
# df = [[df1],[df2],[df3],[df4],[df5]]
# dfn = pd.DataFrame(df)
# dfn.to_json("Web/Data Temp.json",index=None)
# temp1 = [0,0,0,0,0,0]
# data1= {
#     "q1":temp1,
#     "q2":temp1,
#     "q3":temp1,
#     "q4":temp1,
#     "q5":temp1,
#     "q6":temp1,
#     "Total":[0,0,0,0,0,None],
#     "Point":[5,4,3,2,1,None],
#     "Score":[0,0,0,0,0,0]
# }
# data2 = [
#     temp1+[0,5,0],
#     temp1+[0,4,0],
#     temp1+[0,3,0],
#     temp1+[0,2,0],
#     temp1+[0,1,0],
#     temp1+[None,None,0]
# ]
# df1 = pd.DataFrame(data1,index=["Excellent","Very Good","Good","Poor","Very Poor","Total"])
# df2 = pd.DataFrame(data2,index=["Excellent","Very Good","Good","Poor","Very Poor","Total"],columns=["q1","q2","q3","q4","q5","q6","Total","Point","Score"])
# df["Total"] = sum([df["q1"],df["q2"],df["q3"],df["q4"],df["q5"],df["q6"]])
# df["Score"] = df["Point"]*df["Total"]
# a = sum(df.loc[0:4,"Score"])
# print(a)
# df.at[5,"Total"] = None
# df.at[5,"Score"] = sum(df.loc[0:4,"Score"])
# print(df1)
# print(df2)