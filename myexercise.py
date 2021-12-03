import sys
student_dict = {}
with open("C:/users/y/desktop/py/exercise/student.txt","r",encoding="utf-8") as file:
    for line in file:
        line = line.strip(" /n")
        name,university = line.split(":")
        student_dict[name] = university
inpt = sys.argv[1] 
liste = inpt.split(",")       


for name in liste:
    try:
        if name not in student_dict.keys():
            raise NameError("No record of {} was found!\n")
        else:
            file.write(f"Name: {name}, University: {student_dict[name]}")
    except NameError:
        print("No record of {name} was found!\n")
            