import subprocess
import sys
import unittest

from banking import apply_operation


class OperationTests(unittest.TestCase):
    def test_withdraw_checking(self):
        self.assertEqual(apply_operation("w", "c", 30, 100, 50), (70, 50))

    def test_withdraw_full_balance_allowed(self):
        self.assertEqual(apply_operation("withdraw", "s", 50, 100, 50), (100, 0))

    def test_overdraw_returns_none(self):
        self.assertIsNone(apply_operation("w", "c", 101, 100, 50))

    def test_deposit_savings(self):
        self.assertEqual(apply_operation("d", "s", 25, 100, 50), (100, 75))

    def test_transfer_checking_to_savings(self):
        self.assertEqual(apply_operation("t", "c", 40, 100, 50), (60, 90))

    def test_transfer_savings_to_checking(self):
        self.assertEqual(apply_operation("transfer", "s", 50, 100, 50), (150, 0))


class ScriptTests(unittest.TestCase):
    def run_script(self, text):
        return subprocess.run(
            [sys.executable, "banking.py"], input=text, capture_output=True, text=True
        )

    def test_withdraw_run(self):
        out = self.run_script("100\n50\nw\nc\n30\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("70.00", out.stdout)

    def test_float_artifact_is_formatted_away(self):
        out = self.run_script("0.1\n0\nd\nc\n0.2\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("0.30", out.stdout)
        self.assertNotIn("0.30000000000000004", out.stdout)

    def test_eof_has_no_traceback(self):
        out = self.run_script("")
        self.assertEqual(out.returncode, 1)
        self.assertNotIn("Traceback", out.stderr)

    def test_negative_starting_balance_rejected(self):
        out = self.run_script("-5\n50\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("Balances must not be negative", out.stdout)

    def test_bad_action_exits_1(self):
        out = self.run_script("100\n50\nx\nc\n10\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("Please choose w, d, or t", out.stdout)

    def test_insufficient_funds_exits_1(self):
        out = self.run_script("100\n50\nw\nc\n999\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("You do not have that amount of money", out.stdout)


if __name__ == "__main__":
    unittest.main()
