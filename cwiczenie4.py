"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 2
Zadanie 4
"""

class Budynek(object):
    stan_budynku="bardzo dobry"
    def __init__(self, adres, rok_budowy, sr_czynsz):
        self.adres=adres
        self.rok_budowy=rok_budowy
        self.sr_czynsz=sr_czynsz
    def remont_duzy(self):
        self.stan_budynku=" bardzo dobry"
        self.sr_czynsz+=200
        return self.stan_budynku,self.sr_czynsz
    def uplyw_czasu(self):
        self.stan_budynku="bardzo zly"
        self.sr_czynsz+=50
        return self.stan_budynku,self.sr_czynsz
        
class Lokal(Budynek):
    def __init__(self, wlasciciel, ilosc_pomieszczen, czynsz):
        self.wlasciciel=wlasciciel
        self.ilosc_pomieszczen=ilosc_pomieszczen
        self.czynsz=czynsz
    def remont_maly(self):
        self.stan="dobry"
        return self.stan
    def uplyw_czasu(self):
        self.stan="zly"
        return self.stan
class LokalMieszkalny(Lokal):
    funkcja="mieszkalny"
    koszty_media_os=70
    podatek_smieci_os=10
    def __init__(self, ilosc_osob_zamieszkalych, czynsz):
        self.ilosc_osob_zamieszkalych=ilosc_osob_zamieszkalych
        self.czynsz=czynsz
    def koszty(self):
        koszty=self.koszty_media_os*self.ilosc_osob_zamieszkalych+self.podatek_smieci_os*self.ilosc_osob_zamieszkalych+self.czynsz
        return koszty
class LokalBiurowy(Lokal):
    funkcja="biurowy"
    koszty_media_os=120
    podatek_smieci_os=5
    def __init__(self, ilosc_osob_pracujacych):
        self.ilosc_osob_pracujacych=ilosc_osob_pracujacych
    def koszty(self):
        koszty=self.koszty_media*ilosc_osob_pracujacych+self.podatek_smieci*ilosc_osob_pracujacych+self.czynsz
        return koszty
class Pokoj(object):
    porzadek=True
    def __init__(self, metraz):
        self.metraz=metraz
    def uplyw_czasu(self):
        porzadek=False
        return porzadek
    def zrob_porzadek(self):
        porzadek=True
        return porzadek
    def czy_jest_porzadek(self):
        return "Czy w pokoju jest porzadek? "+str(self.porzadek)
	def getMetraz(self):
        return self.__metraz
    def setReal(self,metraz):
        self.__metraz=metraz
    metraz=property(getMetraz,setMetraz)
class Kuchnia(Pokoj):
    rodzaj="kuchnia"
    def __init__(self):
        pass

blok1=Budynek("Pl.Grunwaldzki 16",1999,800)
lokal1=Lokal("Kowalski", 3, 500)
kuchnia=Kuchnia()
mieszkanie1=LokalMieszkalny(4,900)
    
