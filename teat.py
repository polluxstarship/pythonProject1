class aa():
    def __init__(self):
        self.ab = [1,2,3]

lili = []
for i in range(1,4):
    globals()['hello'+str(i)] = aa()
    lili.append(globals()['hello'+str(i)])

print(hello1.ab)
print(hello2.ab)
print(hello3.ab)

for oo in lili:
    print(oo.ab)