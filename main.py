# ******************************
# Make your Code
# ******************************
value = input().split()
values = []
for i in range(len(value)):
    values.append(value[i])

for i in range(len(values)):
    min = -1
    for k in range(i,len(values),1):
        if int(values[i]) > int(values[k]):
            min = k
    if min == -1:
        continue
    else:
        temp = values[i]
        values[i] = values[min]
        values[min] = temp
        print(values)



#for j in range(i + 1,len(values),1):
        ##if int(values[j]) < int(values[i]):
            ##temp = values[i]
            ##values[i] = values[j]
            ##values[j] = temp
            ##print(values)
