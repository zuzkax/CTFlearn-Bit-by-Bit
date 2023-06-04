import base64
import operator


#making variables: "text" and "operations"
print("enter base64:")
code_base64 = str(input())

encode_code = base64.standard_b64decode(code_base64)
print(base64.standard_b64decode(code_base64))

text = []
operations = []

for i in range(0, len(encode_code)):
    if encode_code[i] < 97 or encode_code[i] > 122:
        operations.append(chr(encode_code[i]))
    else:
        text.append(str(chr(encode_code[i])))



#conversion characters to numbers=========================
numbers = []
for letter in text:
    numbers.append(ord(letter)**3)

# checking for rshift====================================

for x in range(0, len(operations)-1):
    if operations[x] == '>':
        operations[x] = '>>'
        operations.pop(x+1)

#print(operations)

# list(dict) of operators=============================

op = {
    '>>': operator.rshift,
    '^': operator.xor,
    '|' : operator.or_,
    '&' : operator.and_,
    '~' : operator.invert
}
#print(text)
#print(numbers)

#===================================================


v = numbers[0]
for i in range(0,len(text)-1):
    for j in range(i+1,len(text)):
        oper = op[operations[j-1]]
        if oper != operator.invert:
            v = oper(v,numbers[j])
        else:
            v = oper(v)

print(v)