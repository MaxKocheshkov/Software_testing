import unittest
import secretary_program
from unittest.mock import patch


class InitSecretaryTest(unittest.TestCase):

    def test_update_date(self):
        dirs, docs = {}, []
        self.assertFalse(dirs)
        self.assertFalse(docs)
        dirs, docs = secretary_program.update_date()
        self.assertTrue(dirs)
        self.assertTrue(docs)
        self.assertIsInstance(dirs, dict)
        self.assertIsInstance(docs, list)


class SecretaryTest(unittest.TestCase):

    def setUp(self):
        self.dirs, self.docs = secretary_program.update_date()
        with patch('secretary_program.input', return_value='q'):
            with patch('secretary_program.update_date') as mock_ud:
                mock_ud.return_value = self.docs, self.dirs
                secretary_program.main()

    def test_search_by_number(self):
        user_input = ['2207 876234']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.search_by_number(self.docs)

    def test_all_docs(self):
        secretary_program.all_docs(self.docs)

    def test_exterminate(self):
        user_input = ['10006']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.exterminate(self.docs, self.dirs)
            self.assertNotIn(user_input, self.docs)
            self.assertNotIn(user_input, self.dirs['2'])

    def test_extension(self):
        user_input = ['pasp', '123', 'TestName', '4']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.extension(self.docs, self.dirs)

    def test_act(self):
        user_input = ['10006']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.act(self.dirs)

    def test_transfer(self):
        user_input = ['10006', '3']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.transfer(self.dirs)

    def test_supplement(self):
        user_input = ['4']
        with patch('secretary_program.input', side_effect=user_input):
            secretary_program.supplement(self.dirs)
