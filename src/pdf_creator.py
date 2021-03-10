from fpdf import FPDF
from datetime import date
from src.diagnose import diagnose

def create_PDF(patient_name, patient_email, xray_date, xray_path):
    '''
    Given a name, email, xray date and xray file path, generates PDF
    with a Pneumonia diagnosis

    Takes: name, email, xray date and xray file path
    Returns: path for PDF with Pneumonia diagnosis
    '''

    # create pdf object with default params
    pdf = FPDF()

    # add a page to start "writing"
    pdf.add_page()

    # length and width of A4 page
    # pdf_w=210
    # pdf_h=297

    # draw two rectangles as a margin and fill with grey
    pdf.set_fill_color(128, 128, 128) # RGB
    
    pdf.rect(5.0, 5.0, 200.0,287.0, "DF") # abscissa upper left corner, ordinate top left, rec width, rec height, fill style
    pdf.set_fill_color(255, 255, 255)

    pdf.rect(8.0, 8.0, 194.0,282.0, "FD")

    # insert logo on top right corner
    pdf.set_xy(175.0,12.0)
    pdf.image('images/healthcare_logo.png', w=20.0)
    
    # add title
    pdf.set_xy(100.0,20.0)
    pdf.set_font('Arial', 'B', 16) # family, style, size
    pdf.set_text_color(0, 0, 50) # RGB
    pdf.cell(w=5.0, h=40.0, align='C', txt="PNEUMONIA TEST", border=0)
    
    # insert x-ray image
    pdf.set_xy(20.0,135.0)
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(64,64,64)
    pdf.cell(173, 8, "Patient's X-ray", border = 1)
    
    pdf.set_xy(42.5,160.0)
    pdf.image(xray_path, w=120.0)
    
    # inset text comments
    pdf.set_xy(20.0,50.0)
    pdf.set_font("Arial", "U", 12)
    pdf.set_text_color(64,64,64)

    diagnosis = diagnose(img_path = xray_path)
    pdf.cell(30, 15, f"Patient name:")
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(30, 15, f"{patient_name.upper()}", ln = 1)

    pdf.set_xy(20.0,65.0)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(30, 15, f"Patient email:")
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(30, 15, f"{patient_email}", ln = 1)

    pdf.set_xy(20.0,80.0)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(30, 15, f"Report date:")

    pdf.set_font("Arial", "", 12)
    pdf.cell(30, 15, f"{date.today()}", ln = 1)
    
    pdf.set_xy(20.0,105.0)
    pdf.cell(30, 15, f"As of {xray_date}, the patient presents the following diagnosis for Pneumonia: {diagnosis.upper()} ")
    
    # save file
    save_path = f"diagnosis_PDFs/{patient_name} - {date.today()}"
    pdf.output(save_path, "F")

    return save_path