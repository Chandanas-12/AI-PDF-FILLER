AI PDF Filler

Project Overview:
The AI PDF Filler project automates the extraction of structured company-related data from a text file and populates a PDF form with this data. This project is particularly useful for generating standardized reports for businesses or organizations based on dynamically changing data.

Key Features:

1.Data Extraction: Extracts various fields from a structured text file (dummy_data.txt) using regular expressions, ensuring accurate data retrieval.

2.PDF Form Filling: Utilizes the PyPDF2 library to fill a PDF form (new_dummy_form.pdf) with extracted company data.

3.Dynamic Field Mapping: Maps extracted data to corresponding fields in the PDF form based on predefined rules, allowing for easy modifications.

4.Error Handling: Incorporates robust error handling, providing informative messages for missing fields and issues during data extraction or PDF filling.

5.Customizable Output: The filled PDF can be customized based on user needs, allowing for different company profiles and reports.


Installation

Clone the Repository: Download or clone this project to your local machine.

git clone <repository-url>
cd AI_PDF_Filler

Set Up a Virtual Environment (optional but recommended):
python -m venv .venv

Activate the Virtual Environment:
Windows:
.venv\Scripts\activate
Mac/Linux:
source .venv/bin/activate
Install Required Dependencies:
pip install PyPDF2

File Structure
main.py: The main script for extracting data and filling the PDF.
dummy_data.txt: The text file containing structured company data to be extracted.
new_dummy_form.pdf: The PDF form that will be populated with extracted data.
output/: The directory where the filled PDF will be saved.

Usage
Run the Script: Execute the Python script to extract data and fill the PDF form:
python main dummy.py # pdf generated using parsing and mapping of data programatically



Check the Output: The filled PDF will be saved in the output/ directory with the name filled_form_TechNova_Solutions_Inc.pdf.

Key Functions
load_data_from_text(file_path): Reads and extracts structured data from the specified text file.
extract_field(content, pattern): A helper function that extracts specific fields from the content using regex patterns.
print_pdf_fields(pdf_path): Prints the available fields in the PDF form for debugging purposes.
map_fields_to_pdf(extracted_data): Maps the extracted data to the corresponding PDF form fields based on predefined rules.
fill_pdf_form(input_pdf, output_pdf, data): Fills the PDF form using the mapped data and saves it as a new file.

Error Handling
The script includes checks for missing fields and will print error messages if any required fields are not found during data extraction or if there are issues with the PDF form filling.
Ensure that the field names in the PDF form match the mappings specified in the map_fields_to_pdf() function for successful data filling.

Future Improvements
User Interface: Consider developing a graphical user interface (GUI) to simplify user interaction and file selection.
Configurable Mappings: Implement a configuration file to allow users to modify field mappings without changing the code.
Support for Multiple Data Formats: Expand the script to support data extraction from various formats (e.g., CSV, JSON).
Enhanced Validation: Add validation to ensure data accuracy and completeness before PDF generation.
