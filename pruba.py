from fpdf import FPDF
""" pip install fpdf """

proyecto = input("Ingrese el nombre del proyecto: ")
descripcion = input("Ingrese la descripción del proyecto: ")
horas_estimadas = input("Ingrese las horas estimadas para completar el proyecto: ")
valor_hora = input("Ingrese el valor por hora de trabajo: ")
plazo_entrega = input("Ingrese el plazo de entrega del proyecto: ")

valor_total = int(horas_estimadas) * int(valor_hora)

print(proyecto)
print(descripcion)


print(valor_total)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

pdf.image("Template.png", 0, 0)
pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, plazo_entrega)
pdf.text(115, 205, str(valor_total))
pdf.output("proyecto.pdf")