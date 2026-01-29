# Invoice Generator 📄

A professional invoice generation application built with Streamlit that allows you to create and download PDF invoices for your business.

## Features ✨

- **Company Management**: Load and select from multiple companies stored in CSV format
- **Product Selection**: Choose from a range of products with customizable quantities
- **PDF Generation**: Automatically generates professional PDF invoices
- **Company Branding**: Includes company logo in the invoice header
- **Real-time Preview**: View the generated invoice directly in the browser
- **Instant Download**: Download invoices as PDF files

## Project Structure 📁

```
laksh/
├── code_1.py           # Main Streamlit application
├── company.csv         # Company/customer data
├── product.csv         # Product catalog
├── company_logo.png    # Company logo for invoices
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Installation 🚀

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd d:\my_projects\My_office_projects\laksh
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage 💻

### Running the Application

1. **Start the Streamlit server**
   ```bash
   streamlit run code_1.py
   ```
   
   Or alternatively:
   ```bash
   python -m streamlit run code_1.py
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://localhost:8501`
   - The application will automatically open in your default browser

### Generating Invoices

1. **Select a Company**: Use the sidebar dropdown to choose a company from your customer list
2. **Select Products**: Choose one or more products from the multiselect dropdown
3. **Set Quantities**: For each selected product, specify the quantity using the number input
4. **Generate Invoice**: Click the "Generate Invoice" button
5. **Download**: Use the download button to save the PDF invoice to your computer

### Data Files

#### company.csv
This file should contain your customer/company information with the following columns:
- `company_id`: Unique identifier for the company
- `company_name`: Name of the company
- `address`: Company address
- `mobile`: Contact phone number
- `email`: Contact email address

#### product.csv
This file should contain your product catalog with the following columns:
- `product_name`: Name of the product
- `description`: Product description
- `price`: Unit price of the product

## Configuration ⚙️

### Company Information

The invoice header includes static company information for **PRISTONIX TECHNOLOGIES PRIVATE LIMITED**. To customize this:

1. Open `code_1.py`
2. Locate lines 28-34 in the `generate_invoice()` function
3. Update the company details:
   - Company name
   - Location
   - Pincode
   - Email
   - Phone number

### Company Logo

- Place your company logo as `company_logo.png` in the project root directory
- Recommended size: 400x400 pixels or similar square dimensions
- Supported formats: PNG (with transparent background recommended)

## Generated Files 📦

The application generates PDF invoices with the naming convention:
```
invoice_{company_id}.pdf
```

These files are saved in the project root directory.

## Dependencies 📚

- **Streamlit**: Web application framework for creating the user interface
- **Pandas**: Data manipulation and CSV file handling
- **fpdf**: PDF generation library for creating invoice documents

## Troubleshooting 🔧

### Common Issues

1. **Module not found error**
   - Ensure you've activated the virtual environment
   - Run: `pip install -r requirements.txt`

2. **CSV encoding issues**
   - The application uses ISO-8859-1 encoding
   - Ensure your CSV files are saved with compatible encoding

3. **Logo not appearing**
   - Check that `company_logo.png` exists in the project directory
   - Verify the file format is PNG

4. **Port already in use**
   - Streamlit uses port 8501 by default
   - Kill any existing Streamlit processes or use: `streamlit run code_1.py --server.port 8502`

## Future Enhancements 🚀

Potential features for future development:
- [ ] Tax calculation (GST/VAT)
- [ ] Multiple currency support
- [ ] Invoice numbering system
- [ ] Database integration
- [ ] Email invoice delivery
- [ ] Invoice history and search
- [ ] Custom invoice templates
- [ ] Payment tracking

## License 📄

This project is part of laksh2006 internal tools.

**Built with ❤️ using Streamlit**
