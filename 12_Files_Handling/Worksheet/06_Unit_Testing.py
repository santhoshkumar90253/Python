'''Unit Testing
 Covers: Basic unit testing
 Description: Write tests using a framework like unittest or pytest to validate the 
functionality of the previously developed scripts.'''


import unittest
from math_utils import process_log_file, extract_severity

class TestLogFunctions(unittest.TestCase):
    
    def setUp(self):
        self.filename = "sample.log"
        with open(self.filename, "w") as f:
            f.write("2025-06-27 10:15:30,123 INFO: Startup complete\n")
            f.write("2025-06-27 10:16:00,456 INFO: Connection established\n")
            f.write("2025-06-27 10:16:00,456 ERROR: Connection established\n")

    def test_process_log_file(self):
        lines = process_log_file(self.filename)
        self.assertIsInstance(lines, list)
        self.assertGreater(len(lines), 0)

    def test_extract_severity_all_info(self):
        lines = process_log_file(self.filename)
        for line in lines:
            severity = extract_severity(line)
            self.assertEqual(severity, "INFO")

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            process_log_file("nonexistent.log")

if __name__ == "__main__":
    unittest.main()