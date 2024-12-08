# Library Management System API

## How to Run

Follow these steps to get your application up and running:

1. **Clone the repository**:
   First, clone the repository to your local machine.
   ```bash
git clone https://github.com/Shrikrishna-Jadhav/Library-Management-System
cd Library-Management-System
2. Set up a virtual environment: It's recommended to set up a virtual environment to keep your dependencies isolated.
python -m venv venv
# For Windows
venv\Scripts\activate
# For Linux/macOS
source venv/bin/activate
3.Install dependencies: Install all the necessary dependencies by running:
pip install -r requirements.txt
4.Run the app: To start the Flask application, use the following command:
python run.py
API Endpoints
1. GET /api/books - Get all books
 Test in Browser: Open your browser and go to:
http://127.0.0.1:5000/api/books
Test with Postman: Send a GET request to http://127.0.0.1:5000/api/books.
Example JSON body:
{
  "title": "Book Title",
  "author": "Author Name",
  "published_year": 2025
}
option 2: Test with cURL(Go to terminal and paste this and run)
curl -X POST -H "Content-Type: application/json" -d '{"title": "Book Title", "author": "Author Name", "published_year": 2025}' http://127.0.0.1:5000/api/books
2.GET /api/books/{id} - Get a book by its ID
Test with curl 
curl http://127.0.0.1:5000/api/books/1
3. PUT /api/books/{id} - Update a book's details
Test with cURL
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Book Title", "author": "Updated Author Name", "published_year": 2026}' http://127.0.0.1:5000/api/books/1
4.DELETE /api/books/{id} - Delete a book by its ID
Test with cURL:
curl -X DELETE http://127.0.0.1:5000/api/books/1



