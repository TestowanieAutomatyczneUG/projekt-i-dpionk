import csv
import re


class Dziennik:
	def __init__(self, lista_uczniow):
		self.lista_uczniow = lista_uczniow 
		self.przedmioty = ['j. polski', 'j. angielski', 'historia', 'matematyka', 'geografia', 'biologia', 'fizyka', 'chemia', 'plastyka', 'muzyka', 'informatyka', 'wychowanie fizyczne']
		self.oceny = [1, 2, 3, 4, 5, 6]

	def dodaj_ucznia(self, id_ucznia, imie_ucznia, nazwisko_ucznia):
		if type(id_ucznia) is not int or type(imie_ucznia) is not str or type(nazwisko_ucznia) is not str or not imie_ucznia or not nazwisko_ucznia:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				raise ValueError('W bazie już jest taki uczeń')
		self.lista_uczniow.append({
			'id': id_ucznia,
			'imie': imie_ucznia,
			'nazwisko': nazwisko_ucznia,
			'przedmioty': [],
			'uwagi': []
		})
		return self.lista_uczniow

	def usun_ucznia(self, id_ucznia):
		if type(id_ucznia) is not int:
			raise ValueError('Podano zły argument')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				self.lista_uczniow.remove(i)
				return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def edytuj_ucznia(self,id_ucznia, nowe_imie_ucznia, nowe_nazwisko_ucznia):
		if type(id_ucznia) is not int or type(nowe_imie_ucznia) is not str or type(nowe_nazwisko_ucznia) is not str or not nowe_imie_ucznia or not nowe_nazwisko_ucznia:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['imie'] = nowe_imie_ucznia
				i['nazwisko'] = nowe_nazwisko_ucznia
				return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def dodaj_przedmiot(self, id_ucznia, przedmiot):
		if type(id_ucznia) is not int:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['przedmioty'].append({
					'przedmiot' : przedmiot,
					'oceny' : []
				})
				return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def edytuj_przedmiot(self, id_ucznia, przedmiot, nowyPrzedmiot):
		if type(id_ucznia) is not int or przedmiot not in self.przedmioty or nowyPrzedmiot not in self.przedmioty:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						j['przedmiot'] = nowyPrzedmiot
						return self.lista_uczniow
				raise ValueError('Ten uczeń nie ma takiego przedmiotu na liście')
		raise ValueError('Nie ma takiego ucznia w bazie')

	def usun_przedmiot(self, id_ucznia, przedmiot):
		if type(id_ucznia) is not int or przedmiot not in self.przedmioty:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						i['przedmioty'].remove(j)
						return self.lista_uczniow
				raise ValueError('Ten uczeń nie ma takiego przedmiotu na liście')
		raise ValueError('Nie ma takiego ucznia w bazie')

	def dodaj_ocene(self, id_ucznia, przedmiot, ocena):
		if type(id_ucznia) is not int or ocena not in self.oceny or przedmiot not in self.przedmioty:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						j['oceny'].append(ocena)
						return self.lista_uczniow
				raise ValueError('Ten uczeń nie ma takiego przedmiotu na liście')	
		raise ValueError('Nie ma takiego ucznia w bazie')

	def edytuj_oceny(self, id_ucznia, przedmiot, nowe_oceny):
		if type(id_ucznia) is not int or przedmiot not in self.przedmioty or type(nowe_oceny) is not list:
			raise ValueError('Podano złe argumenty')
		for o in nowe_oceny:
			if o not in self.oceny:
				raise ValueError('Podano złe oceny')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						j['oceny'] = nowe_oceny
						return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def dodaj_uwage(self, id_ucznia, uwaga):
		if type(id_ucznia) is not int or type(uwaga) is not str or not uwaga:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['uwagi'].append({
					'uwaga': uwaga
				})
				return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def edytuj_uwage(self, id_ucznia, tresc_uwagi, nowa_tresc_uwagi ):
		if type(id_ucznia) is not int or type(tresc_uwagi) is not str or type(nowa_tresc_uwagi) is not str or not tresc_uwagi or not nowa_tresc_uwagi:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['uwagi']:
					if j['uwaga'] == tresc_uwagi:
						j['uwaga'] = nowa_tresc_uwagi
						return self.lista_uczniow
				raise ValueError('Uczeń nie ma takiej uwagi')
		raise ValueError('Nie ma takiego ucznia w bazie')

	def pokaz_statystyki_przedmiotow(self, id_ucznia):
		if type(id_ucznia) is not int:
			raise ValueError('Podano zły argument')
		statystyki = []
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					srednia_z_przedmiotu = []
					srednia_z_przedmiotu.append(j['przedmiot'])
					srednia = 0
					if len(j['oceny']) > 0:
						for o in j['oceny']:
								srednia += o
						srednia = srednia / len(j['oceny'])
					srednia_z_przedmiotu.append(round(srednia,2))
					statystyki.append(srednia_z_przedmiotu)
				return statystyki
		raise ValueError('Nie ma takiego ucznia w bazie')
	
	def pokaz_statystyki_przedmiotu(self, id_ucznia, przedmiot):
		if type(id_ucznia) is not int or przedmiot not in self.przedmioty:
			raise ValueError('Podano złe argumenty')
		statystyki = []
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						srednia_z_przedmiotu = []
						srednia_z_przedmiotu.append(j['przedmiot'])
						srednia = 0
						if len(j['oceny']) > 0:
							for o in j['oceny']:
									srednia += o
							srednia = srednia / len(j['oceny'])
						srednia_z_przedmiotu.append(round(srednia,2))
						statystyki.append(srednia_z_przedmiotu)
						return statystyki
				raise ValueError('Ten uczeń nie ma takiego przedmiotu na liście')
		raise ValueError('Nie ma takiego ucznia w bazie')
	def importuj_dane(self, plik):
		if type(plik) is not str:
			raise ValueError('Podano zły format pliku')
		match = re.search('([a-zA-Z0-9\s_\\.\-\(\):])+(.csv)$', plik)
		if match:
				with open(plik, 'r', encoding='utf_8_sig') as csvfile:
					csvreader = csv.reader(csvfile, delimiter=';')
					tablica = []
			
					for row in csvreader:
						id = False
						imie = False
						nazwisko = False
						przedmiot = [False, False]
						oceny = False
						uwagi = False
						obiekt = {'id' : None, 'imie': None, 'nazwisko' : None, 'przedmioty': [], 'uwagi': [] }
						for element in row:		
							if id:
								obiekt['id'] = int(element)
								id = False				
							if element == 'id':
								id = True
							if imie:
								obiekt['imie'] = element
								imie = False
							if element == 'imie':
								imie = True
							if nazwisko:
								obiekt['nazwisko'] = element
								nazwisko = False
							if element == 'nazwisko':
								nazwisko = True
							if uwagi:
								obiekt['uwagi'].append(
									{
										'uwaga': element
									}
								)
							if element == 'uwagi':
								uwagi = True
								przedmiot = [False, False]
								oceny = False	
							if przedmiot[1]:
								obiekt['przedmioty'].append({
									'przedmiot': element,
									'oceny': []
								})
								przedmiot = [True, False, element]
							if przedmiot[0] and oceny and element in self.przedmioty :
								obiekt['przedmioty'].append({
									'przedmiot': element,
									'oceny': []
								})
								przedmiot = [True, False, element]
							if przedmiot[0] and oceny and element not in [ 'oceny','j. polski', 'j. angielski', 'historia', 'matematyka', 'geografia', 'biologia', 'fizyka', 'chemia', 'plastyka', 'muzyka', 'informatyka', 'wychowanie fizyczne']:
								
								for i in obiekt['przedmioty']:
									if i['przedmiot'] == przedmiot[2]:
										i['oceny'].append(int(element))
										
							if przedmiot[0] and element == 'oceny':
								oceny = True
							if element == 'przedmioty':
								przedmiot = [True, True]
						tablica.append(obiekt)
				self.lista_uczniow = tablica
				return self.lista_uczniow
		else:
			raise ValueError('Podano zły format pliku')

	def eksportuj_dane(self, plik):
			match = re.search('([a-zA-Z0-9\s_\\.\-\(\):])+(.csv)$', plik)
			if match:
				with open(plik, 'w', newline='', encoding='utf_8_sig') as csvfileToWrite:
					writer = csv.writer(csvfileToWrite, delimiter=';')
					do_napisania = []

					for i in self.lista_uczniow:
						wiersz = []
						for j in i:
							if j == 'id':
								wiersz.append('id')
							if j == 'imie':
								wiersz.append('imie')
							if j == 'nazwisko':
								wiersz.append('nazwisko')
							if j == 'przedmioty':
								wiersz.append('przedmioty')
							if wiersz[-1] in ['id', 'imie', 'nazwisko']:
								wiersz.append(i[j])
							if wiersz[-1] == 'przedmioty':
								for z in i[j]:
									if 'przedmiot' in z:
										wiersz.append(z['przedmiot'])
										wiersz.append('oceny')
										for o in z['oceny']:
											wiersz.append(o)
								wiersz.append('uwagi')
							if wiersz[-1] == 'uwagi':
								for z in i[j]:
									if 'uwaga' in z:
										wiersz.append(z['uwaga'])	
						do_napisania.append(wiersz)
					for w in do_napisania:
						writer.writerow(w)
				self.importuj_dane(plik)
				return self.lista_uczniow
			else:
				raise ValueError('Podano zły format pliku')