import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Step 1: Read Data
df = pd.read_csv("data.csv")

# Step 2: Analyze Data
total_rows = len(df)
mean_values = df.mean(numeric_only=True)

# Step 3: Create PDF
doc = SimpleDocTemplate("report.pdf")
elements = []

styles = getSampleStyleSheet()
elements.append(Paragraph("<b>Automated Report</b>", styles["Title"]))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph(f"Total Records: {total_rows}", styles["Normal"]))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Mean Values:</b>", styles["Heading2"]))
elements.append(Spacer(1, 0.2 * inch))

for column, value in mean_values.items():
    elements.append(Paragraph(f"{column}: {value:.2f}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

doc.build(elements)

print("Report Generated Successfully!")
