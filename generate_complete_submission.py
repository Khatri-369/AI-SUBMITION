# generate_complete_submission.py
import subprocess
import os

html_path = os.path.abspath("complete_lab_submission.html")
pdf_path = os.path.abspath("AI_PRACTICLE_SUBMITTION_KHATRI_OM_KUMAR_UPDATED.PDF")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if os.path.exists(edge_path):
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Successfully generated COMPLETE PDF: {pdf_path}")
    else:
        print("Edge error:", res.stderr)
else:
    print("Edge not found")
