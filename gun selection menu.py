#lists of gun available
guns_available = ['mp40','mp5']

#customisable class for guns

class Guns():
    def __init__(self,name,rate_of_fire,damage,range,skins_available):
        self.name = name
        self.rate_of_fire = rate_of_fire
        self.damage = damage
        self.range = range
        self.skins_available = skins_available

#actual gun class 

class mp40(Guns):
    def __init__(self):
        self.name = 'MP40'
        self.rate_of_fire = 6
        self.damage = 24
        self.range = 25
        self.skins_available = 10
    def mp40era(self):
        print(f'wow ! you choosed mp40 which have these attributes . name : {self.name} | range : {self.range} | damage : {self.damage} | skins_available : {self.skins_available} | rate_of_fire : {self.rate_of_fire}')

#prints all guns available in list
for x in guns_available:
    print(x)

#basic logics to call classes

print('currently these are the guns added .')
choose = input('please choose your gun : ')

#simple if/elif/else statements ...

if choose == 'mp40':
    mp = mp40()
    mp.mp40era()
else:
    print('no guns of this name available')