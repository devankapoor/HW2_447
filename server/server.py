from flask import Flask
from flask import request
import sqlite3


app = Flask(__name__)

@app.route('/')
def root():
    # Connect to db
    db = sqlite3.connect('students.db')
    cursor = db.cursor()

    # cursor.execute('INSERT INTO students(Name, Identify, Points) VALUES("Name", "Identify", "Points")')
    # db.commit()

    # Get data from db
    cursor.execute('SELECT * FROM students')
    data = cursor.fetchall()
    
    # Close db connection
    #db.close()
    
    #return {"members": ["Member1", "Member2", "Member3"]}
    return str(data)

@app.route('/create/')
def create():
    # Connect to db
    db = sqlite3.connect('students.db')  
    cursor = db.cursor()
    
    # Get request args
    Name = request.args.get('Name')
    Identify = request.args.get('Identify')
    Points = request.args.get('Points')
    
    # Insert data into db
    #cursor.execute('INSERT INTO students(Name, Identify, Points) VALUES("%s", "%s", "%s")' % (Name, Identify, Points))
    #db.commit()

    cursor.execute('INSERT INTO students(Name, Identify, Points) VALUES("Name", "Identify", "Points")')
    db.commit()
    
    # Close db connection
    db.close()
    #return 'create'
    return 'Name: %s  |  Identify: %s  |  Points: %s' % (Name, Identify, Points)

@app.route('/update/<_id>')
def update(_id):
    # Connect to db
    db = sqlite3.connect('students.db')  
    cursor = db.cursor()
    
    # Get request args
    Name = request.args.get('Name')
    Identify = request.args.get('Identify')
    Points = request.args.get('Points')
    
    # Update data in db
    cursor.execute('UPDATE students SET Name="%s", Identify="%s", Points="%s" WHERE id=%s' % (Name, Identify, Points, _id))
    db.commit()
    
    # Close db connection
    db.close()
    return '_id: %s  |  Name: %s  |  Identify: %s  |  Points: %s' % (_id, Name, Identify, Points)

@app.route('/delete/<_id>')
def delete(_id):
    # Connect to db
    db = sqlite3.connect('students.db')  
    cursor = db.cursor()
    
    # Update data in db
    cursor.execute('DELETE FROM students WHERE id=%s' % _id)
    db.commit()
    
    # Close db connection
    db.close()
    return 'deleted _id: %s' % _id

    #cursor.execute('CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT, Identify TEXT, Points TEXT)')

    # # Get data from db
    # cursor.execute('SELECT * FROM posts')
    # data = cursor.fetchall()

    #     # Close db connection
    # db.close()
    
    #return str(data)

    #return 'root'


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
