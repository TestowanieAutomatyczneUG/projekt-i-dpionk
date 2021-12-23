import unittest
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher
from src.sample.dziennik import *

class MaUcznia(BaseMatcher):
	def __init__(self, imie,nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko
	
	def _matches(self, item):
		for i in item:
			if i['imie'] == self.imie and i['nazwisko'] == self.nazwisko:
				return True
		return False

def ma_ucznia(imie,nazwisko):
	return MaUcznia(imie,nazwisko)


class Dziennik_test_pyhamcrest(unittest.TestCase):

	def setUp(self):
		dziennik = Dziennik([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
		self.temp = dziennik

	def testInstance(self):
		assert_that(self.temp, is_(Dziennik))

	def testInstance_2(self):
		assert_that(self.temp, instance_of(Dziennik))

	def test_dodaj_ucznia_sukces(self):
		assert_that(self.temp.dodaj_ucznia(4, 'Imie', 'Nazwisko')), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}, {'id': 4, 'imie': 'Imie', 'nazwisko': 'Nazwisko', 'przedmioty': [], 'uwagi': []}])
	
	def test_dodaj_ucznia_sukces_2(self):
		assert_that(self.temp.dodaj_ucznia(5, 'Maciej', 'Kowalski'), has_length(4))

	def test_dodaj_ucznia_sukces_3(self):
		assert_that(self.temp.dodaj_ucznia(71, 'Maksymilian', 'Malinowski'), ma_ucznia('Maksymilian', 'Malinowski'))

	def test_dodaj_ucznia_istniejace_id(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( 1, 'Imie', 'Nazwisko'),raises(ValueError))
	
	def test_dodaj_ucznia_nieprawidlowy_typ_id(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( [], 'Imie', 'Nazwisko'),raises(ValueError))
	
	def test_dodaj_ucznia_nieprawidlowy_typ_id_2(self):
		assert_that(calling(self.temp.dodaj_ucznia).with_args( 3.4, 'Imie', 'Nazwisko'),raises(ValueError))

	def test_dodaj_ucznia_puste_imie(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( 7, '', 'Nazwisko'),raises(ValueError))

	def test_dodaj_ucznia_puste_nazwisko(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( 7, 'Imie', ''),raises(ValueError))
	
	def test_dodaj_ucznia_nieprawidlowy_typ_imienia(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( 4, 456, 'Nazwisko'),raises(ValueError))
	
	def test_dodaj_ucznia_nieprawidlowy_typ_nazwiska(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( 4,'Imie', {}),raises(ValueError))
	
	def test_dodaj_ucznia_nieprawidlowy_typ_argumentow(self):
		assert_that( calling(self.temp.dodaj_ucznia).with_args( [], None, {}),raises(ValueError))
	
	def test_usun_ucznia_sukces(self):
		assert_that(self.temp.usun_ucznia(3)) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}])

	def test_usun_ucznia_sukces_2(self):
		assert_that(self.temp.usun_ucznia(1)[0], has_entries({'id': equal_to(2)}))

	def test_usun_ucznia_nieistniejace_id(self):
		assert_that(calling (self.temp.usun_ucznia).with_args(54),raises(ValueError))
	
	def test_usun_ucznia_nieprawidlowy_typ_id(self):
		assert_that(calling (self.temp.usun_ucznia).with_args({}),raises(ValueError))
	
	def test_usun_ucznia_nieprawidlowy_typ_id_2(self):
		assert_that(calling (self.temp.usun_ucznia).with_args(45345.5676786786),raises(ValueError))
	
	def test_edytuj_ucznia_sukces(self):
		assert_that(self.temp.edytuj_ucznia(3, 'Jan', 'Nowak')) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Jan', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_edytuj_ucznia_sukces_2(self):
		assert_that(self.temp.edytuj_ucznia(1, 'Daria', 'Kowalska')), is_not(equal_to(self.temp))

	def test_edytuj_ucznia_nieistniejace_id(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(54,'noweImie', 'noweNazwisko'),raises(ValueError))
	
	def test_edytuj_ucznia_nieprawidlowy_typ_id(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(True,'noweImie', 'noweNazwisko'),raises(ValueError))
	
	def test_edytuj_ucznia_nieprawidlowy_typ_id_2(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(5645465487.456342423,'noweImie', 'noweNazwisko'),raises(ValueError))
	
	def test_edytuj_ucznia_nieprawidlowy_typ_imienia(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(2 , 4353543, 'noweNazwisko'),raises(ValueError))
	
	def test_edytuj_ucznia_nieprawidlowy_typ_nazwiska(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(2 , 'noweImie', None),raises(ValueError))

	def test_edytuj_ucznia_puste_nowe_imie(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(2,'', 'noweNazwisko'),raises(ValueError))

	def test_edytuj_ucznia_puste_nowe_nazwisko(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(2,'noweImie', ''),raises(ValueError))
	
	def test_edytuj_ucznia_nieprawidlowy_typ_argumentow(self):
		assert_that(calling (self.temp.edytuj_ucznia).with_args(True , {} , None),raises(ValueError))
	
	def test_dodaj_przedmiot_sukces(self):
		assert_that(self.temp.dodaj_przedmiot(3, 'j. polski')) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Uwaga'}]}])
	
	def test_dodaj_przedmiot_sukces_2(self):
		assert_that(self.temp.dodaj_przedmiot(1, 'informatyka')), is_not(equal_to(self.temp))

	def test_dodaj_przedmiot_nieistniejace_id(self):
		assert_that(calling (self.temp.dodaj_przedmiot).with_args(45567566, 'j. polski'),raises(ValueError))
	
	def test_dodaj_przedmiot_nieprawidlowy_typ_id(self):
		assert_that(calling (self.temp.dodaj_przedmiot).with_args(54.556546, 'j. polski'),raises(ValueError))
	
	def test_dodaj_przedmiot_nieprawidlowy_typ_id_2(self):
		assert_that(calling (self.temp.dodaj_przedmiot).with_args(True, 'j. polski'),raises(ValueError))
	
	def test_dodaj_przedmiot_nieprawidlowy_przedmiot(self):
		assert_that(calling (self.temp.dodaj_przedmiot).with_args(True, 'sdfsdfsf'),raises(ValueError))
	
	def test_dodaj_przedmiot_nieprawidlowy_przedmiot_2(self):
		assert_that(calling (self.temp.dodaj_przedmiot).with_args(True, {}),raises(ValueError))
	
	def test_edytuj_przedmiot_sukces(self):
		assert_that(self.temp.edytuj_przedmiot(1, 'matematyka', 'informatyka')) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'informatyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_edytuj_przedmiot_sukces_2(self):
		assert_that(self.temp.edytuj_przedmiot(2, 'j. polski', 'j. angielski')) , has_value('j. angielski')

	def test_edytuj_przedmiot_nieprawidlowy_przedmiot(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(2, 'sdfsdfsf', 'biologia'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieprawidlowy_przedmiot_2(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(2, None, 'matematyka'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieistniejace_id(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(546455675464, 'matematyka', 'informatyka'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieprawidlowe_id(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args('dfgfdg', 'matematyka', 'informatyka'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieistniejacy_przedmiot(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(3, 'matematyka', 'informatyka'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(1, 'matematyka', 'sdfdsf'),raises(ValueError))
	
	def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot_2(self):
		assert_that(calling (self.temp.edytuj_przedmiot).with_args(2, 'matematyka', []),raises(ValueError))
	
	def test_usun_przedmiot_sukces(self):
		assert_that(self.temp.usun_przedmiot(2, 'matematyka')) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],)

	def test_usun_przedmiot_sukces_2(self):
		assert_that(self.temp.usun_przedmiot(1, 'matematyka')), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_usun_przedmiot_nieistniejace_id(self):
		assert_that(calling (self.temp.usun_przedmiot).with_args(54, 'matematyka'),raises(ValueError))
	
	def test_usun_przedmiot_nieistniejacy_przedmiot(self):
		assert_that(calling (self.temp.usun_przedmiot).with_args(3, 'matematyka'),raises(ValueError))
	
	def test_usun_przedmiot_nieprawidlowy_przedmiot(self):
		assert_that(calling (self.temp.usun_przedmiot).with_args(3, 'dgfdgfdg'),raises(ValueError))
	
	def test_usun_przedmiot_nieprawidlowe_id(self):
		assert_that(calling (self.temp.usun_przedmiot).with_args({}, 'matematyka'),raises(ValueError))
	
	def test_usun_przedmiot_nieprawidlowe_argumenty(self):
		assert_that(calling (self.temp.usun_przedmiot).with_args(None, 'dfgfdg'),raises(ValueError))
	
	def test_dodaj_ocene_sukces(self):
		assert_that(self.temp.dodaj_ocene(1, 'matematyka', 1)) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],)

	def test_dodaj_ocene_sukces_2(self):
		assert_that(self.temp.dodaj_ocene(1,'matematyka', 1)[0]['przedmioty'][0]['oceny'], has_item(1))

	def test_dodaj_ocene_nieistniejace_id(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(54, 'matematyka', 2),raises(ValueError))
	
	def test_dodaj_ocene_nieprawidlowe_id(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args([], 'matematyka', 2),raises(ValueError))
	
	def test_dodaj_ocene_nieprawidlowa_ocena(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(2, 'matematyka', '56464'),raises(ValueError))
	
	def test_dodaj_ocene_nieprawidlowa_ocena_2(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(2, 'matematyka', 5.75),raises(ValueError))
	
	def test_dodaj_ocene_nieistniejacy_przedmiot(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(1, 'j. polski', 2),raises(ValueError))
	
	def test_dodaj_ocene_nieprawidlowy_przedmiot(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(1, 'dfgfdgfdg', 2),raises(ValueError))
	
	def test_dodaj_ocene_nieprawidlowe_argumenty(self):
		assert_that(calling (self.temp.dodaj_ocene).with_args(44565.456456, 'dfgfdgfdg', {}),raises(ValueError))
	
	def test_edytuj_oceny_sukces(self):
		assert_that(self.temp.edytuj_oceny(1, 'matematyka', [1,1,1,1])), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1, 1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_edytuj_oceny_sukces_2(self):
		assert_that(self.temp.edytuj_oceny(2, 'j. polski', [6, 6, 4])), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': [6, 6, 4]}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_edytuj_oceny_nieprawidlowe_oceny(self):
		assert_that(calling(self.temp.edytuj_oceny).with_args(1, 'matematyka', [5.75,5.5, 2]),raises(ValueError))

	def test_edytuj_oceny_nieprawidlowe_oceny_2(self):
		assert_that(calling(self.temp.edytuj_oceny).with_args(1, 'matematyka', [{}, 5, 6]),raises(ValueError))

	def test_pokaz_statystyki_ucznia_sukces(self):
		assert_that(self.temp.pokaz_statystyki_przedmiotow(2)) ,equal_to([['matematyka', 5.0], ['j. polski', 0]])

	def test_pokaz_statystyki_ucznia_sukces_2(self):
		assert_that(self.temp.pokaz_statystyki_przedmiotow(3), empty())
	
	def test_pokaz_statystyki_ucznia_nieistniejace_id(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotow).with_args(45456546456),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_nieprawidlowe__id(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotow).with_args(45456546456.45654464),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_nieprawidlowe__id_2(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotow).with_args(None),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_przedmiot_sukces(self):
		assert_that(self.temp.pokaz_statystyki_przedmiotu(2, 'matematyka')) ,equal_to([['matematyka', 5.0]])

	def test_pokaz_statystyki_ucznia_przedmiot_sukces_2(self):
		assert_that(self.temp.pokaz_statystyki_przedmiotu(2, 'j. polski')),equal_to([['j. polski', 0]])
	
	def test_pokaz_statystyki_ucznia_przedmiot_nieistniejace_id(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args(45456546456, 'matematyka'),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args([], 'matematyka'),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id_2(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args(6.6699089, 'matematyka'),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowy_przedmiot(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args(1, 'sdfsdf'),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_przedmiot_nieistniejacy_przedmiot(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args(1, 'wychowanie fizyczne'),raises(ValueError))
	
	def test_pokaz_statystyki_ucznia_nieprawidlowe_argumenty(self):
		assert_that(calling (self.temp.pokaz_statystyki_przedmiotu).with_args({}, None),raises(ValueError))
	
	def test_dodaj_uwage_sukces(self):
		assert_that(self.temp.dodaj_uwage(3, 'Jest niegrzeczny')) ,equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}, {'uwaga': 'Jest niegrzeczny'}]}])

	def test_dodaj_uwage_sukces_2(self):
		assert_that(self.temp.dodaj_uwage(1 ,'Nieprawidlowe zachowanie')[0]['uwagi'][0]['uwaga'], equal_to_ignoring_case('nieprawidlowe zachowanie'))

	def test_dodaj_uwage_nieistniejace_id(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args(4565454, 'Uwaga'),raises(ValueError))
	
	def test_dodaj_uwage_nieprawidlowe_id(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args(54.566454654, 'Uwaga'),raises(ValueError))
	
	def test_dodaj_uwage_nieprawidlowe_id_2(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args([], 'Uwaga'),raises(ValueError))
	
	def test_dodaj_uwage_nieprawidlowa_uwaga(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args( 3, 45456),raises(ValueError))
	
	def test_dodaj_uwage_nieprawidlowa_uwaga_2(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args( 3, {}),raises(ValueError))

	def test_dodaj_uwage_pusta_uwaga(self):
		assert_that(calling (self.temp.dodaj_uwage).with_args( 3, ''),raises(ValueError))

	def test_edytuj_uwage_sukces(self):
		assert_that(self.temp.edytuj_uwage(3, 'Uwaga', 'Nieprzygotowanie')), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
							{'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											{'przedmiot': 'j. polski', 'oceny': []}],
							'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
							{'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								[], 'uwagi': [{'uwaga': 'Nieprzygotowanie'}]}])
	
	def test_edytuj_uwage_sukces_2(self):
		assert_that(self.temp.edytuj_uwage(2, 'Źle się zachowuje', 'Źle się zachowuje i przeszkadza na lekcji')), equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
							{'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											{'przedmiot': 'j. polski', 'oceny': []}],
							'uwagi': [{'uwaga': 'Źle się zachowuje i przeszkadza na lekcji'}, {'uwaga': 'Jest niegrzeczny'}]},
							{'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								[], 'uwagi': [{'uwaga': 'Uwaga'}]}])

	def test_edytuj_uwage_nieistniejace_id(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 54, 'uwaga', 'nowa uwaga'),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowe_id(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args(  None, 'uwaga', 'nowa uwaga'),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowe_id_2(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 6546546.6, 'uwaga', 'nowa uwaga'),raises(ValueError))
	
	def test_edytuj_uwage_nieistniejaca_uwaga(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 3, 'sfddsfsff', 'nowa uwaga'),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowa_nowa_uwaga(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 3, 'uwaga', 4569540),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowa_nowa_uwaga_2(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 3, 'uwaga', ['dfgfdgfd']),raises(ValueError))

	def test_edytuj_uwage_pusta_uwaga(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 3, '', 'nowa uwaga'),raises(ValueError))

	def test_edytuj_uwage_pusta_nowa_uwaga(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 3, 'uwaga', ''),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowa_uwaga(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( 1, {}, 'nowa uwaga'),raises(ValueError))
	
	def test_edytuj_uwage_nieprawidlowe_argumenty(self):
		assert_that(calling (self.temp.edytuj_uwage).with_args( [], {}, True),raises(ValueError))

	def test_importuj_dane_sukces(self):
		assert_that(self.temp.importuj_dane('../data/data1.csv'), equal_to([{'id': 1, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 5, 6]}, {'przedmiot': 'informatyka', 'oceny': [5]}], 'uwagi': []}, {'id': 2, 'imie': 'Maciej', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}, {'uwaga': 'Przeszkadza na zajeciach'}]}, {'id': 3, 'imie': 'Wojciech', 'nazwisko': 'Przykladowy', 'przedmioty': [{'przedmiot':
'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}]))
	
	def test_importuj_dane_sukces_2(self):
		assert_that(self.temp.importuj_dane('../data/data1_1.csv')),equal_to([{'id': 2, 'imie': 'Franciszka', 'nazwisko': 'Sienkiewicz', 'przedmioty': [{'przedmiot': 'chemia', 'oceny': [1, 5, 6, 2, 3]}, {'przedmiot': 'plastyka', 'oceny': [5, 1, 2]}], 'uwagi': []}, {'id': 46, 'imie': 'Oliwier', 'nazwisko': 'Stanek', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}]}, {'id': 2173, 'imie': 'Maurycy', 'nazwisko': 'Kamiński', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6, 6, 6]}, {'przedmiot': 'geografia', 'oceny': [1, 2, 6]}, {'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}, {'id': 656, 'imie': 'August', 'nazwisko': 'Wrona', 'przedmioty': [], 'uwagi': []}, {'id': 1, 'imie': 'Maciej', 'nazwisko': 'Jeleń', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}],)

	def test_importuj_dane_zly_format_pliku(self):
		assert_that(calling (self.temp.importuj_dane).with_args('sdfsf.jpg'),raises(ValueError))

	def test_importuj_dane_zly_format_pliku_2(self):
		assert_that(calling (self.temp.importuj_dane).with_args('sdfsf'),raises(ValueError))

	def test_importuj_dane_zly_format_pliku_3(self):
		assert_that(calling (self.temp.importuj_dane).with_args([]),raises(ValueError))

	def test_importuj_dane_zly_format_pliku_4(self):
		assert_that(calling (self.temp.importuj_dane).with_args(3),raises(ValueError))

	def test_eksportuj_dane_sukces(self):
		assert_that(self.temp.eksportuj_dane('../data/data2.csv')), equal_to(self.temp.lista_uczniow)

	def test_eksportuj_dane_zly_format_pliku(self):
		assert_that(calling (self.temp.eksportuj_dane).with_args('tyutuy'),raises(ValueError))

	def test_eksportuj_dane_zly_format_pliku_2(self):
		assert_that(calling (self.temp.eksportuj_dane).with_args({}),raises(ValueError))

	def test_eksportuj_dane_zly_format_pliku_3(self):
		assert_that(calling (self.temp.eksportuj_dane).with_args(545.654),raises(ValueError))

	def test_eksportuj_dane_zly_format_pliku_4(self):
		assert_that(calling (self.temp.eksportuj_dane).with_args('dfsdf.js'),raises(ValueError))

	def tearDown(self):
		self.temp = None


if __name__ == '__main__':
	unittest.main()