from flask import Flask,render_template,request
from pymongo import MongoClient
app=Flask(__name__)

client=MongoClient('mongodb://localhost:27017/')
db=client['ssss']
collection=db['aa']
@app.route('/')

def jk():
    return render_template('z.html')

@app.route('/submit', methods=['POST'])

def submit():
    if request.method == 'POST':
        user =request.form.get('user')
        password =request.form.get('password')
    
        data={'user':user,'password':password}
        collection.insert_one(data)
    
        return f"congrates {user}  {password}"
if __name__=='__main__':
    app.run(debug=True)