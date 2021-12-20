import unittest
from assertpy import *
from src.sample.dziennik import *

def ma_przedmiot(self, id, przedmiot):
	for i in self.val:
		if i['id'] ==id :
			for p in i['przedmioty']:
				if p['przedmiot'] == przedmiot:
					return self
	return self.error('Uczeń nie ma takiego przedmiotu na liście!')

add_extension(ma_przedmiot)
			
class Dziennik_test_assertpy(unittest.TestCase):

    def setUp(self):
        dziennik = Dziennik([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        self.temp = dziennik

    def testInstance(self):
        assert_that(self.temp).is_instance_of(Dziennik)

    def test_dodaj_ucznia_sukces(self):
        assert_that(self.temp.dodaj_ucznia(4, 'Imie', 'Nazwisko')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}, {'id': 4, 'imie': 'Imie', 'nazwisko': 'Nazwisko', 'przedmioty': [], 'uwagi': []}])
    
    def test_dodaj_ucznia_sukces_2(self):
        assert_that(self.temp.dodaj_ucznia(5, 'Maciej', 'Kowalski')).is_iterable

    def test_dodaj_ucznia_istniejace_id(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 1, 'Imie', 'Nazwisko')
    
    def test_dodaj_ucznia_nieprawidlowy_typ_id(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( [], 'Imie', 'Nazwisko')
    
    def test_dodaj_ucznia_nieprawidlowy_typ_id_2(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 3.4, 'Imie', 'Nazwisko')

    def test_dodaj_ucznia_puste_imie(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 7, '', 'Nazwisko')

    def test_dodaj_ucznia_puste_nazwisko(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 7, 'Imie', '')
    
    def test_dodaj_ucznia_nieprawidlowy_typ_imienia(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 4, 456, 'Nazwisko')
    
    def test_dodaj_ucznia_nieprawidlowy_typ_nazwiska(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( 4,'Imie', {})
    
    def test_dodaj_ucznia_nieprawidlowy_typ_argumentow(self):
        assert_that(self.temp.dodaj_ucznia).raises(ValueError).when_called_with( [], None, {})
    
    def test_usun_ucznia_sukces(self):
        assert_that(self.temp.usun_ucznia(3)).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}])

    def test_usun_ucznia_sukces_2(self):
        assert_that(self.temp.usun_ucznia(1)).does_not_contain({'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []})
    
    def test_usun_ucznia_sukces_3(self):
        assert_that(self.temp.usun_ucznia(2)[1]).does_not_contain_value(2)

    def test_usun_ucznia_nieistniejace_id(self):
        assert_that(self.temp.usun_ucznia).raises(ValueError).when_called_with(54)
    
    def test_usun_ucznia_nieprawidlowy_typ_id(self):
        assert_that(self.temp.usun_ucznia).raises(ValueError).when_called_with({})
    
    def test_usun_ucznia_nieprawidlowy_typ_id_2(self):
        assert_that(self.temp.usun_ucznia).raises(ValueError).when_called_with(45345.5676786786)
    
    def test_edytuj_ucznia_sukces(self):
        assert_that(self.temp.edytuj_ucznia(3, 'Jan', 'Nowak')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Jan', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

    def test_edytuj_ucznia_sukces_2(self):
        assert_that(self.temp.edytuj_ucznia(1, 'Daria', 'Kowalska')).is_not_equal_to(self.temp)

    def test_edytuj_ucznia_nieistniejace_id(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(54,'noweImie', 'noweNazwisko')
    
    def test_edytuj_ucznia_nieprawidlowy_typ_id(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(True,'noweImie', 'noweNazwisko')
    
    def test_edytuj_ucznia_nieprawidlowy_typ_id_2(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(5645465487.456342423,'noweImie', 'noweNazwisko')
    
    def test_edytuj_ucznia_nieprawidlowy_typ_imienia(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(2 , 4353543, 'noweNazwisko')
    
    def test_edytuj_ucznia_nieprawidlowy_typ_nazwiska(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(2 , 'noweImie', None)

    def test_edytuj_ucznia_puste_nowe_imie(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(2,'', 'noweNazwisko')

    def test_edytuj_ucznia_puste_nowe_nazwisko(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(2,'noweImie', '')
    
    def test_edytuj_ucznia_nieprawidlowy_typ_argumentow(self):
        assert_that(self.temp.edytuj_ucznia).raises(ValueError).when_called_with(True , {} , None)
    
    def test_dodaj_przedmiot_sukces(self):
        assert_that(self.temp.dodaj_przedmiot(3, 'j. polski')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_dodaj_przedmiot_sukces_2(self):
        assert_that(self.temp.dodaj_przedmiot(1, 'informatyka')).is_not_equal_to(self.temp)

    def test_dodaj_przedmiot_sukces_3(self):
        assert_that(self.temp.dodaj_przedmiot(3, 'muzyka')).ma_przedmiot( 3, 'muzyka')

    def test_dodaj_przedmiot_nieistniejace_id(self):
        assert_that(self.temp.dodaj_przedmiot).raises(ValueError).when_called_with(45567566, 'j. polski')
    
    def test_dodaj_przedmiot_nieprawidlowy_typ_id(self):
        assert_that(self.temp.dodaj_przedmiot).raises(ValueError).when_called_with(54.556546, 'j. polski')
    
    def test_dodaj_przedmiot_nieprawidlowy_typ_id_2(self):
        assert_that(self.temp.dodaj_przedmiot).raises(ValueError).when_called_with(True, 'j. polski')
    
    def test_dodaj_przedmiot_nieprawidlowy_przedmiot(self):
        assert_that(self.temp.dodaj_przedmiot).raises(ValueError).when_called_with(True, 'sdfsdfsf')
    
    def test_dodaj_przedmiot_nieprawidlowy_przedmiot_2(self):
        assert_that(self.temp.dodaj_przedmiot).raises(ValueError).when_called_with(True, {})
    
    def test_edytuj_przedmiot_sukces(self):
        assert_that(self.temp.edytuj_przedmiot(1, 'matematyka', 'informatyka')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'informatyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_edytuj_przedmiot_sukces_2(self):
        assert_that(self.temp.edytuj_przedmiot(2, 'j. polski', 'plastyka')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'plastyka', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])

    def test_edytuj_przedmiot_nieprawidlowy_przedmiot(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with(2, 'sdfsdfsf', 'biologia')
    
    def test_edytuj_przedmiot_nieprawidlowy_przedmiot_2(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with(2, None, 'matematyka')
    
    def test_edytuj_przedmiot_nieistniejace_id(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with(546455675464, 'matematyka', 'informatyka')
    
    def test_edytuj_przedmiot_nieprawidlowe_id(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with('dfgfdg', 'matematyka', 'informatyka')
    
    def test_edytuj_przedmiot_nieistniejacy_przedmiot(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with( 3, 'matematyka', 'informatyka')
    
    def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with( 1, 'matematyka', 'sdfdsf')
    
    def test_edytuj_przedmiot_nieprawidlowy_nowy_przedmiot_2(self):
        assert_that(self.temp.edytuj_przedmiot).raises(ValueError).when_called_with( 2, 'matematyka', [])
    
    def test_usun_przedmiot_sukces(self):
        assert_that(self.temp.usun_przedmiot(2, 'matematyka')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],)

    def test_usun_przedmiot_sukces_2(self):
        assert_that(self.temp.usun_przedmiot(1, 'matematyka')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_usun_przedmiot_nieistniejace_id(self):
        assert_that(self.temp.usun_przedmiot).raises(ValueError).when_called_with(54, 'matematyka')
    
    def test_usun_przedmiot_nieistniejacy_przedmiot(self):
        assert_that(self.temp.usun_przedmiot).raises(ValueError).when_called_with(3, 'matematyka')
    
    def test_usun_przedmiot_nieprawidlowy_przedmiot(self):
        assert_that(self.temp.usun_przedmiot).raises(ValueError).when_called_with(3, 'dgfdgfdg')
    
    def test_usun_przedmiot_nieprawidlowe_id(self):
        assert_that(self.temp.usun_przedmiot).raises(ValueError).when_called_with({}, 'matematyka')
    
    def test_usun_przedmiot_nieprawidlowe_argumenty(self):
        assert_that(self.temp.usun_przedmiot).raises(ValueError).when_called_with(None, 'dfgfdg')
    
    def test_dodaj_ocene_sukces(self):
        assert_that(self.temp.dodaj_ocene(1, 'matematyka', 1)).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}],)

    def test_dodaj_ocene_sukces_2(self):
        assert_that(self.temp.dodaj_ocene(2, 'matematyka', 5)).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6, 5]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_dodaj_ocene_nieistniejace_id(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(54, 'matematyka', 2)
    
    def test_dodaj_ocene_nieprawidlowe_id(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with([], 'matematyka', 2)
    
    def test_dodaj_ocene_nieprawidlowa_ocena(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(2, 'matematyka', '56464')
    
    def test_dodaj_ocene_nieprawidlowa_ocena_2(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(2, 'matematyka', 5.75)
    
    def test_dodaj_ocene_nieistniejacy_przedmiot(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(1, 'j. polski', 2)
    
    def test_dodaj_ocene_nieprawidlowy_przedmiot(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(1, 'dfgfdgfdg', 2)
    
    def test_dodaj_ocene_nieprawidlowe_argumenty(self):
        assert_that(self.temp.dodaj_ocene).raises(ValueError).when_called_with(44565.456456, 'dfgfdgfdg', {})
    
    def test_edytuj_oceny_sukces(self):
        assert_that(self.temp.edytuj_oceny(1, 'matematyka', [1,1,1,1])).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1, 1, 1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_edytuj_oceny_sukces_2(self):
        assert_that(self.temp.edytuj_oceny(2, 'j. polski', [6, 6, 4])).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': [6, 6, 4]}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_edytuj_oceny_nieprawidlowe_oceny(self):
        assert_that(self.temp.edytuj_oceny).raises(ValueError).when_called_with(1, 'matematyka', [5.75,5.5, 2])

    def test_edytuj_oceny_nieprawidlowe_oceny_2(self):
        assert_that(self.temp.edytuj_oceny).raises(ValueError).when_called_with(1, 'matematyka', [{}, 5, 6])
    
    def test_pokaz_statystyki_ucznia_sukces(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotow(2)).is_equal_to([['matematyka', 5.0], ['j. polski', 0]])
    
    def test_pokaz_statystyki_ucznia_sukces_2(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotow(3)).is_equal_to([])
    
    def test_pokaz_statystyki_ucznia_nieistniejace_id(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotow).raises(ValueError).when_called_with(45456546456)
    
    def test_pokaz_statystyki_ucznia_nieprawidlowe__id(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotow).raises(ValueError).when_called_with(45456546456.45654464)
    
    def test_pokaz_statystyki_ucznia_nieprawidlowe__id_2(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotow).raises(ValueError).when_called_with(None)
    
    def test_pokaz_statystyki_ucznia_przedmiot_sukces(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu(2, 'matematyka')).is_equal_to([['matematyka', 5.0]])
    
    def test_pokaz_statystyki_ucznia_przedmiot_sukces_2(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu(2, 'j. polski')).is_equal_to([['j. polski', 0]])
    
    def test_pokaz_statystyki_ucznia_przedmiot_nieistniejace_id(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with(45456546456, 'matematyka')
    
    def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with(45456546456, 'matematyka')
    
    def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowe_id_2(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with(6.6699089, 'matematyka')
    
    def test_pokaz_statystyki_ucznia_przedmiot_nieprawidlowy_przedmiot(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with(1, 'sdfsdf')
    
    def test_pokaz_statystyki_ucznia_przedmiot_nieistniejacy_przedmiot(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with( 1, 'wychowanie fizyczne')
    
    def test_pokaz_statystyki_ucznia_nieprawidlowe_argumenty(self):
        assert_that(self.temp.pokaz_statystyki_przedmiotu).raises(ValueError).when_called_with({}, None)
    
    def test_dodaj_uwage_sukces(self):
        assert_that(self.temp.dodaj_uwage(3, 'Jest niegrzeczny')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}, {'uwaga': 'Jest niegrzeczny'}]}])

    def test_dodaj_uwage_sukces_2(self):
        assert_that(self.temp.dodaj_uwage(1, 'Przeszkadza na lekcji')).starts_with({'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': [{'uwaga':'Przeszkadza na lekcji'}]})
    
    def test_dodaj_uwage_nieistniejace_id(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with(4565454, 'Uwaga')
    
    def test_dodaj_uwage_nieprawidlowe_id(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with(54.566454654, 'Uwaga')
    
    def test_dodaj_uwage_nieprawidlowe_id_2(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with([], 'Uwaga')
    
    def test_dodaj_uwage_nieprawidlowa_uwaga(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with( 3, 45456)
    
    def test_dodaj_uwage_nieprawidlowa_uwaga_2(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with( 3, {})

    def test_dodaj_uwage_pusta_uwaga(self):
        assert_that(self.temp.dodaj_uwage).raises(ValueError).when_called_with( 3, '')

    def test_edytuj_uwage_sukces(self):
        assert_that(self.temp.edytuj_uwage(3, 'Uwaga', 'nowa uwaga')).ends_with({'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'nowa uwaga'}]})
    
    def test_edytuj_uwage_sukces_2(self):
        assert_that(self.temp.edytuj_uwage(2, 'Źle się zachowuje', 'Źle się zachowuje i przeszkadza na lekcji')).is_equal_to([{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
							  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											  {'przedmiot': 'j. polski', 'oceny': []}],
							   'uwagi': [{'uwaga': 'Źle się zachowuje i przeszkadza na lekcji'}, {'uwaga': 'Jest niegrzeczny'}]},
							  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								  [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    
    def test_edytuj_uwage_nieistniejace_id(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 54, 'uwaga', 'nowa uwaga')
    
    def test_edytuj_uwage_nieprawidlowe_id(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( None, 'uwaga', 'nowa uwaga')
    
    def test_edytuj_uwage_nieprawidlowe_id_2(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 6546546.6, 'uwaga', 'nowa uwaga')
    
    def test_edytuj_uwage_nieistniejaca_uwaga(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with(3, 'sfddsfsff', 'nowa uwaga')
    
    def test_edytuj_uwage_nieprawidlowa_nowa_uwaga(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with(  3, 'uwaga', 4569540)
    
    def test_edytuj_uwage_nieprawidlowa_nowa_uwaga_2(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 3, 'uwaga', ['dfgfdgfd'])

    def test_edytuj_uwage_pusta_uwaga(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 3, '', 'nowa uwaga')

    def test_edytuj_uwage_pusta_nowa_uwaga(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 3, 'uwaga', '')
    
    def test_edytuj_uwage_nieprawidlowa_uwaga(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( 1, {}, 'nowa uwaga')
    
    def test_edytuj_uwage_nieprawidlowe_argumenty(self):
        assert_that(self.temp.edytuj_uwage).raises(ValueError).when_called_with( [], {}, True)

    def test_importuj_dane_sukces(self):
        assert_that(self.temp.importuj_dane('data/data1.csv')).is_equal_to([{'id': 1, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 5, 6]}, {'przedmiot': 'informatyka', 'oceny': [5]}], 'uwagi': []}, {'id': 2, 'imie': 'Maciej', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}, {'uwaga': 'Przeszkadza na zajeciach'}]}, {'id': 3, 'imie': 'Wojciech', 'nazwisko': 'Przykladowy', 'przedmioty': [{'przedmiot':
'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}])

    def test_importuj_dane_sukces_2(self):
        assert_that(self.temp.importuj_dane('data/data1_1.csv')).is_equal_to([{'id': 2, 'imie': 'Franciszka', 'nazwisko': 'Sienkiewicz', 'przedmioty': [{'przedmiot': 'chemia', 'oceny': [1, 5, 6, 2, 3]}, {'przedmiot': 'plastyka', 'oceny': [5, 1, 2]}], 'uwagi': []}, {'id': 46, 'imie': 'Oliwier', 'nazwisko': 'Stanek', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}]}, {'id': 2173, 'imie': 'Maurycy', 'nazwisko': 'Kamiński', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6, 6, 6]}, {'przedmiot': 'geografia', 'oceny': [1, 2, 6]}, {'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}, {'id': 656, 'imie': 'August', 'nazwisko': 'Wrona', 'przedmioty': [], 'uwagi': []}, {'id': 1, 'imie': 'Maciej', 'nazwisko': 'Jeleń', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}],)
    
    def test_importuj_dane_zly_format_pliku(self):
        assert_that(self.temp.importuj_dane).raises(ValueError).when_called_with('sdfsf.jpg')

    def test_importuj_dane_zly_format_pliku_2(self):
        assert_that(self.temp.importuj_dane).raises(ValueError).when_called_with('sdfsf')

    def test_importuj_dane_zly_format_pliku_3(self):
        assert_that(self.temp.importuj_dane).raises(ValueError).when_called_with([])

    def test_importuj_dane_zly_format_pliku_4(self):
        assert_that(self.temp.importuj_dane).raises(ValueError).when_called_with(3)

    def test_eksportuj_dane_sukces(self):
        assert_that(self.temp.eksportuj_dane('data/data2.csv')).is_equal_to(self.temp.lista_uczniow)
    
    def test_eksportuj_dane_zly_format_pliku(self):
        assert_that( self.temp.eksportuj_dane).raises(ValueError).when_called_with('sdfsf')

    def test_eksportuj_dane_zly_format_pliku_2(self):
        assert_that(self.temp.eksportuj_dane).raises(ValueError).when_called_with([])

    def test_eksportuj_dane_zly_format_pliku_3(self):
        assert_that(self.temp.eksportuj_dane).raises(ValueError).when_called_with(456546)

    def test_eksportuj_dane_zly_format_pliku_4(self):
        assert_that(self.temp.eksportuj_dane).raises(ValueError).when_called_with('dfsdf.mp3')

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
