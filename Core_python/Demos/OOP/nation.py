class Nation:
    def setLang(self, name, pop, lang):
        self.nm = name
        self.p = pop
        self.lang = lang

    def getLang(self):

        print(f'Name : {self.nm}')
        print(f'Name : {self.p}')
        print(f'India speaks "{self.lang}" Language')


nt = Nation()
nt.setLang("India", 1500000, 'Hindi')
nt.getLang()
