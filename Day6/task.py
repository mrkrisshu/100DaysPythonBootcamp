from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Coding Discipline Agreement", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(33, 37, 41)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, body):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, body)
        self.ln(1)

pdf = PDF()
pdf.add_page()

# Participants and Purpose
pdf.section_title("Participants:")
pdf.section_body("- Participant 1: Bibek Bhandari\n- Participant 2: Krishna Bantola")

pdf.section_title("Purpose:")
pdf.section_body("To establish and maintain daily coding discipline through public accountability via YouTube Live, ensuring active and genuine participation.")

# Rules
pdf.section_title("Rules")
pdf.section_body("1️⃣ Daily Duration:\n"
                 "- Minimum 3 hours of live coding on YouTube per day.\n"
                 "- Can be split into up to 4 sessions (e.g., 2×1.5hr, 4×45min).\n"
                 "- Total must be ≥ 3 hours daily.\n\n"
                 "2️⃣ Stream Layout:\n"
                 "- Main screen: external monitor (coding screen).\n"
                 "- Two overlays must be visible throughout:\n"
                 "  • Webcam feed (participant’s face)\n"
                 "  • Laptop display (as a small window)\n\n"
                 "3️⃣ Webcam Activity:\n"
                 "- Webcam must clearly show participant present and active.\n"
                 "- If inactive or absent for over 10 mins, a penalty applies.\n\n"
                 "4️⃣ Penalty:\n"
                 "- Rs. 100 per violation (e.g., <3 hrs, layout issue, inactive >10 mins).\n"
                 "- Must be paid within 24 hours to the other participant.\n\n"
                 "5️⃣ Verification & Review:\n"
                 "- Daily YouTube live link must be shared with both participants.\n"
                 "- To report a violation:\n"
                 "  • Review at least 10 continuous minutes of the stream.\n"
                 "  • Provide clear timestamp(s) showing the issue.\n"
                 "  • Penalty is valid only if violation is clearly proven.")

# Validity
pdf.section_title("Validity")
pdf.section_body("This agreement is valid for 30 days starting from [Start Date].\nIt can be extended by mutual agreement.")

# Signatures
pdf.section_title("Signatures")
pdf.set_font("Helvetica", "", 11)
pdf.cell(60, 8, "Participant Name", border=1)
pdf.cell(65, 8, "Signature", border=1)
pdf.cell(50, 8, "Date", border=1)
pdf.ln()
pdf.cell(60, 8, "Bibek Bhandari", border=1)
pdf.cell(65, 8, "", border=1)
pdf.cell(50, 8, "", border=1)
pdf.ln()
pdf.cell(60, 8, "Krishna Bantola", border=1)
pdf.cell(65, 8, "", border=1)
pdf.cell(50, 8, "", border=1)

# Save PDF
pdf_path = "/mnt/data/Coding_Discipline_Agreement.pdf"
pdf.output(pdf_path)

pdf_path
