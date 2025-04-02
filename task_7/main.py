i_file = open("input.txt", 'r')
template = (i_file.readline())[:-1]
word = i_file.readline()
i_file.close()

i = 0
while i < len(template):
    if template[i] == '?':
        word = word[:i] + word[(i+1):]
        template = template.replace('?','',1)
    elif template[i] == '*' and (i+1) < len(template) and template[i+1]!='?':
        letter = template[i+1]
        while word[i] != letter and i <= len(word):
            word = word[:i] + word[(i+1):]
        template = template.replace('*','',1)
    elif template[i] == '*' and (i + 1) == len(template):
        word = word[:i]
        template = template.replace('*', '', 1)
    else:
        i+=1

o_file = open("output.txt", 'w')
if template == word: o_file.write("YES")
else: o_file.write("NO")
o_file.close()
