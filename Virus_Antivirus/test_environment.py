import unittest
import os
import time
from virus import change_signature, infect_files, trigger_virus, VIRUS_SIGNATURE


class TestVirusAndAntivirus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_folder = os.path.expanduser("C:\\Users\\90507\\Desktop\\target")
        os.makedirs(cls.test_folder, exist_ok=True)

    def setUp(self):
        self.test_file = os.path.join(self.test_folder, "test1.txt")
        self.infected_file = os.path.join(self.test_folder, "infected.txt")
        create_test_file(self.test_file)
        create_test_file(self.infected_file, VIRUS_SIGNATURE)

    def tearDown(self):
        for file_path in [self.test_file, self.infected_file]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_signature_change(self):
        trigger_virus()
        infect_files()

        original_signature = VIRUS_SIGNATURE
        print(f"Original signature without changed: {original_signature}")

        time.sleep(10)

        new_signature = change_signature()
        print(f"New signature: {new_signature}")
        infect_files()
        self.assertNotEqual(original_signature, new_signature, "Signature didn't change!")
        self.assertTrue(check_infection(self.test_file, new_signature),
                        "Test file should be infected with new signature!")

    def test_antivirus_cleaning(self):
        run_antivirus(self.test_folder)
        self.assertTrue(check_clean(self.test_file), "Antivirus did not clean test1.txt!")
        self.assertTrue(check_clean(self.infected_file), "Antivirus did not clean infected.txt!")

    def test_infected_file(self):
        self.assertTrue(check_infection(self.infected_file, VIRUS_SIGNATURE),
                        "Infected file should contain the virus signature!")


def create_test_file(file_path, content=""):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def check_infection(file_path, expected_signature):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"Content of the file: {content}")
    return expected_signature in content


def check_clean(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content == ""


def run_antivirus(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            clean_content = content.replace(VIRUS_SIGNATURE, "")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(clean_content)


if __name__ == "__main__":
    unittest.main()
