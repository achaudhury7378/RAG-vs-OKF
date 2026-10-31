"""Extract the interview-notes PDF to plain text (the shared RAG corpus)."""
import re
import sys
from pypdf import PdfReader

pdf_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/abhisheknarayanchaudhury/Downloads/EY Supply Chain Interview Notes.pdf"
pages = [p.extract_text() or "" for p in PdfReader(pdf_path).pages]
text = "\n\n".join(pages)
# drop the repeated running header/footer so it doesn't pollute chunks
text = re.sub(r"EY Supply Chain Interview Notes\s*\nPage \d+ of \d+", "", text)
open("data/docs/ey_supply_chain_notes.txt", "w").write(text.strip() + "\n")
print(f"{len(pages)} pages, {len(text)} chars")
