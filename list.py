std_Names = ["Vaibhav","Nilesh","Ram"]
eng_marks = [50,60,70]
math_marks = [60,70,80]
scienceMark = [90,99,60]

for i in range(1):
    std_Names.append("Vishal")
    eng_marks.append(90)
    math_marks.append(70)
    scienceMark.append(80)
    
for i in range(len(std_Names)):
    print(std_Names[i]," has got ",eng_marks[i]," in English ",scienceMark[i]," in science and ",math_marks[i]," in maths")
