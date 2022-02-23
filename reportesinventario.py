# Impresion de Inventarios
import os.path
import subprocess
inventario1 = "/home/caja/Descargas/inventarios/inventarioAdentro.pdf"
inventario2 = "/home/caja/Descargas/inventarios/inventarioAfuera.pdf"
inventario3 = "/home/caja/Descargas/inventarios/inventarioCarnesVegetales.pdf"
#Los xlsx que seran pasados a PDF
pdf1 ="/home/caja/Descargas/inventarios/inventarioCarnesVegetales.xlsx"
pdf2 ="/home/caja/Descargas/inventarios/inventarioAfuera.xlsx"
pdf3 ="/home/caja/Descargas/inventarios/inventarioAdentro.xlsx"


def generador_de_pdf(pdf1, pdf2, pdf3):
    subprocess.run(["libreoffice", "--convert-to", "pdf", pdf1 ])
    subprocess.run(["libreoffice", "--convert-to", "pdf", pdf2 ])
    subprocess.run(["libreoffice", "--convert-to", "pdf", pdf3 ])
    return pdf1,pdf2,pdf3
def impresiones(inventario1,inventario2,inventario3):
    subprocess.run(["lpr", "-P", "EPSON-TM-T20II", inventario1])
    subprocess.run(["lpr", "-P", "EPSON-TM-T20II", inventario2])
    subprocess.run(["lpr", "-P", "EPSON-TM-T20II", inventario3])
    return inventario1,inventario2,inventario3

generador_de_pdf(pdf1,pdf2,pdf3)
impresiones(inventario1,inventario2, inventario3)
