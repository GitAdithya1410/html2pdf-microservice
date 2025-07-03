# HTML2PDF Microservice

## 📄 Description

A lightweight Flask-based microservice that accepts raw HTML and returns a Base64-encoded PDF. Useful for integrations with CAP, automation scripts, or any service that needs dynamic PDF generation.

---

## 🔌 Endpoints

### `GET /`
Health check endpoint. Returns a confirmation message.

### `POST /convert`
- **Request Body:** Raw HTML (`text/html`)
- **Response:** JSON object with base64-encoded PDF

#### Example Response:
```json
{
  "pdf_base64": "JVBERi0xLjQKJeLjz9MK..."
}
