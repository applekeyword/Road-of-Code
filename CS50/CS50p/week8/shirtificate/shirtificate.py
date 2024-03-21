from fpdf import FPDF

A4_WIDTH = 210
A4_HEIGHT = 297

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", size=12)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def add_shirt(self, name):
        self.image("shirtificate.png", x=A4_WIDTH/2 - 50, w=100)

        self.set_text_color(255, 255, 255)
        self.set_xy(A4_WIDTH/2 - 20, A4_HEIGHT/2 - 100)
        self.set_font("Helvetica", size=16)
        self.cell(40, 10, name + " took CS50", ln=True, align="C")


def create_shirtificate(name):
    pdf = Shirtificate(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")


def main():
    name = input("Please enter your name: ")
    create_shirtificate(name)


if __name__ == "__main__":
    main()
