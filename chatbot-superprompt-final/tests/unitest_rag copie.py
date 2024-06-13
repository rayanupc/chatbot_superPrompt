import unittest
from unittest.mock import patch, MagicMock
from RAG_recherche_sur_internet_version_finale import *
import RAG_recherche_sur_internet_version_finale

class TestLanguageModels(unittest.TestCase):

    def test_stocker_reponse(self):
        RAG_recherche_sur_internet_version_finale.stocker_reponse("Quelle heure est-il?", "Il est midi")
        self.assertIn("quelle heure est-il?", RAG_recherche_sur_internet_version_finale.database)
        self.assertEqual(RAG_recherche_sur_internet_version_finale.database["quelle heure est-il?"], "il est midi")

    @patch('openai.chat.completions.create')
    def test_most_relevant(self, mock_create):
        mock_create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="La réponse la plus pertinente"))])
        responses = ["Réponse 1", "Réponse 2", "Réponse 3"]
        result = RAG_recherche_sur_internet_version_finale.most_relevant("Quelle est la meilleure réponse?", responses)
        self.assertEqual(result, "La réponse la plus pertinente")

    # tests pour la fonction question_existante
    def setUp(self): 
        RAG_recherche_sur_internet_version_finale.database.clear()
        RAG_recherche_sur_internet_version_finale.stocker_reponse("Où est Paris?", "Paris est en France")

    def test_question_existante_true(self):
        self.assertIsNotNone(RAG_recherche_sur_internet_version_finale.question_existante("où est paris?", 0.8))

    def test_question_existante_false(self):
        self.assertIsNone(RAG_recherche_sur_internet_version_finale.question_existante("Quelle est la capitale de l'Allemagne?", 0.8))

if __name__ == "__main__":
    unittest.main()
