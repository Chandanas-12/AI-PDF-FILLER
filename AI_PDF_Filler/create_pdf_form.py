from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_exact_pdf_with_tables(output_path):
    # Create a canvas for the PDF
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Title Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Questionnaire")

    # First Table: Company Information (Company Name, Founded, Industry, Net Income)
    table_data_1 = [
        ["Company Name", ""],
        ["Founded", ""],
        ["Industry", ""],
        ["Net Income", ""]
    ]

    # Define column widths for the table
    col_widths_1 = [2.5 * inch, 4.0 * inch]

    # Create the first table
    table_1 = Table(table_data_1, colWidths=col_widths_1)
    table_1.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color (black)
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Position and draw the first table on the page
    table_1.wrapOn(c, 50, 650)
    table_1.drawOn(c, 50, 650)

    # Second Table: Financial Ratios, Future Outlook, Main Products, Customer Lifetime Value
    # Financial Ratios Sub-table for Profit Margin, Current Ratio, and Debt to Equity Ratio
    financial_ratios_sub_table = [
        ["Profit Margin", ""],
        ["Current Ratio", ""],
        ["Debt to Equity Ratio", ""]
    ]
    
    # Reduce the width of the sub-table columns slightly
    financial_ratios_sub = Table(financial_ratios_sub_table, colWidths=[1.8 * inch, 1.8 * inch])
    financial_ratios_sub.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))

    # Main table data
    table_data_2 = [
        ["Financial Ratios", financial_ratios_sub],  # Add the sub-table here
        ["Future Outlook Summary", ""],
        ["Main Products", ""],
        ["Customer Lifetime Value", ""]
    ]

    # Define column widths for the second table
    col_widths_2 = [2.5 * inch, 5.0 * inch]

    # Create the second table
    table_2 = Table(table_data_2, colWidths=col_widths_2)
    table_2.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color (black)
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Position and draw the second table on the page
    table_2.wrapOn(c, 50, 450)
    table_2.drawOn(c, 50, 450)

    # Questions Section
    c.setFont("Helvetica", 9)  # Set font size for questions
    question_y_position = 380  # Starting y position for the questions

    # Placeholders for questions without lines
    questions = [
        "1. What is WECOMMIT dummy Inc.'s specific target year for achieving carbon neutrality, and what does this goal entail?",
        "2. How many women are on the board of directors of WECOMMIT dummy Inc., and what percentage of the board does this represent?"
    ]

    for question in questions:
        c.drawString(50, question_y_position, question)  # Draw the question placeholder
        question_y_position -= 35  # Increase the spacing between questions

    # Add space between the second question and the table
    question_y_position -= 50  # Add additional space before the next table

    # New Table Section for Additional Questions
    additional_questions_data = [
        ["What is the projected growth rate for WECOMMIT dummy Inc.'s cloud services division in the upcoming fiscal year?", ""],
        ["How many years has it been since WECOMMIT dummy Inc. was founded from now?", ""]
    ]

    # Create the new additional questions table
    additional_questions_table = Table(additional_questions_data, colWidths=[5.0 * inch, 2.0 * inch])  # Increased column width for better spacing
    additional_questions_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 6.9),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Draw the additional questions table on the canvas
    additional_questions_table.wrapOn(c, 50, question_y_position - 20)  # Adjust position
    additional_questions_table.drawOn(c, 50, question_y_position - 20)  # Draw the table

    # Save the PDF
    c.save()

# Example usage
output_pdf = "data/exact_questionnaire_with_increased_table_size.pdf"
create_exact_pdf_with_tables(output_pdf)
print(f"PDF created: {output_pdf}")
