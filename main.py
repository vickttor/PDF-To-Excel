import tabula
import pandas as pd

# Caminho do arquivo PDF
pdf_path = "./pdf/leads.pdf"

# Função para extrair texto de um PDF
def extract_tables_from_pdf(pdf_path):
    # Try different options for extracting tables 
    # You might need to adjust parameters based on your PDF structure
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=False, guess=True, encoding='UTF-16') 
    except Exception as e:
        print(f"Error extracting tables: {e}")
        return []

    return tables

# Extrair tabelas do PDF
tables = extract_tables_from_pdf(pdf_path)

# Criar o DataFrame do Pandas
# Assuming the first table is the one you want
df = pd.concat(tables, ignore_index=True)

# Salvar o DataFrame em um arquivo Excel
excel_path = "./out/leads.xlsx"
df.to_excel(excel_path, index=False)

print("Dados salvos em:", excel_path)