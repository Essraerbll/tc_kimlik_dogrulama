def tckimlik(tc):
    list = []
    for i in tc:
        list.append(int(i))

    if len(list) != 11:
        return "Your TC should be 11 characters long."
    if list[0] == 0:
        return "The first digit of TC cannot be 0."

    sum = 0
    for i in range(len(list) - 1):
        sum += list[i]

    if sum % 10 == list[10]:
        return True
    else:
        return False

while True:
    tc = input("Enter your TC: ")
    result = tckimlik(tc)
    if result == True:
        print("Valid TC!")
        break
    else:
        print(result)
