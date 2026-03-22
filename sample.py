divsub = {}
for div in ["A","B","C"]:
    sub2 = (input(f"Enter Subject For {div}: "))
    if sub2 == '0':
        continue
    divsub[div]=sub2
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
        
print(qua)