from theme_analyzer2bis import *
import unittest

class TestProgrammeProxy(unittest.TestCase):
    def test_theme_analyzer2bis(self):
        self.assertEqual(analyze_query("How to integrate a second-degree polynomial?"), "mathematic")
        self.assertEqual(analyze_query("How does mitosis starts?"), "biologie")
        self.assertEqual(analyze_query("What was the writing style of Shakespeare?"), "poetry")
        self.assertEqual(analyze_query("Explain the Java Script programming laguage"), "computer science")
        self.assertEqual(analyze_query("Has the president of United States full control of his country?"), "politic")
        self.assertEqual(analyze_query("What was the date of the second World War?"), "history")


if __name__ == "__main__":
    unittest.main()
