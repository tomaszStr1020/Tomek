import sys

var = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z' + var.lower()
cons = var[:9].lower()
fun = var[9:28].lower()
pred = var[28:51].lower()
all = ['FORALL', '∀']
exists = ['∃', 'EXISTS']
neg = ['~', 'NOT', '¬']
kon = ['AND', '^', '&']
dys = ['OR', '∨']
imp = ['IMPLIES', '→']
rown = ['IFF', ' ↔']
alt_w = ['XOR', ' ⊕']
operators = [neg, kon, dys, imp, rown, alt_w]
existors = [exists, all]
stos = []
tup = 0
while True:
    x = input('*** START I KONTYNUACJA: 1 *** KONIEC PROGRAMU: 2 ***')
    if x == '2':
        sys.exit()
    elif x == '1':
        onp = input().split()
        for i in onp:
            if i[0] in letters:
                if i[0] in cons:
                    stos.append(i)
                if i[0] in fun or i[0] in pred:
                    x = []
                    x.append(i[0])
                    x.append('(')
                    for g in range(int(i[2])):
                        x.append(stos.pop())
                        x.append(',')
                    x.append(')')
                    x.pop(-2)
                    stos.append(''.join(x))
                if i[0] in var and len(i) == 1:
                    stos.append(i)

            if i in all or i in exists:
                pol = 0
                temporary = []
                while pol == 0:
                    temporary.insert(0, stos.pop())
                    if temporary[0] in var:
                        temporary.insert(0, i)
                        temporary.insert(1, ' ')
                        stos.append(''.join(temporary))
                        pol += 1
                    else:
                        temporary.insert(0, '(')
                        temporary.append(')')

            if i in neg:
                neg_temp = []
                neg_temp.append(i)
                neg_temp.append('(')
                neg_temp.append(stos.pop())
                neg_temp.append(')')
                stos.append(''.join(neg_temp))

            if any(i in sl for sl in operators):
                temp_oper = []
                temp_oper.append('(')
                temp_oper.append(')')
                temp_oper.append('(')
                temp_oper.append(')')
                temp_oper.insert(3,stos.pop())
                temp_oper.insert(1, stos.pop())
                temp_oper.insert(3, i)
                stos.append(''.join(temp_oper))
        print(stos[tup])
        tup+=1
