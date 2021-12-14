my = input("enter the name:-")
sal = int(input("enter your salary:-"))      #intiser typecost

my = my.capitalize()                        #string capitalize method
print(my)

print("hello {},how are you".format(my))   #string formet method

#string formet method
print("Your salary is {salary:.2f}".format(salary=sal))     #keyword value 
# 2f = formet spesifier
content = "hello everyone how are you"

x = content.split()
print(x)
print(type(x))