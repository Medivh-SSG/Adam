class Genshin():
    def __init__(self, name, stars, eye, category, weapon, role):
        self.name = name
        self.stars = stars
        self.eye = eye
        self.category = category
        self.weapon = weapon
        self.role = role
    
    def stars_Genshin(self):
        if(self.stars==4):
            print('%s is 4-stars' %self.name)
        else:
            print('%s is 5-stars'%self.name)
     
    def eye_Genshin(self):
        if(self.eye=="piro"):
            print('%s имеет пиро глаз бога' %self.name)
        elif(self.eye=="aqua"):
            print('%s имеет аква глаз бога' %self.name)
        elif(self.eye=="krio"):
            print('%s имеет крио глаз бога' %self.name)
        elif(self.eye=="dendro"):
            print('%s имеет дендро глаз бога' %self.name)
        elif(self.eye=="electro"):
            print('%s имеет электро глаз бога' %self.name)
        elif(self.eye=="anemo"):
            print('%s имеет анемо глаз бога' %self.name)
            
    def category_Genshin(self):
        if(self.category =='LyYue'):
            print('%s персонаж из ЛиЮэ' %self.name)
        else:
            print(' %s персонаж из Монштадта' %self.name)
            
    def weapon_Genshin(self):
        if(self.weapon =='spear'):
            print('%s использует копье'%self.name)
        elif(self.weapon =='greatsword'):
            print( '%s использует большой меч'%self.name)
        elif(self.weapon =='bow'):
            print('%s использует лук'%self.name)
        elif(self.weapon =='book'%self.name):
            print('%s использует книгу'%self.name)
        elif(self.weapon =='sword'):
            print('%s использует меч'%self.name)
    def role_Genshin(self):
        if(self.role =='support'):
            print('%s выступает в роли поддержки'%self.name)
        else:
            print('%s выступает в роли основы'%self.name)

                           
Genshin1 = Genshin('СянЛин', 4, 'piro', 'LyYue', 'spear', 'support')
Genshin1.stars_Genshin()
Genshin1.eye_Genshin()
Genshin1.category_Genshin()
Genshin1.weapon_Genshin()
Genshin1.role_Genshin()

class PvP(Genshin):
    def _init_(self, name, stars, eye, category, weapon, role):
        super().__init__(stars, eye, category, weapon, role)
    def category_Genshin(self):
        if(self.category =="LyYue"):
            print("%s персонаж из ЛиЮэ" %self.name)
        elif(self.category =="Monshtadt"):
            print("%s персонаж из Монштадт" %self.name)
        elif(self.category =="Inadzuma"):
            print("%s персонаж из Инадзумы" %self.name)
    def role_Genshin(self):
        if(self.role =='support'):
            print('%s выступает в роли поддержки'%self.name)
        elif(self.role =='carry'):
            print('%s выступает в роли основы'%self.name)
        elif(self.role =='halfsupport'):
            print('%s выступает в роли полуподдержки'%self.name)
            
PvP1 = PvP('Кадзуха', 5, 'anemo', 'Inadzuma', 'sword', 'halfsupport')
PvP1.category_Genshin()
PvP1.role_Genshin()