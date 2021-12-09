import unittest
from src.sample.dziennik import *

class Dziennik_test(unittest.TestCase):

	def setUp(self):
		dziennik = Dziennik([])
		dziennik.dodaj_ucznia(1, 'Daria', 'Pionk')
		dziennik.dodaj_ucznia(2, 'Jan', 'Kowalski')
		dziennik.dodaj_ucznia(3, 'Kamil', 'Nowak')
		dziennik.dodaj_przedmiot(2, 'matematyka' )
		dziennik.dodaj_przedmiot(2, 'j. polski')
		dziennik.dodaj_przedmiot(1, 'matematyka' )
		dziennik.dodaj_ocene(2, 'matematyka', 6)
		dziennik.dodaj_ocene(2, 'matematyka', 3)
		dziennik.dodaj_ocene(2, 'matematyka', 6)
		dziennik.dodaj_uwage(2, 'Źle się zachowuje')
		dziennik.dodaj_uwage(2, 'Jest niegrzeczny')
		dziennik.dodaj_ocene(1, 'matematyka', 1)
		dziennik.dodaj_uwage(3, 'Uwaga')
		self.temp = dziennik

	def test_dodaj_ucznia_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}, {'id': 4, 'imie': 'Imie', 'nazwisko': 'Nazwisko', 'przedmioty': [], 'uwagi': []}], self.temp.dodaj_ucznia(4, 'Imie', 'Nazwisko'))
	
	def test_dodaj_ucznia_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}, {'id': 67, 'imie': 'Kazimierz', 'nazwisko': 'Maj', 'przedmioty': [], 'uwagi': []}], self.temp.dodaj_ucznia(67, 'Kazimierz', 'Maj'))

	def test_dodaj_ucznia_istniejace_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 1, 'Imie', 'Nazwisko')

	def test_dodaj_ucznia_puste_imie(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 7, '', 'Nazwisko')

	def test_dodaj_ucznia_puste_nazwisko(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 6, 'Imie', '')

	def test_dodaj_ucznia_nieprawidlowy_typ_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, [], 'Imie', 'Nazwisko')

	def test_dodaj_ucznia_nieprawidlowy_typ_id_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 3.4, 'Imie', 'Nazwisko')

	def test_dodaj_ucznia_nieprawidlowy_typ_imienia(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 4, 456, 'Nazwisko')

	def test_dodaj_ucznia_nieprawidlowy_typ_nazwiska(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, 4,'Imie', {})

	def test_dodaj_ucznia_nieprawidlowy_typ_argumentow(self):
		self.assertRaises(ValueError, self.temp.dodaj_ucznia, [], None, {})

	def test_usun_ucznia_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}]
		, self.temp.usun_ucznia(3))

	def test_usun_ucznia_sukces_2(self):
		self.assertEqual([{'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}]
		, self.temp.usun_ucznia(1))

	def test_usun_ucznia_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.usun_ucznia, 54)

	def test_usun_ucznia_nieprawidlowy_typ_id(self):
		self.assertRaises(ValueError, self.temp.usun_ucznia, {})

	def test_usun_ucznia_nieprawidlowy_typ_id_2(self):
		self.assertRaises(ValueError, self.temp.usun_ucznia, 45345.5676786786)

	def test_edytuj_ucznia_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Jan', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_ucznia(3, 'Jan', 'Nowak'))

	def test_edytuj_ucznia_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Maksymilian', 'nazwisko': 'Malinowski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_ucznia(2, 'Maksymilian', 'Malinowski'))

	def test_edytuj_ucznia_puste_nowe_imie(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 2,'', 'noweNazwisko')

	def test_edytuj_ucznia_puste_nowe_nazwisko(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 2,'noweImie', '')
	
	def test_edytuj_ucznia_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 54,'noweImie', 'noweNazwisko')

	def test_edytuj_ucznia_nieprawidlowy_typ_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, True,'noweImie', 'noweNazwisko')

	def test_edytuj_ucznia_nieprawidlowy_typ_id_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 5645465487.456342423,'noweImie', 'noweNazwisko')

	def test_edytuj_ucznia_nieprawidlowy_typ_imienia(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 2 , 4353543, 'noweNazwisko')

	def test_edytuj_ucznia_nieprawidlowy_typ_nazwiska(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, 2 , 'noweImie', None)

	def test_edytuj_ucznia_nieprawidlowy_typ_argumentow(self):
		self.assertRaises(ValueError, self.temp.edytuj_ucznia, True , {} , None)

	def test_dodaj_przedmiot_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.dodaj_przedmiot(3, 'j. polski'))

	def test_dodaj_przedmiot_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}, {'przedmiot': 'muzyka', 'oceny': []}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.dodaj_przedmiot(1, 'muzyka'))

	def test_dodaj_przedmiot_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_przedmiot, 54, 'j. polski')

	def test_dodaj_przedmiot_nieprawidlowy_typ_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_przedmiot, 54.556546, 'j. polski')

	def test_dodaj_przedmiot_nieprawidlowy_typ_id_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_przedmiot, True, 'j. polski')

	def test_dodaj_przedmiot_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.dodaj_przedmiot, True, 'sdfsdfsf')

	def test_dodaj_przedmiot_nieprawidlowy_przedmiot_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_przedmiot, True, {})

	def test_edytuj_przedmiot_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'informatyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_przedmiot(1, 'matematyka', 'informatyka'))

	def test_edytuj_przedmiot_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'plastyka', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_przedmiot(2, 'j. polski', 'plastyka'))

	def test_edytuj_przedmiot_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 2, 'sdfsdfsf', 'biologia')

	def test_edytuj_przedmiot_nieprawidlowy_przedmiot_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 2, None, 'matematyka')

	def test_edytuj_przedmiot_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 54, 'matematyka', 'informatyka')

	def test_edytuj_przedmiot_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 'dfgfdg', 'matematyka', 'informatyka')

	def test_edytuj_przedmiot_nieistniejacy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 3, 'matematyka', 'informatyka')

	def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 1, 'matematyka', 'sdfdsf')

	def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_przedmiot, 2, 'matematyka', [])

	def test_usun_przedmiot_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.usun_przedmiot(2, 'matematyka'))

	def test_usun_przedmiot_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.usun_przedmiot(1, 'matematyka'))

	def test_usun_przedmiot_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.usun_przedmiot, 54, 'matematyka')

	def test_usun_przedmiot_nieistniejacy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.usun_przedmiot, 3, 'matematyka')

	def test_usun_przedmiot_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.usun_przedmiot, 3, 'dgfdgfdg')

	def test_usun_przedmiot_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.usun_przedmiot, {}, 'matematyka')

	def test_usun_przedmiot_nieprawidlowe_argumenty(self):
		self.assertRaises(ValueError, self.temp.usun_przedmiot, None, 'dfgfdg')

	def test_dodaj_ocene_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.dodaj_ocene(1, 'matematyka', 1))

	def test_dodaj_ocene_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6, 5]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.dodaj_ocene(2, 'matematyka', 5))

	def test_dodaj_ocene_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 54, 'matematyka', 2)

	def test_dodaj_ocene_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, [], 'matematyka', 2)

	def test_dodaj_ocene_nieprawidlowa_ocena(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 2, 'matematyka', '56464')

	def test_dodaj_ocene_nieprawidlowa_ocena_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 2, 'matematyka', 5.75)

	def test_dodaj_ocene_nieistniejacy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 1, 'j. polski', 2)

	def test_dodaj_ocene_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 1, 'dfgfdgfdg', 2)

	def test_dodaj_ocene_nieprawidlowe_argumenty(self):
		self.assertRaises(ValueError, self.temp.dodaj_ocene, 44565.456456, 'dfgfdgfdg', {})

	def test_edytuj_oceny_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1, 1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_oceny(1, 'matematyka', [1,1,1,1]))

	def test_edytuj_oceny_sukces_2(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': [6, 6, 4]}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
		self.temp.edytuj_oceny(2, 'j. polski', [6, 6, 4]))

	def test_edytuj_oceny_nieprawidlowe_oceny(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny,1, 'matematyka', [5.75,5.5, 2])

	def test_edytuj_oceny_nieprawidlowe_oceny_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny,1, 'matematyka', [{}, 5, 6])

	def test_edytuj_oceny_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny, 54, 'matematyka', [2])

	def test_edytuj_oceny_nieprawidlowy_typ_ocen(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny, [], 'matematyka', 2)

	def test_edytuj_oceny_nieprawidlowy_typ_ocen_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny, [], 'matematyka', {'ocena': 3})

	def test_edytuj_oceny_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny, [], 'matematyka', [2])

	def test_edytuj_oceny_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.edytuj_oceny, 1, 'dfgfdgdfg', [2])

	def test_pokaz_statystyki_ucznia_sukces(self):
		self.assertEqual([['matematyka', 5.0], ['j. polski', 0]], self.temp.pokaz_statystyki_przedmiotow(2))

	def test_pokaz_statystyki_ucznia_sukces_2(self):
		self.assertEqual([], self.temp.pokaz_statystyki_przedmiotow(3))

	def test_pokaz_statystyki_ucznia_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotow, 54)

	def test_pokaz_statystyki_ucznia_nieprawidlowe__id(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotow, 54.456456546)

	def test_pokaz_statystyki_ucznia_nieprawidlowe__id_2(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotow, None)

	def test_pokaz_statystyki_ucznia_przedmiot_sukces(self):
		self.assertEqual([['matematyka', 5.0]], self.temp.pokaz_statystyki_przedmiotu(2, 'matematyka') )

	def test_pokaz_statystyki_ucznia_przedmiot_sukces_2(self):
		self.assertEqual([['j. polski', 0]], self.temp.pokaz_statystyki_przedmiotu(2, 'j. polski') )

	def test_pokaz_statystyki_ucznia_przedmiot_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, 54, 'matematyka')

	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, {}, 'matematyka')

	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id_2(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, 6.6699089, 'matematyka')

	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, 1, 'sdfsdf')
	@unittest.skip('Niezaimplementowane')
	def test_pokaz_statystyki_ucznia_przedmiot_nieistniejacy_przedmiot(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, 1, 'wychowanie fizyczne')

	def test_pokaz_statystyki_ucznia_nieprawidlowe_argumenty(self):
		self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, {}, None)

	def test_dodaj_uwage_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': 
[], 'uwagi': [{'uwaga': 'Uwaga'}, {'uwaga': 'Jest niegrzeczny'}]}],
self.temp.dodaj_uwage(3, 'Jest niegrzeczny'))

	def test_dodaj_uwage_sukces_2(self):
			self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]},
							  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											  {'przedmiot': 'j. polski', 'oceny': []}],
							   'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
							  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								  [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
							 self.temp.dodaj_uwage(1, 'nieprzygotowanie'))
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, 54, 'Uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_pusta_uwaga(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, 2, '')
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, 54.566454654, 'Uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_nieprawidlowe_id_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, [], 'Uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_nieprawidlowa_uwaga(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, 3, 45456)
	@unittest.skip('Niezaimplementowane')
	def test_dodaj_uwage_nieprawidlowa_uwaga_2(self):
		self.assertRaises(ValueError, self.temp.dodaj_uwage, 3, {})
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': 
[], 'uwagi': [{'uwaga': 'nowa uwaga'}]}], self.temp.edytuj_uwage(3, 'Uwaga', 'nowa uwaga'))
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_sukces_2(self):
			self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
							  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											  {'przedmiot': 'j. polski', 'oceny': []}],
							   'uwagi': [{'uwaga': 'Źle się zachowuje i przeszkadza na lekcji'}, {'uwaga': 'Jest niegrzeczny'}]},
							  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								  [], 'uwagi': [{'uwaga': 'Uwaga'}]}],
							 self.temp.edytuj_uwage(2, 'Źle się zachowuje', 'Źle się zachowuje i przeszkadza na lekcji'))
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieistniejace_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 54, 'uwaga', 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowe_id(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, None, 'uwaga', 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowe_id_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 6546546.6, 'uwaga', 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieistniejaca_uwaga(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 3, 'sfddsfsff', 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowa_nowa_uwaga(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 3, 'uwaga', 4569540)
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowa_nowa_uwaga_2(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 3, 'uwaga', ['dfgfdgfd'])
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_pusta_uwaga(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 3, '', 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_pusta_nowa_uwaga(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 3, 'uwaga', '')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowa_uwaga(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, 1, {}, 'nowa uwaga')
	@unittest.skip('Niezaimplementowane')
	def test_edytuj_uwage_nieprawidlowe_argumenty(self):
		self.assertRaises(ValueError, self.temp.edytuj_uwage, [], {}, True)
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_sukces(self):
		self.assertEqual([{'id': 1, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 5, 6]}, {'przedmiot': 'informatyka', 'oceny': [5]}], 'uwagi': []}, {'id': 2, 'imie': 'Maciej', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}, {'uwaga': 'Przeszkadza na zajeciach'}]}, {'id': 3, 'imie': 'Wojciech', 'nazwisko': 'Przykladowy', 'przedmioty': [{'przedmiot':
'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}],
		self.temp.importuj_dane('data/data1.csv'))
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_sukces_2(self):
		self.assertEqual([{'id': 2, 'imie': 'Franciszka', 'nazwisko': 'Sienkiewicz', 'przedmioty': [{'przedmiot': 'chemia', 'oceny': [1, 5, 6, 2, 3]}, {'przedmiot': 'plastyka', 'oceny': [5, 1, 2]}], 'uwagi': []}, {'id': 46, 'imie': 'Oliwier', 'nazwisko': 'Stanek', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}]}, {'id': 2173, 'imie': 'Maurycy', 'nazwisko': 'Kamiński', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6, 6, 6]}, {'przedmiot': 'geografia', 'oceny': [1, 2, 6]}, {'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}, {'id': 656, 'imie': 'August', 'nazwisko': 'Wrona', 'przedmioty': [], 'uwagi': []}, {'id': 1, 'imie': 'Maciej', 'nazwisko': 'Jeleń', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}],
						 self.temp.importuj_dane('data/data1_1.csv'))
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_zly_format_pliku(self):
		self.assertRaises(ValueError, self.temp.importuj_dane, 'idk/asd/sdfsf.jpg')
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_zly_format_pliku_2(self):
		self.assertRaises(ValueError, self.temp.importuj_dane, 'sdfsf')
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_zly_format_pliku_3(self):
		self.assertRaises(ValueError, self.temp.importuj_dane, [])
	@unittest.skip('Niezaimplementowane')
	def test_importuj_dane_zly_format_pliku_4(self):
		self.assertRaises(ValueError, self.temp.importuj_dane, 3)
	@unittest.skip('Niezaimplementowane')
	def test_eksportuj_dane_sukces(self):
		self.assertEqual(self.temp.lista_uczniow,  self.temp.eksportuj_dane('data/data2.csv'))
	@unittest.skip('Niezaimplementowane')
	def test_eksportuj_dane_zly_format_pliku(self):
		self.assertRaises(ValueError, self.temp.eksportuj_dane, 'data/sdfsf')
	@unittest.skip('Niezaimplementowane')
	def test_eksportuj_dane_zly_format_pliku_2(self):
		self.assertRaises(ValueError, self.temp.eksportuj_dane, [])
	@unittest.skip('Niezaimplementowane')
	def test_eksportuj_dane_zly_format_pliku_3(self):
		self.assertRaises(ValueError, self.temp.eksportuj_dane, 3)
	@unittest.skip('Niezaimplementowane')
	def test_eksportuj_dane_zly_format_pliku_4(self):
		self.assertRaises(ValueError, self.temp.eksportuj_dane, 'dfsdf.mp3')
	@unittest.skip('Niezaimplementowane')
	def test_daj_liste_uczniow(self):
		self.assertEqual([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
						   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
						  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
						   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
										  {'przedmiot': 'j. polski', 'oceny': []}],
						   'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
						  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [],
						   'uwagi': [{'uwaga': 'Uwaga'}]}],
						 self.temp.daj_liste_uczniow())

	def tearDown(self):
		self.temp = None

if __name__ == '__main__':
    unittest.main()