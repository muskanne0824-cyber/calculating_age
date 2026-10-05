from datetime import datetime as dt

now = dt.now()
print(now.date())
print(now.time())

birth_date = input("Enter your birth date : DD-MM-YYYY : ")
#converting string to date
birth_date = dt.strptime(birth_date,"%d-%m-%Y")

age = now.year - birth_date.year
print(age)

if (now.month, now.day)<(birth_date.month , birth_date.day):
    age -= 1

print("Your age is : ", age) 