# Get started: 
### Create Virtual Environment
```
python -m venv myenv                                          
source myenv/bin/activate    
```

### Install dependencies 
` pip install -r requirements.txt`

All server side computation happens in the /app/__init__.py file SO WORK IN /app/__init__.py  NOT THE app.py FILE

### Connect to MongoDB
```
# in the ROOT FOLDER of your project create a file named .env
# just .env to title or anthing but make sure there's a . lol
# your file should have the contents 

MONGO_DB_API_KEY = "yourKeyHere"
```
When you make an account on mongoDB at the end it will give you a link that looks like this "mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority"
That goes in the yourKeyHere slot.

### Run 
```
flask --debug run
#This will reload the server every time you save the __init__.py file
# Access dev server in your browser at http://127.0.0.1:5000/
```
