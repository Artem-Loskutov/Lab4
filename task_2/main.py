i_file = open("input.txt", 'r')
number = int(i_file.readline())
i_file.close()

count = 0
history = []

while number > 1:
    count+=1
    history.insert(0,number)
    if number % 3 == 0:
        number//=3
    elif (number-1) % 3 == 0:
        number-=1
    elif number % 2 == 0:
        number//=2
    else:
        number-=1

history.insert(0,1)

o_file = open("output.txt", 'w')
o_file.write(str(count) + '\n')
for i in history:
    o_file.write(str(i) + ' ')
o_file.close()
