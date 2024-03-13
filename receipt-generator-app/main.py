import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id":str})


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        return in_stock


class Receipt:
    def __init__(self, article_id, article_object):
        self.article_id = article_id
        self.article = article_object

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", style="B",size=16)
        pdf.cell(h=8, w=0, txt=f"Receipt ID. {self.article.id}", ln=1)

        pdf.set_font(family="Times", style="B",size=16)
        pdf.cell(h=8, w=0, txt=f"Name: {self.article.name}", ln=1)

        pdf.set_font(family="Times", style="B",size=16)
        pdf.cell(h=8, w=0, txt=f"Price: {self.article.price}", ln=1)

        pdf.output(f"receipt_{article.id}.pdf")


print(df)
article_id = input("Enter the article ID: ")
article = Article(article_id)

if article.available():
    receipt = Receipt(article_id, article)
    receipt.generate()
else:
    print("No article found.")