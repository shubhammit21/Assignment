import re
n = input("enter the number of email to be validated")
E_list =[]
for i in range(int(n)):
    email = input("enter the email address::")
    E_list.append(email)
for i in E_list:
    if re.findall('[a-zA-z0-9.+-]+@[a-zA-Z0-9-]+\.com',i):
        print("Email is valid:" +i)
    else:
        print("Email is not valid:" +i)
