import os
import re

TARGET_FOLDER = os.path.expanduser("C:\\Users\\90507\\Desktop\\target")
SIGNATURES_FILE = "virus_signatures.txt"


def load_virus_signatures(file_path):
    virus_signatures = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                signature = line.strip()
                virus_signatures.append(signature)
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
    return virus_signatures


def scan_files():
    infected_files = []
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                if is_infected(file_path):
                    infected_files.append(file_path)
    return infected_files


def is_infected(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    for signature in SIGNATURES_FILE:
        if re.search(signature, content):
            return True
    return False


def clean_files(infected_files):
    for file_path in infected_files:
        clean_file(file_path)


def clean_file(file_path):
    with open(file_path, "w") as f:
        f.write("")


def run_antivirus():
    print("Antivirus scanning started.")
    virus_signatures = load_virus_signatures(SIGNATURES_FILE)
    infected_files = scan_files()
    if infected_files:
        print(f"Found {len(infected_files)} infected files. Cleaning them now...")
        clean_files(infected_files)
        print("Cleaning completed.")
    else:
        print("No infected files found.")
    print("Antivirus scanning finished.")


if __name__ == "__main__":
    run_antivirus()
