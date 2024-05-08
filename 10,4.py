domain = {}
with open('mbox-short.txt', 'r') as file:
    for i in file:
        i = i.strip()
        if i.startswith('From:'):
            domain[i.split('@')[1]] = domain.get(i.split('@')[1], 0) + 1
print(domain)