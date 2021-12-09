class Dziennik:
	def __init__(self, lista_uczniow):
		self.lista_uczniow = lista_uczniow 

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
		if not nowe_imie_ucznia or not nowe_nazwisko_ucznia:
			raise ValueError('Podano złe argumenty')
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['imie'] = nowe_imie_ucznia
				i['nazwisko'] = nowe_nazwisko_ucznia
				return self.lista_uczniow
		raise ValueError('Nie ma takiego ucznia w bazie')

	def dodaj_przedmiot(self, id_ucznia, przedmiot):
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['przedmioty'].append({
					'przedmiot' : przedmiot,
					'oceny' : []
				})
				return self.lista_uczniow

	def dodaj_ocene(self, id_ucznia, przedmiot, ocena):
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				for j in i['przedmioty']:
					if j['przedmiot'] == przedmiot:
						j['oceny'].append(ocena)
						return self.lista_uczniow

	def dodaj_uwage(self, id_ucznia, uwaga):
		for i in self.lista_uczniow:
			if i['id'] == id_ucznia:
				i['uwagi'].append({
					'uwaga': uwaga
				})
				return self.lista_uczniow