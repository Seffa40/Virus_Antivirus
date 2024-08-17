# Allsafe

Allsafe is a software project designed to handle both virus creation and antivirus detection. This README provides an overview of the project structure and its main components.

![Allsafe](https://png.pngtree.com/png-vector/20191121/ourmid/pngtree-shield-with-a-check-mark-safe-and-protect-logo-on-white-png-image_1870454.jpg)


## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)

## About

Allsafe is developed as an educational tool to demonstrate the workings of viruses and antivirus software. The project includes scripts for creating viruses and detecting them.

## Features

- **Virus Creation**: Demonstrates basic concepts of virus construction.
- **Antivirus Detection**: Scans and detects known viruses using signatures.
- **Testing**: Includes dynamic and static testing environments.

## Installation

To install the project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/berkinozturk/Allsafe.git
cd Allsafe
```

## Usage
Run the antivirus script to scan for viruses:

```bash
python antivirus.py
```

To test virus creation, refer to the virus.py script. Caution: Use in a controlled environment only.

## Files

- **antivirus.py**: The main antivirus script.
- **virus.py**: Script for creating a sample virus.
- **virus_signatures.txt**: Contains known virus signatures for detection.
- **test_environment.py**: Sets up the environment for testing.
- **static_test.py and dynamic_test.py**: Scripts for different testing methods.

