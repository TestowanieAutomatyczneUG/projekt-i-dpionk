import unittest
from parameterized import parameterized, parameterized_class
from src.sample.dziennik import *

class Dziennik_test_parameterized_1(unittest.TestCase):

    def setUp(self):
        dziennik = Dziennik([])
        dziennik.dodaj_ucznia(1, 'Daria', 'Pionk')
        dziennik.dodaj_ucznia(2, 'Jan', 'Kowalski')
        dziennik.dodaj_ucznia(3, 'Kamil', 'Nowak')
        dziennik.dodaj_przedmiot(2, 'matematyka')
        dziennik.dodaj_przedmiot(2, 'j. polski')
        dziennik.dodaj_przedmiot(1, 'matematyka')
        dziennik.dodaj_ocene(2, 'matematyka', 6)
        dziennik.dodaj_ocene(2, 'matematyka', 3)
        dziennik.dodaj_ocene(2, 'matematyka', 6)
        dziennik.dodaj_uwage(2, 'Źle się zachowuje')
        dziennik.dodaj_uwage(2, 'Jest niegrzeczny')
        dziennik.dodaj_ocene(1, 'matematyka', 1)
        dziennik.dodaj_uwage(3, 'Uwaga')
        self.temp = dziennik

    def tearDown(self):
        self.temp = None

    @parameterized.expand([
        (4, 'Imie', 'Nazwisko', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]},
                    {'id': 4, 'imie': 'Imie', 'nazwisko': 'Nazwisko', 'przedmioty': [], 'uwagi': []}]
        ),
        (67, 'Kazimierz', 'Maj', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}, {'id': 67, 'imie': 'Kazimierz', 'nazwisko': 'Maj', 'przedmioty': [], 'uwagi': []}])

    ])
    def test_parameterized_dodaj_ucznia_poprawne(self, id, imie, nazwisko, output):
        self.assertEqual(self.temp.dodaj_ucznia(id, imie, nazwisko), output)

    @parameterized.expand([
        (1, 'Imie', 'Nazwisko'),
        (7, '', 'Nazwisko'),
        (6, 'Imie', ''),
        ([], 'Imie', 'Nazwisko'),
        (3.4, 'Imie', 'Nazwisko'),
        (4, 456, 'Nazwisko'),
        (4, 'Imie', {}),
        ([], None, {})

    ])
    def test_parameterized_dodaj_ucznia_error(self, id, imie, nazwisko):
        self.assertRaises(ValueError, self.temp.dodaj_ucznia, id, imie, nazwisko)

    @parameterized.expand([
        (3, [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}])
        ,
        (1, [{'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])])

    def test_parameterized_usun_ucznia_poprawne(self, id, output):
        self.assertEqual(self.temp.usun_ucznia(id), output)

    @parameterized.expand([
        (54,),
        ({},),
        (45345.5676786786,)

    ])

    def test_parameterized_usun_ucznia_error(self, id):
        self.assertRaises(ValueError, self.temp.usun_ucznia, id)

    @parameterized.expand([
        ((3, 'Jan', 'Nowak', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Jan', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ),
        (2, 'Maksymilian', 'Malinowski', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Maksymilian', 'nazwisko': 'Malinowski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    ])

    def test_parameterized_edytuj_ucznia_poprawne(self, id, noweImie, noweNazwisko, output):
        self.assertEqual(self.temp.edytuj_ucznia(id, noweImie, noweNazwisko), output)

    @parameterized.expand([
        (2, '', 'noweNazwisko'),
        (2, 'noweImie', ''),
        (54, 'noweImie', 'noweNazwisko'),
        (True, 'noweImie', 'noweNazwisko'),
        (5645465487.456342423, 'noweImie', 'noweNazwisko'),
        (2, 4353543, 'noweNazwisko'),
        (2, 'noweImie', None),
        (True, {}, None)
        ])

    def test_parameterized_edytuj_ucznia_error(self, id, noweImie, noweNazwisko):
        self.assertRaises(ValueError, self.temp.edytuj_ucznia, id, noweImie, noweNazwisko)

    @parameterized.expand([
        ((3, 'j. polski', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak',
                    'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ),
        (1, 'muzyka', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}, {'przedmiot': 'muzyka', 'oceny': []}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    ])

    def test_dodaj_przedmiot_poprawne(self, id, przedmiot, output):
        self.assertEqual(self.temp.dodaj_przedmiot(id, przedmiot), output)

    @parameterized.expand([
        (54, 'j. polski'),
        (54.556546, 'j. polski'),
        (True, 'j. polski'),
        (True, 'sdfsdfsf'),
        (True, {}),

        ])

    def test_dodaj_przedmiot_error(self, id, przedmiot):
        self.assertRaises(ValueError, self.temp.dodaj_przedmiot, id, przedmiot)

    @parameterized.expand([
        (1, 'matematyka', 'informatyka', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'informatyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}]
        ),
        (2, 'j. polski', 'plastyka', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'plastyka', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    ])

    def test_edytuj_przedmiot_poprawne(self, id, przedmiot, nowyPrzedmiot, output):
        self.assertEqual(self.temp.edytuj_przedmiot(id,przedmiot,nowyPrzedmiot), output)

    @parameterized.expand([
        (2, 'sdfsdfsf', 'biologia'),
        (3, None, 'matematyka'),
        (54, 'matematyka', 'informatyka'),
        ('dfgfdg', 'matematyka', 'informatyka'),
        (3, 'matematyka', 'informatyka'),
        (1, 'matematyka', 'sdfdsf'),
        (2, 'matematyka', [])
        ])

    def test_edytuj_przedmiot_error(self, id, przedmiot, nowyPrzedmiot):
        self.assertRaises(ValueError, self.temp.edytuj_przedmiot, id, przedmiot, nowyPrzedmiot)

    @parameterized.expand([
        (2, 'matematyka', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}]
        ),
        (1, 'matematyka', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
    ])

    def test_usun_przedmiot_poprawne(self, id, przedmiot, output):
        self.assertEqual(self.temp.usun_przedmiot(id, przedmiot), output)

    @parameterized.expand([
        (54, 'matematyka'),
        (3, 'matematyka'),
        (3, 'dgfdgfdg'),
        ({}, 'matematyka'),
        (None, 'dfgfdg')
        ])

    def test_usun_przedmiot_error(self, id, przedmiot):
        self.assertRaises(ValueError, self.temp.usun_przedmiot, id, przedmiot)

    @parameterized.expand([
        (1, 'matematyka', 1, [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}]
        ),
        (2, 'matematyka', 5, [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6, 5]}, {'przedmiot': 'j. polski', 'oceny': []}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ])

    def test_dodaj_ocene_poprawne(self, id, przedmiot,ocena, output):
        self.assertEqual(self.temp.dodaj_ocene(id, przedmiot, ocena), output)

    @parameterized.expand([
        (54, 'matematyka', 2),
        ([], 'matematyka', 2),
        (2, 'matematyka', '56464'),
        (2, 'matematyka', 5.75),
        (1, 'j. polski', 2),
        (1, 'dfgfdgfdg', 2),
        (44565.456456, 'dfgfdgfdg', {})
    ])

    def test_dodaj_ocene_error(self, id, przedmiot, ocena):
        self.assertRaises(ValueError, self.temp.dodaj_ocene, id, przedmiot, ocena)

    @parameterized.expand([
        (1, 'matematyka', [1, 1, 1, 1], [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 1, 1, 1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}]
        ),
        (2, 'j. polski', [6, 6, 4],[{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []}, {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]}, {'przedmiot': 'j. polski', 'oceny': [6, 6, 4]}], 'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]}, {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ])

    def test_edytuj_oceny_poprawne(self, id, przedmiot, oceny, output):
        self.assertEqual(self.temp.edytuj_oceny(id, przedmiot, oceny), output)

    @parameterized.expand([
        (1, 'matematyka', [5.75, 5.5, 2]),
        (1, 'matematyka', [{}, 5, 6]),
        (54, 'matematyka', [2]),
        (1, 'dfgfdgdfg', [2])
        ])

    def test_edytuj_oceny_error(self, id, przedmiot, oceny):
        self.assertRaises(ValueError, self.temp.edytuj_oceny, id, przedmiot, oceny)

    @parameterized.expand([
        (2, [['matematyka', 5.0], ['j. polski', 0]]),
        (3, [])
        ])

    def test_pokaz_statystyki_ucznia_poprawne(self, id, output):
        self.assertEqual(self.temp.pokaz_statystyki_przedmiotow(id), output)

    @parameterized.expand([
        (54,),
        (54.456456546,),
        (None,),
        ])

    def test_pokaz_statystyki_ucznia_error(self, id):
        self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotow, id)

    @parameterized.expand([
        (2, 'matematyka', [['matematyka', 5.0]]),
        (2, 'j. polski', [['j. polski', 0]])
    ])

    def test_pokaz_statystyki_przedmiot_poprawne(self, id, przedmiot, output):
        self.assertEqual(self.temp.pokaz_statystyki_przedmiotu(id, przedmiot), output)

    @parameterized.expand([
        (54, 'matematyka'),
        ({}, 'matematyka'),
        (6.6699089, 'matematyka'),
        (1, 'sdfsdf'),
        (1, 'wychowanie fizyczne'),
        ({}, None)
        ])

    def test_pokaz_statystyki_przedmiot_error(self, id, przedmiot):
        self.assertRaises(ValueError, self.temp.pokaz_statystyki_przedmiotu, id , przedmiot)

    @parameterized.expand([
        (3, 'Jest niegrzeczny',[{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
                        [], 'uwagi': [{'uwaga': 'Uwaga'}, {'uwaga': 'Jest niegrzeczny'}]}] )
        , (1, 'nieprzygotowanie', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]},
							  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											  {'przedmiot': 'j. polski', 'oceny': []}],
							   'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
							  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								  [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ])

    def test_dodaj_uwage_poprawne(self, id, uwaga, output):
        self.assertEqual(self.temp.dodaj_uwage(id, uwaga), output)

    @parameterized.expand([
        (54, 'Uwaga'),
        (2, ''),
        (54.566454654, 'Uwaga'),
        ([], 'Uwaga'),
        (3, 45456),
        (3, {})
        ])

    def test_dodaj_uwage_error(self, id, uwaga):
        self.assertRaises(ValueError, self.temp.dodaj_uwage, id, uwaga)

    @parameterized.expand([
        (3, 'Uwaga', 'nowa uwaga',[{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
                    {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
                    'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
                                    {'przedmiot': 'j. polski', 'oceny': []}],
                    'uwagi': [{'uwaga': 'Źle się zachowuje'}, {'uwaga': 'Jest niegrzeczny'}]},
                    {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
                        [], 'uwagi': [{'uwaga': 'nowa uwaga'}]}] )
        ,(2, 'Źle się zachowuje', 'Źle się zachowuje i przeszkadza na lekcji', [{'id': 1, 'imie': 'Daria', 'nazwisko': 'Pionk',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1]}], 'uwagi': []},
							  {'id': 2, 'imie': 'Jan', 'nazwisko': 'Kowalski',
							   'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [6, 3, 6]},
											  {'przedmiot': 'j. polski', 'oceny': []}],
							   'uwagi': [{'uwaga': 'Źle się zachowuje i przeszkadza na lekcji'}, {'uwaga': 'Jest niegrzeczny'}]},
							  {'id': 3, 'imie': 'Kamil', 'nazwisko': 'Nowak', 'przedmioty':
								  [], 'uwagi': [{'uwaga': 'Uwaga'}]}])
        ])

    def test_edytuj_uwage_poprawne(self, id, uwaga, nowa_uwaga, output):
        self.assertEqual(self.temp.edytuj_uwage(id, uwaga, nowa_uwaga), output)

    @parameterized.expand([
        (5456545, 'uwaga', 'nowa uwaga'),
        (None, 'uwaga', 'nowa uwaga'),
        (6546546.6, 'uwaga', 'nowa uwaga'),
        (3, 'sfddsfsff', 'nowa uwaga'),
        (3, 'uwaga', 4569540),
        (3, 'uwaga', ['dfgfdgfd']),
        (3, '', 'nowa uwaga'),
        (3, 'uwaga', ''),
        (1, {}, 'nowa uwaga'),
        ([], {}, True)
        ])

    def test_edytuj_uwage_error(self, id, uwaga, nowa_uwaga):
        self.assertRaises(ValueError, self.temp.edytuj_uwage, id, uwaga, nowa_uwaga)

    @parameterized.expand([
        ('data/data1.csv', [{'id': 1, 'imie': 'Jan', 'nazwisko': 'Kowalski', 'przedmioty': [{'przedmiot': 'matematyka', 'oceny': [1, 5, 6]}, {'przedmiot': 'informatyka', 'oceny': [5]}], 'uwagi': []}, {'id': 2, 'imie': 'Maciej', 'nazwisko': 'Nowak', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}, {'uwaga': 'Przeszkadza na zajeciach'}]}, {'id': 3, 'imie': 'Wojciech', 'nazwisko': 'Przykladowy', 'przedmioty': [{'przedmiot':
'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}]),
        ('data/data1_1.csv', [{'id': 2, 'imie': 'Franciszka', 'nazwisko': 'Sienkiewicz', 'przedmioty': [{'przedmiot': 'chemia', 'oceny': [1, 5, 6, 2, 3]}, {'przedmiot': 'plastyka', 'oceny': [5, 1, 2]}], 'uwagi': []}, {'id': 46, 'imie': 'Oliwier', 'nazwisko': 'Stanek', 'przedmioty': [], 'uwagi': [{'uwaga': 'Jest niegrzeczny'}]}, {'id': 2173, 'imie': 'Maurycy', 'nazwisko': 'Kamiński', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6, 6, 6]}, {'przedmiot': 'geografia', 'oceny': [1, 2, 6]}, {'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}, {'id': 656, 'imie': 'August', 'nazwisko': 'Wrona', 'przedmioty': [], 'uwagi': []}, {'id': 1, 'imie': 'Maciej', 'nazwisko': 'Jeleń', 'przedmioty': [{'przedmiot': 'wychowanie fizyczne', 'oceny': [6, 6]}], 'uwagi': [{'uwaga': 'nieprzygotowanie'}]}])])

    def test_importuj_dane_sukces(self, plik, output):
        self.assertEqual(self.temp.importuj_dane(plik), output)

    @parameterized.expand([
        ('sdsfdsf',),
        ('sdfsf.jpg',),
        ([],),
        ( 3,),

    ])

    def test_importuj_dane_error(self,plik):
        self.assertRaises(ValueError, self.temp.importuj_dane, plik)

    @parameterized.expand([
        ('data/data2.csv', )
    ])
    
    def test_eksportuj_dane_sukces(self,plik):
        self.assertEqual(self.temp.lista_uczniow,  self.temp.eksportuj_dane(plik))
    
    @parameterized.expand([
        ('csvplik',),
        ('sdfsf.mp3',),
        ({},),
        ( 4545.5,),

    ])

    def test_eksportuj_dane_error(self,plik):
        self.assertRaises(ValueError, self.temp.eksportuj_dane, plik)


if __name__ == '__main__':
    unittest.main()