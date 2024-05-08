"""import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
user_input = input("User : ")
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response_text = model.generate_content(user_input)
print(response_text.text)"""

#---------------------

"""secret_key= secrets.token_hex(16)
app = Flask(__name__)
app.secret_key = secret_key

client = genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/', methods=["GET","POST"])
def index():
    session['conversation'] = []
    return render_template("index.html")


@app.route('/submit', methods=['GET','POST'])
def submit():
    user_input = request.form['text_input']
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(user_input)
    response_text = response.text
    session['conversation'].append({'input': user_input, 'modeloutput': response_text})
    #mongo.db.conversation.insert_one({'input': user_input, 'modeloutput': response_text})
    print(session['conversation'])
    
    return render_template('submit.html', conversation=session['conversation'])

if __name__ == "__main__":
    app.run(debug=True)
    
#Store the conversation to the db """

# this code below works in .py 
'''
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

conversation = []

model = genai.GenerativeModel('gemini-1.0-pro-latest')

while True: 
    user_input = input("Ask your question here: ")
    if user_input.lower() == 'exit': 
        break   
    model_input = user_input
    response = model.generate_content(model_input)
    response_text = response.text
    conversation.append({'input' : model_input, 'modeloutput': response_text})
    print (response_text)


print(conversation)

for item in conversation:
    test_db.get_collection(name='test-user-conversations').insert_one(item)

'''
