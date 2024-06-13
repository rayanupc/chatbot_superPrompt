import unittest
from unittest.mock import patch
from proxyv2 import *
import proxyv2 

class TestLanguageModels(unittest.TestCase):
    """"Tester ces fonctions implique de s'assurer qu'elles envoient 
    les bons messages aux LLM et renvoient correctement la réponse"""
    @patch('proxyv2.generic_model_request')
    def test_get_response_llama(self, mock_generic):
        # Set up
        mock_generic.return_value = ["This is a test response."]
        
        query = "Test query"
        response = get_response_llama(query)
        
        # Verify response
        self.assertEqual(response, "This is a test response.")
        
        # Verify call arguments
        mock_generic.assert_called_with(
            model="together_ai/togethercomputer/llama-2-70b-chat",
            messages=[
                {"role": "system", "content": "réponds à la question comme un expert dans le domaine."},
                {"role": "user", "content": query},
            ],
            api_base=None
        )
        
    @patch('proxyv2.generic_model_request')
    def test_get_response_chatgpt(self, mock_generic):
        # Setup 
        mock_generic.return_value = ["This is a ChatGPT test response."]
        
        query = "Test query for ChatGPT"
        response = get_response_chatgpt(query)
        
        # Verify response
        self.assertEqual(response, "This is a ChatGPT test response.")
        
        # Verify call arguments
        mock_generic.assert_called_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "réponds à la question comme un expert dans le domaine."},
                {"role": "user", "content": query},
            ],
            api_base=None
        )

    @patch('proxyv2.generic_model_request')
    def test_get_response_coral(self, mock_generic):
        # Setup 
        mock_generic.return_value = ["This is a Coral test response."]
        
        query = "Test query for Coral"
        response = get_response_coral(query)
        
        # Verify response
        self.assertEqual(response, "This is a Coral test response.")
        
        # Verify call arguments
        mock_generic.assert_called_with(
            model="cohere/command-nightly",
            messages=[
                {"role": "system", "content": "Réponds uniquement à la requete comme un expert dans le domaine"},
                {"role": "user", "content": query},
            ],
            api_base=None
        )

    @patch('proxyv2.generic_model_request')
    def test_get_response_mistral(self, mock_generic):
        # Setup 
        mock_generic.return_value = ["This is a Mistral test response."]
        
        query = "Test query for Mistral"
        response = get_response_mistral(query)
        
        # Verify response
        self.assertEqual(response, "This is a Mistral test response.")
        
        # Verify call arguments
        mock_generic.assert_called_with(
            model="huggingface/mistralai/Mistral-7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": "réponds à la question comme un expert dans le domaine."},
                {"role": "user", "content": query},
            ],
            api_base="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
        )

    @patch('proxyv2.evaluate_qa_pair')  
    def test_best_reponse_local_llm(self, mock_evaluate):
        # Setup
        request = "Describe quantum computing."
        responses = {
            "IBM": "Quantum computing is a new type of computing.",
            "Google": "Quantum computers use quantum bits or qubits.",
            "Microsoft": "Quantum computing could revolutionize computing by using the principles of quantum mechanics."
        }

        def side_effect(question, answer):
            scores = {
                responses["IBM"]: 75,
                responses["Google"]: 85,
                responses["Microsoft"]: 95
            }
            return scores[answer]

        mock_evaluate.side_effect = side_effect

        # Test
        model, best_response = proxyv2.best_reponse_local_llm(request, responses)

        # Verify
        self.assertEqual(best_response, responses["Microsoft"])
        self.assertEqual(model, "Microsoft")


    #tests de la focntion preprocess_test
    def test_preprocess_text_general(self):
        text = "Hello, World!"
        expected = "hello world"
        self.assertEqual(preprocess_text(text), expected)

    def test_preprocess_text_empty(self):
        text = ""
        expected = ""
        self.assertEqual(preprocess_text(text), expected)

    def test_preprocess_text_special_chars(self):
        text = "It's a test: Does it work?"
        expected = "its a test does it work"
        self.assertEqual(preprocess_text(text), expected)

    #tests de la fonction get_vector
    def test_get_vector_simple(self):
        text = "hello hello world"
        expected = Counter({'hello': 2, 'world': 1})
        self.assertEqual(get_vector(text), expected)

    def test_get_vector_empty(self):
        text = ""
        expected = Counter()
        self.assertEqual(get_vector(text), expected)

    #tests de la fonction FindBestIndex
    def test_exact_match(self):
        best_response = "Hello world"
        responses = ["Hello world", "Hello", "World", "Hello there"]
        expected_index = 0
        self.assertEqual(FindBestIndex(best_response, responses), expected_index)

    def test_close_match(self):
        best_response = "Hello world"
        responses = ["Help", "Hello", "World", "Hello there world"]
        expected_index = 3  
        self.assertEqual(FindBestIndex(best_response, responses), expected_index)

    def test_no_close_match(self):
        best_response = "Hello world"
        responses = ["Goodbye world", "See you later", "Farewell", "Good night"]
        self.assertTrue(FindBestIndex(best_response, responses) in range(len(responses)))

    def test_with_empty_responses(self):
        best_response = "Hello world"
        responses = []
        with self.assertRaises(ValueError):  
            FindBestIndex(best_response, responses)

if __name__ == "__main__":
    unittest.main()