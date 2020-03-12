'''
将4种print方法分别在vscode上练习一下
'''
# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
# print(info)


# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary) 
# print(info1)


# name = input("username：") 
# age = input("age：") 
# skill = input("skill：") 
# salary = input("salary：") 
# info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) 
# print(info)


name = input("name：") 
age = input("age：") 
skill = input("skill：") 
salary = input("salary：") 
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, age, skill, salary) 
print(info)