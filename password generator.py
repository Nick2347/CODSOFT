import random 

characters="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-=[];',./_+}{|:<>?"

length=int(input("Enter the length of password:-"))
password="".join(random.sample(characters,length))
print(password)