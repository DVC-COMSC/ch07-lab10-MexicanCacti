# ******************************
# Make your Code
# ******************************
value = input().split()
values = []
for i in range(len(value)):
    values.append(value[i])

for i in range(len(values)):
    min = i
    for k in range(i,len(values),1):
        if int(values[min]) > int(values[k]):
            min = k
    if min == i:
        print(values)
        continue
    else:
        temp = values[i]
        values[i] = values[min]
        values[min] = temp
        print(values)