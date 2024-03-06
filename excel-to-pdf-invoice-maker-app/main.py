import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("datas/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_no, invoice_date = filename.split("-")

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=12)
    pdf.cell(w=0,h=8,txt=f"Invoice ID. {invoice_no}",align="L",ln=1)
    pdf.cell(w=0,h=8,txt=f"Date {invoice_date}",align="L",ln=1)

    pdf.ln(5)
    
    pdf.cell(w=35,h=8,txt="Product ID",align="L",border=1,ln=0)
    pdf.cell(w=50,h=8,txt="Product Name",align="L",border=1,ln=0)
    pdf.cell(w=35,h=8,txt="Amount",align="L",border=1,ln=0)
    pdf.cell(w=35,h=8,txt="Price per Unit",align="L",border=1,ln=0)
    pdf.cell(w=35,h=8,txt="Total Price",align="L",border=1,ln=1)

    pdf.set_font(family="Times",size=10)
    for index,row in df.iterrows():
        pdf.cell(w=35,h=8,txt=str(row["product_id"]),align="L",border=1,ln=0)
        pdf.cell(w=50,h=8,txt=str(row["product_name"]),align="L",border=1,ln=0)
        pdf.cell(w=35,h=8,txt=str(row["amount_purchased"]),align="L",border=1,ln=0)
        pdf.cell(w=35,h=8,txt=str(row["price_per_unit"]),align="L",border=1,ln=0)
        pdf.cell(w=35,h=8,txt=str(row["total_price"]),align="L",border=1,ln=1)
    
    pdf.set_font(family="Times",style='B')
    pdf.cell(w=35,h=8,txt="",align="L",border=1,ln=0)
    pdf.cell(w=50,h=8,txt="",align="L",border=1,ln=0)
    pdf.cell(w=35,h=8,txt="",align="L",border=1,ln=0)
    pdf.cell(w=35,h=8,txt="Total",align="R",border=1,ln=0)
    pdf.cell(w=35,h=8,txt=str(df["total_price"].sum()),align="L",border=1,ln=1)

    pdf.ln(10)

    pdf.set_font(family="Times",style="B",size=14)
    pdf.cell(w=0,h=8,txt=f"The total due amount is {df["total_price"].sum()} Euros.",align="L",ln=1)
    pdf.cell(w=0,h=8,txt=f"Powered by aratheunseen",align="L",ln=1)
    
    pdf.output(f"invoices/{invoice_no}.pdf")
