import pandas as pd

class Convert:
    def __init__(self,roll,name,age,phone,address):
        self.roll=roll
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address

    def display2(self):
        print(f"Hello {self.name} - your roll is {self.roll}")

df=pd.read_csv(r"C:\Users\risha\Downloads\my_students.csv")

hey_students=[]
collect=[]

for i in df.index:
    my_stud={}
    my_address={}
    my_stud["roll"]=df.loc[i,"roll"]
    my_stud["name"]=df.loc[i,"name"]
    my_stud["age"]=df.loc[i,"age"]
    my_stud["phone"]=df.loc[i,"phone"]
    my_address["add1"]=df.loc[i,"address.add1"]
    my_address["add2"]=df.loc[i,"address.add2"]
    my_address["add3"]=df.loc[i,"address.add3"]
    my_address["add4"]=df.loc[i,"address.add4"]
    my_address["add5"]=df.loc[i,"address.add5"]
    my_stud["address"]=my_address
    hey_students.append(my_stud)

for i in hey_students:
    o=Convert(i['roll'],i['name'],i['age'],i['phone'],i['address'])
    collect.append(o)

for i in collect:
    i.display2()