from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.set_fill_color(100,100,100)
    pdf.line(10,21,200,21)

    # For lined notebook
    pdf.set_fill_color(100,100,100)
    for line_height in range (0,245,10):
        pdf.line(10,21+line_height,200,21+line_height)

    #  For footer text 
    pdf.ln(244)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")

    for page in range(row['Pages']-1):
        pdf.add_page()

        # For lined notebook
        pdf.set_fill_color(100,100,100)
        for line_height in range (0,245,10):
            pdf.line(10,21+line_height,200,21+line_height)

        #  For footer text
        pdf.ln(256)
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    
# pdf.output("notebook.pdf")

pdf.output("notebook_line.pdf")