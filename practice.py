# from github import *
# g = Github("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")
# g = Github(base_url=("{https://github.com/saurabhk7677/pythoncode.git}"))
# for repo in g.get_user().get_repos():
#     print(repo.pythoncode)
# str1 =  "this is spartaaaaa"
# print("shri ram")
# print(str1)

# print("hello spartaaaaa!")

#########################################################################

# def decor(num):
#     def inner():
#         a = num()
#         add = a + 5
#         return add
#     return inner

# #@decor
# def num():
#     return 10

# result_fun = decor(num)
# print(result_fun())
# #print(num())

###############################################################################

# class Employee:
#     name = "ram"
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         #self.email = f"{fname} {lname}@gmail.com"
#         self.mobile = 7066885714

#     def show(self):
#         return f"This Employee is {self.fname} {self.lname}"

#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#     @classmethod
#     def xyz(cls):
#         print("staticmethod")
#         return Employee.name
#         # print(cls.lname)
        
# saurabh = Employee('saurabh', 'kadam.')
# print(saurabh.show())
# print(saurabh.email())
# print(saurabh.xyz())
# # print(saurabh.mobile)

# import pdb


# pdb.set_trace
# num1 = int(input("Enter first Number: "))
# num2 = input("Enter Sencond Number: ")
# addition = num1 + num2
# print(f"additin is {addition}")


class Mobile():
    fp = 'Yes'

    def __init__(self):
        self.model = 'Realme x'

    def show_model(self):
        print("Model: ", self.model)

    @classmethod
    def is_fp(cls):
        print("Fingure print: ",cls.fp)

realme = Mobile()
realme.show_model()
Mobile.is_fp()
print()
Mobile.fp = 'No'
Mobile.is_fp()
