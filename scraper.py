import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


class Scraper:
    def __init__(self):
        self.URL = 'https://es.wikipedia.org/wiki/'
        self.query = ""

        self.page = ""

    def askQuery(self):
        self.query = input('¿What do you want to search in wikipedia?')
        self.query.replace(' ', '_')
        complete_url = self.URL + self.query
        r = requests.get(complete_url)
        self.page = r.content

        if r.ok:
            return True
        else:
            return False

    def convertToPdf(self):
        soup = BeautifulSoup(self.page, 'html.parser')
        title = soup.find("h1", {"id": "firstHeading"})

        divTag = soup.find_all("div", {"class": "mw-parser-output"})
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, title.text, 0, 1, 'C')
        pdf.set_font('Arial', '', 11)
        for tag in divTag:
            content = tag.find_all("p")
            for x in content:
                text = x.text
                text2 = text.encode('latin-1', 'replace').decode('latin-1')
                text2 = text2.replace('?', '')
                pdf.multi_cell(0, 10, text2)

        pdf.output(self.query+'.pdf', 'F')


scraper = Scraper()
is_valid_website = scraper.askQuery()
if is_valid_website:
    print('waiting...')
    scraper.convertToPdf()
    print('Complete.')
else:
    print('page not found')
