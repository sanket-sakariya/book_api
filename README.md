Here’s a complete and professional `README.md` file tailored for your **Book Catalog RESTful API with authentication and file upload**, as per the assignment requirements.

---

````markdown
 📚 Book Catalog API

A Django RESTful API for managing a book catalog, with support for custom API key authentication and book cover image uploads.

---

 🚀 Features

- 📖 CRUD operations for books
- 🔐 API key-based authentication
- 🖼️ Upload book cover images (JPG, PNG, WEBP)
- ✅ Input validation (ISBN, page count, published date)
- 🔄 Tested via Postman collection

---
````

 🛠️ Setup Instructions

 1. Clone the repository

```bash
git clone https://github.com/yourusername/book_api.git
cd book_api
```

 2. Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
 OR
source venv/bin/activate  # Linux/Mac
```

 3. Install dependencies

```bash
pip install -r requirements.txt
```

 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

 5. Run the server

```bash
python manage.py runserver
```

---

 🔐 API Key Configuration

 Option 1: Use `.env` file

Create a `.env` file in your project root:

```env
API_KEYS=valid-api-key
```

Use `python-decouple` or `os.environ.get()` in `settings.py` to access it:

```python
from decouple import config

API_KEYS = config("API_KEYS").split(",")
```

 Option 2: Hard-code (Not Recommended)

```python
API_KEYS = ["valid-api-key"]
```

---

 🧪 Postman Testing

 📤 Import Postman Collection

1. Open Postman
2. Go to **Collections → Import**
3. Select the `book_api_collection.json` file from this repo

---

 📬 API Endpoints Summary

| Method | Endpoint                        | Auth Required | Description                |
| ------ | ------------------------------- | ------------- | -------------------------- |
| GET    | `/api/books/`                   | ❌             | List all books (paginated) |
| POST   | `/api/books/`                   | ✅             | Create a new book          |
| GET    | `/api/books/<pk>/`              | ❌             | Get details of a book      |
| PUT    | `/api/books/<pk>/`              | ✅             | Update a book              |
| DELETE | `/api/books/<pk>/`              | ✅             | Delete a book              |
| POST   | `/api/books/<pk>/upload-cover/` | ✅             | Upload cover image         |

---

 ✅ Validation Rules

* `isbn`: Must be exactly 13 characters
* `page_count`: Minimum of 1
* `published_date`: Cannot be in the future
* `cover`:

  * Max size: 2MB
  * File types: JPG, PNG, WEBP

---

## 🖼️ Cover Upload Sample Response (200 OK)

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "cover_url": "http://localhost:8000/media/covers/gatsby.jpg",
  "message": "Cover uploaded successfully"
}
```

---

## 🚫 Invalid File Type Response (400)

```json
{
  "error": "INVALID_FILE_TYPE",
  "message": "Only JPG, PNG, and WEBP files are allowed",
  "allowed_types": ["jpg", "png", "webp"],
  "received_type": "pdf"
}
```

---

## 🔐 Unauthorized Access (401)

```json
{
  "error": "INVALID_API_KEY",
  "message": "Missing or invalid API key"
}
```


 👨‍💻 Developed By

[GitHub Profile](https://github.com/sanket-sakariya)

```
