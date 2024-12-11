import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)


    def test_1(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.assertEqual(len(results), 2)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner].name == 'Ник')
        result_dict = {}
        for i in results.keys():
            result_dict[i] = results[i].name
        self.all_results.append(result_dict)


    def test_2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertEqual(len(results), 2)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner].name == 'Ник')
        result_dict = {}
        for i in results.keys():
            result_dict[i] = results[i].name
        self.all_results.append(result_dict)


    def test_3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.assertEqual(len(results), 3)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner].name == 'Ник')
        result_dict = {}
        for i in results.keys():
            result_dict[i] = results[i].name
        self.all_results.append(result_dict)


if __name__ == '__main__':
    unittest.main()
