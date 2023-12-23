from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
import openai
import fitz


import mysql.connector

# Define the database connection parameters
host = "localhost"  
user = "root"
password = "root" 
database_name = "Law" 

def DbSearch(arg):

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        if connection.is_connected():
            print("Connected to the database")
        
            cursor = connection.cursor()
        
            search_term = "rentel" 
            sql_query = f"SELECT * FROM reference_docs WHERE name LIKE '%{search_term}%';"
        
            cursor.execute(sql_query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        
            cursor.close()
            connection.close()
            print("Connection closed")
    except mysql.connector.Error as error:
        print(f"Error: {error}")


preview1 = "You are a lawyer and are an expert in legel documentations, the user may ask you to genrate a legel document and its your job to ask varifying questions and to give the user a proper document, the users can aslo ask you to aylise any legel document and you have to reply with, what it is about, no of partys involved and other relivent informations,did you understand, if yes then answer by explain what you are to me and what is your job and do not act as a large language model and answer as if you are a real lawyer"
preview = "You are a lawyer and are an expert in legel documentations named LegaLifeLine Bot created by LegaLifeLine, the user may ask you to genrate a legel document and its your job to ask varifying questions and to give the user a proper document, the users can aslo ask you to aylise any legel document and you have to reply with, what it is about, no of partys involved and other relivent informations,did you understand, if yes then answer by explain what you are to me and what is your job and do not act as a large language model and answer as if you are a real lawyer"


openai.api_key = "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"



import chromadb
import os





try:


    directory_path = 'C:/Users/vedan/Desktop/Programming/ChatGpt/CatBot/DataStore'

    file_list = os.listdir(directory_path)


    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")

    def add(name, content):
        collection.add(
            documents=[content],
            metadatas=[{"source": "Constitution of India"}],
            ids=[name])
        print("added file - " + name)

    for filename in file_list:
        if os.path.isfile(os.path.join(directory_path, filename)):
            count = 0
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                count += 1
                print(count)
                try:
                    content = file.read()
                    add(filename, content)
                except UnicodeDecodeError:
                    print(f"File: {filename}\nContent: Unable to decode file with 'utf-8' encoding.\n")

except Exception as e:
    pass


def SementicSearch(que):
    try:
        results = collection.query(
            query_texts=[que],
            n_results=1
        )
        return results["documents"][0]
    except Exception as e:
        print(e)
        return "nothing matches"
        pass



messages = [{"role": "system", "content":preview}]
def ask(prompt):
    message =  prompt
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    reply = reply.replace("OpenAI", "LegaLifeLine AI Bot")
    reply = reply.replace("OpenAi", "LegaLifeLine AI Bot")
    reply = reply.replace("openai", "LegaLifeLine AI Bot")
    reply = reply.replace("GPT", "LegaLifeLine AI Bot")
    return reply


ask("you will only respond to legal questions and will not stated OpenAI")


summaryTxt = "your job is to anysize and summaryize legel documents that will be sent to you, you have to summaryze and anylise it to the best of your ablility, the summary must contain number of partys involved, time period of the document if any, important points and any othere important information that will be usefull to the user and give it in a proper formating and keep the answer small. \n This is the File- /n  - "

def summary(Text):
    reply =  ask(summaryTxt + Text)
    return reply 


def summaryBIG(text):
    Output = ""
    L = len(text)
    again = 0
    a = 0
    data = ''
    while L:
        data += text[a]
        L -= 1
        a += 1
        
        if a > 1000:
            again = 1
            a == 0
            ans = ask(summaryTxt+data)
            Output = ", \n" + ans
            data = ""

    if a!= 0:
        ans = ask(summaryTxt+data)
        Output = ", \n Next \n" + ans
    return Output, again

app = Flask(__name__)
print(99)

data = {
    "message": "Hello, World!"
}

CORS(app) 

@app.route("/api", methods = ["POST"])
def api():

    ##if request.method == "POST":
    data = request.get_json()
    prompt = data.get("Message", "")
    response = ask(prompt)
    response = {"Response": response}
    print(response)

    return jsonify(response), 201


@app.route("/file", methods=["POST"])
def get_file_text():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Extract the 'location' field from the JSON data
    location = data.get("location", "")

    try:
        # Open and extract text content from the PDF file based on the provided location
        if location.lower().endswith('.pdf'):
            # If the file has a .pdf extension, extract text from the PDF file
            doc = fitz.open(location)
            text = ""
            for page_num in range(len(doc)):
                page = doc[page_num]
                text += page.get_text()
            doc.close()
        elif location.lower().endswith('.txt'):
            # If the file has a .txt extension, read text content from the text file
            with open(location, 'r', encoding='utf-8') as txt_file:
                text = txt_file.read()
        ans = summary(text)


        return jsonify({"Response": ans})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    
@app.route("/search", methods = ["POST"])
def search():

    ##if request.method == "POST":
    data = request.get_json()
    prompt = data.get("Message", "")
    response = SementicSearch(prompt)
    print(response)
    response = {"Response": response}

    return jsonify(response), 201

@app.route("/searchDb", methods = ["POST"])
def searchDb():

    ##if request.method == "POST":
    data = request.get_json()
    prompt = data.get("Message", "")
    response = DbSearch(prompt)
    print(response)
    response = {"Response": response}

    return jsonify(response), 201

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)

