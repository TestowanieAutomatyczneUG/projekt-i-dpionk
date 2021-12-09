class Dziennik:
	def __init__(self, lista_uczniow):
		self.lista_uczniow = lista_uczniow 

	def dodaj_ucznia(self, id_ucznia, imie_ucznia, nazwisko_ucznia):
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