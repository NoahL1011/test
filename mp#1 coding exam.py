"""
Laudat_Noah
MP1_Exam
"""
fahrenheit = int(input("tempature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} = {celsius}C")
celsius_rounded = round(celsius, 1)
print(f"{fahrenheit} : {celsius_rounded}F")
if celsius_rounded < 0:
    print("Freezing Alert!")
elif celsius_rounded > 35:
    print("Heat Warning!")
else:
    print("Normal Tempature")