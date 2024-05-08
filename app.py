from flask import Flask, request, jsonify,render_template, session
from dotenv import load_dotenv , find_dotenv
import google.generativeai as genai
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os, secrets, json
from flask import session

load_dotenv()
secret_key = secrets.token_hex(16)
db_password = os.getenv("MONGO_PWD")

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://testUser:{db_password}@cluster-prof-web-db.8v2lgup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-prof-web-db"
mongo_client = MongoClient(app.config["MONGO_URI"])
dbs = mongo_client.list_database_names()
test_db = mongo_client["rocket-app"] #accessing the database
collection = test_db.list_collection_names()   #list collections inside the database

client = genai.configure(api_key=os.environ["GEMINI_API_KEY"])

CONVERSATION_THREAD = []


model = genai.GenerativeModel('gemini-1.0-pro-latest')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        user_input = request.form.get('user_input')
        model_input = user_input
        response = model.generate_content(model_input)
        response_text = response.text
        new_item = {'input' : model_input, 'modeloutput': response_text}
        CONVERSATION_THREAD.append(new_item)
        test_db.get_collection(name='test-user-conversations').update_one(new_item, {'$set': new_item}, upsert=True)
        return render_template('index.html', conversation = CONVERSATION_THREAD)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)