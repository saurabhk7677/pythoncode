from github import *
g = Github("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")
g = Github(base_url=("{https://github.com/saurabhk7677/pythoncode.git}"))
for repo in g.get_user().get_repos():
    print(repo.pythoncode)
str1 =  "this is spartaaaaa"
print("shri ram")
print(str1)

print("hello spartaaaaa!")