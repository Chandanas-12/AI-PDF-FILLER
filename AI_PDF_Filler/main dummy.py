import re
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

def load_data_from_text(file_path):
    """Reads the data from the text file and returns it as a dictionary."""
    data = {}
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract fields based on known patterns
        data['Company Name'] = re.search(r'Company Name:(.+)', content).group(1).strip()
        data['Founded'] = re.search(r'Founded:(.+)', content).group(1).strip()
        data['CEO'] = re.search(r'CEO:(.+)', content).group(1).strip()
        data['Industry'] = re.search(r'Industry:(.+)', content).group(1).strip()
        data['Revenue'] = re.search(r'Revenue:(.+)', content).group(1).strip()
        data['Net Income'] = re.search(r'Net Income:(.+)', content).group(1).strip()
        data['Main Products'] = re.search(r'Main Products:(.+)', content).group(1).strip()
        data['Number of Employees'] = re.search(r'Number of Employees:(.+)', content).group(1).strip()
        data['Headquarters'] = re.search(r'Headquarters:(.+)', content).group(1).strip()
        data['Website'] = re.search(r'Website:(.+)', content).group(1).strip()
        data['Operating Income'] = re.search(r'Operating Income:(.+)', content).group(1).strip()
        data['Market Capitalization'] = re.search(r'Market Capitalization:(.+)', content).group(1).strip()
        data['Profit Margin'] = re.search(r'Profit Margin:(.+)', content).group(1).strip()
        data['Return on Equity (ROE)'] = re.search(r'Return on Equity \(ROE\):(.+)', content).group(1).strip()
        data['Debt to Equity Ratio'] = re.search(r'Debt to Equity Ratio:(.+)', content).group(1).strip()
        data['Current Ratio'] = re.search(r'Current Ratio:(.+)', content).group(1).strip()
        data['P/E Ratio'] = re.search(r'P/E Ratio:(.+)', content).group(1).strip()
        data['Dividend Yield'] = re.search(r'Dividend Yield:(.+)', content).group(1).strip()
        data['Revenue Growth (YoY)'] = re.search(r'Revenue Growth \(YoY\):(.+)', content).group(1).strip()
        data['R&D Expenses'] = re.search(r'R&D Expenses:(.+)', content).group(1).strip()
        data['Customer Acquisition Cost'] = re.search(r'Customer Acquisition Cost:(.+)', content).group(1).strip()
        data['Customer Lifetime Value'] = re.search(r'Customer Lifetime Value:(.+)', content).group(1).strip()
        data['Market Share'] = re.search(r'Market Share:(.+)', content).group(1).strip()
        data['Competitors'] = re.search(r'Competitors:(.+)', content).group(1).strip()
        data['Recent News'] = re.search(r'Recent News:(.+)', content).group(1).strip()
        data['Future Outlook'] = re.search(r'Future Outlook Summary:(.+)', content).group(1).strip()
        data['ESG Initiatives'] = re.search(r'ESG Initiatives:(.+)', content).group(1).strip()

    except Exception as e:
        print(f"An error occurred while reading the text file: {e}")
    
    return data

def print_pdf_fields(pdf_path):
    """Prints the form fields in the specified PDF."""
    reader = PdfReader(pdf_path)
    form_fields = reader.get_form_text_fields()
    print("Form fields in PDF:")
    for field in form_fields:
        print(field)

def calculate_years_since_founded(founded_date_str):
    """Calculates the number of years since the company was founded."""
    founded_date = datetime.strptime(founded_date_str, '%Y-%m-%d')
    current_date = datetime.now()
    return current_date.year - founded_date.year

def map_fields_to_pdf(extracted_data):
    """Map the extracted data to the corresponding PDF form fields."""
    mapped_data = {}
    rules = {
        'Text-OrN6IEuUMK': 'Company Name',
        'Text-_NjjkC36_y': 'Founded',
        'Text-R5QrMNRgBI': 'CEO',
        'Text-t7jthyYnmR': 'Industry',
        'Text-FjLkuiZK7W': 'Net Income',  # Update field name for Net Income
        'Text-NyiEFw8Q73': 'Revenue',  # Update field name for Revenue
        'Text-r8WYKkKnF5': 'Main Products',
        'Text-Ftzrb-tq1p': 'Number of Employees',
        'Text-1eXkNHJD3o': 'Headquarters',
        'Text-kmd8gDGQr5': 'Website',
        'Text-3wFskU85I1': 'Operating Income',
        'Text-1Z98_16rNR': 'Market Capitalization',
        'Text-3PhzHkBoTy': 'Profit Margin',
        'Text-4RmI85phMZ': 'Return on Equity (ROE)',
        'Text-L8cf1b5HSH': 'Debt to Equity Ratio',
        'Text-PyO5Ep61Hu': 'Current Ratio',
        'Text-9eS5I9ALsB': 'P/E Ratio',
        'Text-3gJPsDhe9O': 'Dividend Yield',
        'Text-8U0GZc91Li': 'Revenue Growth (YoY)',
        'Text-NGQezHBuAX': 'R&D Expenses',
        'Text-LndjQt97gS': 'Customer Acquisition Cost',
        'Text-ZIXBcKIn2h': 'Customer Lifetime Value',
        'Text-5b4Zy7Qz3y': 'Market Share',
        'Text-7Cka8b9QGx': 'Competitors',
        'Text-KMcNPu7pFe': 'Recent News',
        'Text-9phO6QJcBt': 'Future Outlook',
        'Text-CcNlPQMa7C': 'ESG Initiatives',
        # Additional questions
        'Paragraph-QjM9gEKVQj': 'Carbon Neutrality Target Year',  # Assuming this is the field
        'Paragraph-_VS4VzdgsU': 'Projected Growth Rate',
        'Text-1PdbN2ew5G': 'Years Since Founded'
    }

    for pdf_field, data_key in rules.items():
        if data_key in extracted_data:
            mapped_data[pdf_field] = extracted_data[data_key]
            print(f"Mapped {data_key} to {pdf_field}: {extracted_data[data_key]}")
        elif data_key == 'Years Since Founded':
            # Calculate years since founded
            mapped_data[pdf_field] = str(calculate_years_since_founded(extracted_data['Founded']))
        else:
            print(f"Field {data_key} not found in extracted data.")
    
    return mapped_data

def fill_pdf_form(input_pdf, output_pdf, data):
    """Fills the PDF form using the mapped data."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Fill in the form fields
    writer.add_page(reader.pages[0])
    writer.update_page_form_field_values(writer.pages[0], data)

    # Write the filled form to a new PDF
    with open(output_pdf, "wb") as out_pdf:
        writer.write(out_pdf)

def main():
    print_pdf_fields('data/new_dummy_form.pdf')

    extracted_data = load_data_from_text('data/Dummy_data.txt')

    mapped_data = map_fields_to_pdf(extracted_data)
    fill_pdf_form('data/new_dummy_form.pdf', 'output/filled_form_TechNova_Solutions_Inc.pdf', mapped_data)

if __name__ == "__main__":
    main()
