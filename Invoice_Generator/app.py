import pandas as pd
from fpdf import FPDF
from datetime import datetime

# ==========================================
# STEP 4A: READ & CALCULATE COMMERCE DATA
# ==========================================

# 1. Load the Excel file using pandas
df = pd.read_excel('sales_data.xlsx')

# 2. Get the customer's name from the first row
customer_name = df['Customer Name'].iloc[0]

# 3. Calculate total price for each row (Quantity x Price)
df['Total Price'] = df['Quantity'] * df['Price Per Unit']

# 4. Calculate the Grand Total of the entire invoice
grand_total = df['Total Price'].sum()

# 5. Get today's date automatically
today_date = datetime.today().strftime('%Y-%m-%d')


# ==========================================
# STEP 4B: GENERATE THE PDF INVOICE
# ==========================================

# Create a PDF object (P = Portrait mode, mm = millimeters, A4 size)
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Set up the font (Arial, Bold, Size 20)
pdf.set_font("Arial", style='B', size=20)

# --- HEADER SECTION ---
# Create a title box (Width=0 means full page width, Height=10mm)
pdf.cell(0, 10, txt="INVOICE / BILL RECEIPT", ln=True, align='C')
pdf.ln(5) # Add a 5mm blank line space

# --- CUSTOMER & DATE DETAILS ---
pdf.set_font("Arial", size=11)
pdf.cell(0, 6, txt=f"Customer Name: {customer_name}", ln=True)
pdf.cell(0, 6, txt=f"Date: {today_date}", ln=True)
pdf.cell(0, 6, txt="Invoice No: #INV-2026-001", ln=True)
pdf.ln(10) # Blank space before the table

# --- TABLE HEADERS ---
pdf.set_font("Arial", style='B', size=11)
# Create columns: Item Name (80mm), Qty (30mm), Price/Unit (40mm), Total (40mm)
pdf.cell(80, 8, txt="Item Name", border=1)
pdf.cell(30, 8, txt="Quantity", border=1, align='C')
pdf.cell(40, 8, txt="Price/Unit (Rs)", border=1, align='R')
pdf.cell(40, 8, txt="Total (Rs)", border=1, align='R', ln=True)

# --- TABLE ROWS (LOOP THROUGH EXCEL DATA) ---
pdf.set_font("Arial", size=11)
for index, row in df.iterrows():
    pdf.cell(80, 8, txt=str(row['Item Name']), border=1)
    pdf.cell(30, 8, txt=str(row['Quantity']), border=1, align='C')
    pdf.cell(40, 8, txt=f"{row['Price Per Unit']:.2f}", border=1, align='R')
    pdf.cell(40, 8, txt=f"{row['Total Price']:.2f}", border=1, align='R', ln=True)

# --- GRAND TOTAL SECTION ---
pdf.ln(5)
pdf.set_font("Arial", style='B', size=12)
# Create a blank spacer cell to push the total to the right side
pdf.cell(110, 8, txt="") 
pdf.cell(40, 8, txt="Grand Total:", border=1, align='R')
pdf.cell(40, 8, txt=f"Rs. {grand_total:.2f}", border=1, align='R', ln=True)

# --- FOOTER ---
pdf.ln(20)
pdf.set_font("Arial", style='I', size=10)
pdf.cell(0, 10, txt="Thank you for your business! Generated automatically via Python.", align='C')

# Save the PDF file to your folder
pdf.output("Final_Invoice.pdf")

print("⚡ Success! 'Final_Invoice.pdf' has been generated in your folder.")