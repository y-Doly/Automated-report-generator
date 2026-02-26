import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#Read Data
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: data.csv file not found!")
    exit()
Analyze Data
total_rows = len(df)
mean_values = df.mean(numeric_only=True)

#Create PDF
doc = SimpleDocTemplate("report.pdf")
elements = []
styles = getSampleStyleSheet()

#Title
elements.append(Paragraph("Automated Report", styles["Title"]))
elements.append(Spacer(1, 0.5 * inch))

#Total Records
elements.append(Paragraph(f"Total Records: {total_rows}", styles["Normal"]))
elements.append(Spacer(1, 0.3 * inch))

#Mean Values
elements.append(Paragraph("Mean Values:", styles["Heading2"]))
elements.append(Spacer(1, 0.2 * inch))

if not mean_values.empty:
    for column, value in mean_values.items():
        elements.append(Paragraph(f"{column}: {value:.2f}", styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))
else:
    elements.append(Paragraph("No numeric columns found.", styles["Normal"]))

#Build PDF
doc.build(elements)

print("Report Generated Successfully!")
