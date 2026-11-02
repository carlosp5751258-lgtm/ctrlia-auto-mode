import unittest

from check_defaults import problems


class TestProblems(unittest.TestCase):
    def test_with_defaults_no_warning(self):
        self.assertEqual(problems({"autoMode": {"soft_deny": ["$defaults", "x"], "hard_deny": ["$defaults"]}}), [])

    def test_without_defaults_warns(self):
        warnings = problems({"autoMode": {"soft_deny": ["Never run migrations"], "environment": ["$defaults"]}})
        self.assertEqual(len(warnings), 1)
        self.assertIn("soft_deny", warnings[0])

    def test_without_automode(self):
        self.assertEqual(problems({"permissions": {"ask": ["Bash(git push *)"]}}), [])


if __name__ == "__main__":
    unittest.main()
