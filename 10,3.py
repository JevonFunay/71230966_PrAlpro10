pesanemail = {}
with open('mbox-short.txt', 'r') as file:
    for i in file:
        if i.startswith('From:'):
            pesanemail[i.split()[1]] = pesanemail.get(i.split()[1], 0) + 1
print(pesanemail)