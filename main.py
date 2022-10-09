# ******************************
# Make your Code
# ******************************
value = input().split()
values = []

for i in range(len(value)):
    values.append(value[i])

for i in range(len(values)):
    for j in range(i + 1,len(values),1):
        if int(values[j]) < int(values[i]):
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
            print(values)