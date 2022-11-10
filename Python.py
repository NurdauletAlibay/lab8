var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
var_3 = int(input("Введите третье число: "))
var_4 = int(input("Введите четвертое число: "))
agregator = []
agregator.append(var_1)
agregator.append(var_2)
agregator.append(var_3)
agregator.append(var_4)
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            for l in range(0, 4):
            if(i != j & j != k & k != l & l != i):
                print(agregator[i], agregator[j], agregator[k], agregator[l])