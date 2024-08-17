import pylint.lint
import sys
import io

# List of scripts for analyzing
scripts = ['virus.py', 'antivirus.py']

# List of arguments for pylint
pylint_args = scripts + ['--output-format=text', '--reports=y']

# catch pylint output
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

# Run pylint with the given
pylint_output = pylint.lint.Run(pylint_args, do_exit=False)

# Restore standard output
sys.stdout = old_stdout
pylint_report = new_stdout.getvalue()

# Save the pylint report
report_file_path = 'pylint_report.txt'
with open(report_file_path, 'w', encoding='utf-8') as report_file:
    report_file.write(pylint_report)

print(f"Pylint report saved to {report_file_path}")
