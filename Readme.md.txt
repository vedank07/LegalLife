Legal Life
This repository hosts the Flask backend and Frontend for the Legal Life project, which aims to assist legal professionals and users in document generation, analysis, and retrieval of legal information.

Introduction
Legal Life comprises a Flask-based backend that leverages various functionalities to interact with databases, perform semantic searches, and summarize legal documents.

Features
1. Database Connectivity
The backend connects to a MySQL database to retrieve legal documents and information. It uses the mysql.connector library to establish connections and execute SQL queries.

2. Semantic Search
Using the ChromaDB library, the backend offers semantic search capabilities. This functionality allows users to input queries and retrieve relevant legal documents based on semantics and context.

3. Summary and Analysis
The backend provides functionality to summarize and analyze legal documents. It aims to extract crucial details such as involved parties, timeframes, and key points from uploaded PDF or TXT files.

Requirements
Python 3.x: The backend is built using Python.
Flask: Used for creating the API endpoints and handling requests.
Flask-CORS: Enables Cross-Origin Resource Sharing for API requests.
MySQL Connector: Required for connecting and interacting with the MySQL database.
OpenAI's GPT-3.5 Model: Utilized for natural language processing tasks.
ChromaDB: Used for semantic search functionality.
Installation
Cloning the Repository:

bash
Copy code
git clone https://github.com/your_username/Legal-Life-Flask-Backend.git
Installing Dependencies:

bash
Copy code
pip install -r requirements.txt
Database Setup:

Create a MySQL database named Law.
Update the host, user, password, and database_name variables in the code with your database credentials.
Usage
Running the Application:

bash
Copy code
python app.py
Endpoints:

/api: Receives legal queries and generates appropriate responses.
/file: Accepts PDF or TXT files, extracts text, and provides a summary and analysis of the legal document.
/search: Performs a semantic search within the connected legal document database.
/searchDb: Searches the local MySQL database for specific legal terms.
Code Explanation
Database Connectivity (DbSearch)
The DbSearch function establishes a connection to the MySQL database and performs a SQL query to retrieve relevant legal documents based on a search term. It showcases basic usage of the mysql.connector library.

Semantic Search (SementicSearch)
This function utilizes ChromaDB's collection.query method to perform a semantic search within the stored documents based on user queries.

Summary and Analysis (summary and summaryBIG)
These functions use OpenAI's GPT-3.5 model through the ask function to summarize legal texts, extracting key information, and presenting it in a formatted manner. summaryBIG handles larger texts by breaking them down into smaller chunks for processing.

Configuration
Ensure to provide the necessary API keys and configurations for OpenAI and ChromaDB. Replace placeholders like your_api_key with actual keys in the code.

Contributions
Contributions to enhance features or fix issues are welcome. Fork this repository, make changes, and create a pull request.

License
This project is licensed under the MIT License.