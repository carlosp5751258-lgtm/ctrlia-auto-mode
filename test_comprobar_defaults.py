import unittest

from comprobar_defaults import problemas


class TestProblemas(unittest.TestCase):
    def test_con_defaults_no_avisa(self):
        self.assertEqual(problemas({"autoMode": {"soft_deny": ["$defaults", "x"], "hard_deny": ["$defaults"]}}), [])

    def test_sin_defaults_avisa(self):
        avisos = problemas({"autoMode": {"soft_deny": ["Never run migrations"], "environment": ["$defaults"]}})
        self.assertEqual(len(avisos), 1)
        self.assertIn("soft_deny", avisos[0])

    def test_sin_automode(self):
        self.assertEqual(problemas({"permissions": {"ask": ["Bash(git push *)"]}}), [])


if __name__ == "__main__":
    unittest.main()
