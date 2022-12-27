"""
print("begin")
try:
    a = int(input("Type a numarater:"))
    b = int(input("Type a denomanater:"))
    print(f"{a} / {b} = {a/b}")
except(ValueError,ZeroDivisionError):
    print(f"{b} cant a denomanater")
finally:
    print("Welcome")
    print("Hello")
print("END")
"""
###
"""
print("begin")
try:
    a = int(input("Type a numarater:"))
    b = int(input("Type a denomanater:"))
    print(f"{a} / {b} = {a/b}")
    raise KeyError
except(ValueError,ZeroDivisionError):
    print(f"{b} cant a denomanater")
except:
    print("Error occured")
finally:
    print("Welcome")
    print("Hello")
print("END")
"""
###
"""
print("Begin")

try:
    n = int(input("Enter a number:"))
    if type(n) is not int:
        raise TypeError
except TypeError:
    print("Enter integer Data only")
print("END")
"""
###
"""
def Kf(t):
    assert (t % 2 == 0), "Even number"
    return t * 10
try:
    print(Kf(12))
    print(Kf(6))
    print(Kf(5))
except(AssertionError):
    print("The temrater should be positive")
"""
###
"""
Class is a container which contains Data related operations
Data--->Variables
Operations--->Methods
with in a class we can declare 3 types of variables
1)Non static variable
2)Static variable
3)Local variable
with in a class we can define 3 types of variables
1)Non static variable
2)Static variable
3)Class method
"""
###
"""
class Test:
    def Ml(self):
        print("Inside ML method")
t1 = Test()
t1.Ml()
"""
###
"""
class Test:
    a = 1000
    b = 2000
    def Display(self):
        print(Test.a,Test.b)
    def Update(self):
        Test.a=Test.a+10
        Test.b=Test.b+20
T1 = Test
T1.Display()
T1.Update()
"""
###
"""
class Test:
    a = 1000
    b = 2000
    def Display(self):
        print(Test.a,Test.b)
T1 = Test()
T1.Display()
print(T1.a)
print(T1.b)
T1.a=T1.a+100
T1.b=T1.b+200
print(T1.a,T1.b)
"""
###
"""
class Test:
    a = 1000
    b = 2000
    def Display(self):
        print(Test.a,Test.b)
    def Update(self):
        Test.a=Test.a+100
        Test.b=Test.b+200
T1 = Test
print("1st Object")
T1.Display()
T1.Update()
T1.Display()
T2 = Test
print("2nd Object")
T2.Display()
T2.Update()
T2.Display()
T3 = Test
print("3rd Object")
T3.Display()
T3.Update()
T3.Display()
T4 = Test
print("4th Object")
T4.Display()
T4.Update()
T4.Display()
"""
###
"""
class Test:
    def Insert(self):
        a = 1000
        b = 2000
    def Display(self):
        print(self.a,self.b)
    def Update(self):
        self.a=self.a+10
        self.b=self.b+20
T1 = Test()
T1.Insert()
T1.Display()
T1.Update()
T1.Display()
T2 = Test()
T2.Insert()
T2.Display()
T2.Update()
T2.Display()
T3 = Test()
T3.Insert()
T3.Display()
T3.Update()
T3.Display()
T4 = Test()
T4.Insert()
T4.Display()
T4.Update()
T4.Display()
"""
###
"""
class Test:
    a = 1000
    b = 2000
    def Display(self):
        print(Test.a, Test.b)
T1 = Test()
T1.Display()
print(T1.a, T1.b)
T1.a = T1.a + 12
T1.b = T1.b + 45
print(T1.a,T1.b)
"""
###
"""
class Test:
    def Insert(self):
        self.a = 100
        self.b = 50
    def Display(self):
        print(self.a, self.b)
    def Update(self):
        self.a = self.a + 100
        self.b = self.b + 50
T1 = Test()
T1.Insert()
T1.Display()
T1.Update()
print(T1.a, T1.b)
T1.a = T1.a + 10
T1.b = T1.b + 20
print(T1.a,T1.b)
"""
###
"""
# it's a special metherd constucted the variables that are declared are local variables which are declared direcly are known as local variable the data 
# which are recuierd to use whitin a direct methord for all the local vaiables of a methord memory will be aloted wenever we make a methord fall local 
# variables we canot aces from out side the class

class Test:
    def Ml(self):
        a = 10
        b = 30
        print(a,b)
    def Ml2(self):
        c = 30
        d = 40
        print(c,d)
        print(a)
T1 = Test()
T1.Ml()
T1.Ml2()
print()
"""
###
"""
class Test:
    def __init__(self):
        self.a = 1000
        self.b = 2000
    def Ml(self):
        print(self.a,self.b)
T1 = Test()
T1.Ml()
"""
###
"""
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Display(self):
        print(self.a, self.b)
T1 = Test(10, 20)
T1.Display()
T2 = Test(30, 40)
T2.Display()
"""
###
"""
class Student:
    Colage_Name = "MRCET"
    def __init__(self, Name, Id1, S1, S2, S3):
        self.Name = Name
        self.Id1 = Id1
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
    def Display(self):
        print(Student.Colage_Name, self.Name, self.Id1, self.S1, self.S2, self.S3)
    def Find_Result(self):
        if((self.S1>200) and (self.S2>200) and (self.S3>200)):
            print("Pass")
        else:
            print("Fail")
S1 = Student("Rahmatullah", 850,280,270,290)
S1.Display()
S1.Find_Result()
S2 = Student('Abdur Rahman', 746, 246, 250, 250)
S2.Display()
S2.Find_Result()
"""
###
"""
class Student:
    Colage_Name = "MRCET"
    def __init__(self, Name, Rno, S1, S2, S3):
        self.Name = Name
        self.Rno = Rno
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
    def Display(self):
        print(Student.Colage_Name, self.Name, self.Rno, self.S1, self.S2, self.S3)
    def Find_Result(self):
        if((self.S1>50) and (self.S2>50) and (self.S3>50)):
            print(f"{self.Name} Passed")
        else:
            print(f"{self.Name} Failed")
N = int(input("Enter N value:"))
I = 1
while I <= N:
    print("----------------------------------------")
    name = input("Enter your name:")
    Rno = int(input("Enter your Rno:"))
    S1,S2,S3 = map(int,input("Enter your 3 subject marks:").split(" "))
    St1 = Student(name, Rno, S1, S2, S3)
    St1.Display()
    St1.Find_Result()
    print("----------------------------------------")
    I = I + 1
"""
###
"""
class Emplaoye:
    job = "Hospital"
    def __init__(self, Name, Id1, Salary):
        self.Name = Name
        self.Id1 = Id1
        self.Salary = Salary
    def Display(self):
        print(Emplaoye.job, self.Name, self.Id1, self.Salary)
N = int(input("Enter N value:"))
I = 1
while I <= N:
    print("----------------------------------------")
    name = input("Enter your name:")
    Id1 = int(input("Enter your Id1:"))
    Salary = int(input("Enter your salary:"))
    St1 = Emplaoye(name, Id1, Salary)
    St1.Display()
    print("----------------------------------------")
    I = I + 1
"""
###
"""
class Math:
    def Mutiply(A, B):
        print(A  * B)
    def Divide(A, B):
        print(A / B)
    def Add(A, B):
        print(A + B)
    def Sub(A, B):
        print(A - B)
W, R = map(int,input("Type 2 numbers:").split(" "))
M = Math.Mutiply(W, R)
D = Math.Divide(W, R)
A = Math.Add(W, R)
s = Math.Sub(W, R)
"""
###
"""
def Hello(Func):
    Func()

def Greet():
    print("Still Here!")

a = Hello(Greet)
print(a)
"""
###
"""
import random

Liam = random.randint(25, 50)
Arthur = random.randint(25, 50)
Alice = random.randint(25, 50)

Menu = {
    "Veg Biriani": 10,
    "Chi Biriani": 15,
    "Beef Biriani": 20,
    "Mot Biriani": 25,
    "Prawn Biriani": 30,
    "Mix Biriani": 35,
    "Veg Pizza": 20,
    "Chi Pizza": 25,
    "Beef Pizza": 30,
    "Peperoni Pizza": 35,
    "Mix Pizza": 40
}

def Restorent():
    print(Menu)
    print("What do you want from the menu?")
    
Restorent()
"""
###

import unittest
import main
"""
class Test(unittest.TestCase):
    def TestA(self):
        test_param = 10
        result = main.A(test_param)
        self.assertEqual(result, 15)

    def TestB(self):
        test_param = "fvgcuhd"
        result = main.A(test_param)
        self.assertEqual(result, isinstance(ValueError))

unittest.main()
"""
###
"""
from PIL import Image, ImageFilter

Sword_Pic = Image.open("images/swords1.jpg")
Sword_Pic_Blur = Sword_Pic.filter(ImageFilter.BLUR)
Sword_Pic_Smoothen = Sword_Pic.filter(ImageFilter.SMOOTH)
Sword_Pic_More_Smoothend = Sword_Pic.filter(ImageFilter.SMOOTH_MORE)
Sword_Pic_Sharpen = Sword_Pic.filter(ImageFilter.SHARPEN)
Sword_Pic_Sharpen_More = Sword_Pic_Sharpen.filter(ImageFilter.SHARPEN)
Sword_Pic_Gray_scale = Sword_Pic.convert("L")
Sword_Pic_Rotated = Sword_Pic.rotate(90)
Sword_Pic_Resized = Sword_Pic.resize((320, 320))
Box = (320,320,640,640)
Sword_Pic_Croped = Sword_Pic.crop(Box)


Sword_Pic_Sharpen_More.show()
"""
###
"""
import smtplib
from email.message import EmailMessage as EM
Email = EM()
Email["From"] = "Raj Raj"
Email["To"] = "rahmatullah.ajmal123"
Email["Subject"] = "You Won 117,000,000 AED!!"
Email.set_content("Pleas send your Bank Card number to recive your money")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login()
    smtp.send_message(Email)
    print("All good boss")
"""
###
"""
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".storylink")
subtext = soup.select(".subtext")

def C_c_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        votes = subtext[idx].select(".score")
        if len(votes):
            points = int(votes[0].getText().replace("points", ""))
            hn.append({"title" : title,"links" : href},"votes" : points)


    return hn
C_c_hn(links, subtext)
"""
###




