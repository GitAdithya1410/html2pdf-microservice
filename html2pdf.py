from flask import Flask, request, jsonify
import pdfkit
import base64
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_pdf():
    html = request.data.decode('utf-8')

    # Save HTML to temp file
    with open("temp.html", "w", encoding='utf-8') as f:
        f.write(html)

    # Convert HTML to PDF using wkhtmltopdf
    pdf_path = "output.pdf"
    pdfkit.from_file("temp.html", pdf_path)

    # Encode PDF as base64
    with open(pdf_path, "rb") as f:
        pdf_base64 = base64.b64encode(f.read()).decode("utf-8")

    # Clean up files
    os.remove("temp.html")
    os.remove(pdf_path)

    return jsonify({ "pdf_base64": pdf_base64 })

@app.route('/', methods=['GET'])
def hello():
    return "HTML2PDF service running."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
