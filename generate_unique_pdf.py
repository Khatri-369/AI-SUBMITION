# generate_unique_pdf.py
# Proxy to generate_complete_submission.py to generate the complete updated PDF
import subprocess
import sys

if __name__ == "__main__":
    result = subprocess.run([sys.executable, "generate_complete_submission.py"])
    sys.exit(result.returncode)
