from similarité_cosinus import *
import unittest

class TestProgrammeProxy(unittest.TestCase):
    def test_Similarite_cosinus(self):
        # Comparaison avec une précision jusqu'à trois décimales
        self.assertAlmostEqual(simCos("Je suis intéressé par l'apprentissage automatique.", 
                                      "Je suis intéressé par l'apprentissage automatique."), 
                                      1.0000000000, places=10)
        self.assertAlmostEqual(simCos("Je suis grand", 
                                      "La voiture rapide"), 
                                      0.0000000000, places=10)       

if __name__ == "__main__":
    unittest.main()

