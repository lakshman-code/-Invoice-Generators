import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64
import os

# ==============================
# Load Data
# ==============================
customers = pd.read_csv("company.csv", encoding="ISO-8859-1")
products = pd.read_csv("product.csv", encoding="ISO-8859-1")

# ==============================
# Function to Generate PDF Invoice
# ==============================
def generate_invoice(company, selected_products_df, quantities):
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", 'B', size=30)
    pdf.cell(200, 10, txt="INVOICE", ln=True, align='C')

    # Company Logo
    if os.path.exists("company_logo.png"):
        pdf.image("company_logo.png", x=160, y=25, w=40)

    # Static Company Header
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TECHNOLOGIES PRIVATE LIMITED", ln=True)
    pdf.cell(200, 10, txt="India, Chennai", ln=True)
    pdf.cell(200, 10, txt="Pincode: 600016", ln=True)
    pdf.cell(200, 10, txt="Email: mail.", ln=True)
    pdf.cell(200, 10, txt="7984321437", ln=True)

    # Selected Customer Details
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt="Company Details:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {company['company_name']}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {company['address']}", ln=True)
    pdf.cell(200, 10, txt=f"Mobile: {company['mobile']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {company['email']}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)

    # Table Header
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(60, 10, "Product", border=1)
    pdf.cell(60, 10, "Description", border=1)
    pdf.cell(20, 10, "Qty", border=1)
    pdf.cell(30, 10, "Unit Price", border=1)
    pdf.cell(30, 10, "Total", border=1)
    pdf.ln()

    # Table Rows
    total = 0
    pdf.set_font("Arial", size=12)
    for idx, (i, product) in enumerate(selected_products_df.iterrows()):
        quantity = quantities[idx]
        line_total = product['price'] * quantity
        total += line_total
        pdf.cell(60, 10, product['product_name'], border=1)
        pdf.cell(60, 10, product.get('description', 'No description'), border=1)
        pdf.cell(20, 10, str(quantity), border=1)
        pdf.cell(30, 10, f"{product['price']:.2f}", border=1)
        pdf.cell(30, 10, f"{line_total:.2f}", border=1)
        pdf.ln()

    # Total Amount
    pdf.cell(200, 10, "", ln=True)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(170, 10, "Total", border=1)
    pdf.cell(30, 10, f"{total:.2f}", border=1)

    # Save PDF
    filename = f"invoice_{company['company_id']}.pdf"
    pdf.output(filename)
    return filename

# ==============================
# Streamlit UI
# ==============================
st.title("Invoice Generator")
st.sidebar.header("Select Company and Products")

# Select Company
company_names = customers["company_name"].tolist()
selected_company = st.sidebar.selectbox("Choose a company", company_names)
selected_company_row = customers[customers["company_name"] == selected_company].iloc[0]

# Select Products
product_names = products["product_name"].tolist()
selected_product_names = st.sidebar.multiselect("Select Products", product_names)
selected_products_df = products[products["product_name"].isin(selected_product_names)]

# Get Quantities
quantities = []
for product_name in selected_product_names:
    quantity = st.sidebar.number_input(f"Quantity for {product_name}", min_value=1, max_value=100, value=1)
    quantities.append(quantity)

# Generate Invoice Button
if st.sidebar.button("Generate Invoice"):
    if len(selected_products_df) != len(quantities):
        st.error("Mismatch between selected products and quantities")
    else:
        invoice_file = generate_invoice(selected_company_row, selected_products_df, quantities)

        if invoice_file and os.path.exists(invoice_file):
            # Download Button
            with open(invoice_file, "rb") as f:
                st.download_button("Download Invoice", f, file_name=invoice_file, mime="application/pdf")

            # Display PDF in App
            with open(invoice_file, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>',
                unsafe_allow_html=True
            )

# Show Selected Info
if selected_product_names:
    st.write("### Selected Products and Quantities:")
    for i, product_name in enumerate(selected_product_names):
        st.write(f"- {product_name}: {quantities[i]} units")
else:
    st.write("No products selected.")
