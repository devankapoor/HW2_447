# HW2_447

Below is a brief direction on the steps I took:

SERVER side (see server folder)

1. I created a file called server.py which accesses is a database called students.db which I created using SQLlite commands.
2. The SQLite database called students.db contains a table called 'students' with data of id, name, and points
3. I did ">> flask run" and reloaded 8 times or so to populate the database.
4. The server.py contains various "routes" (including root route) to create, update, delete (CRUD)

server.py works well and creates the data in a json like format.

CLIENT side (see client folder)

5. Next, on the client side I ran react using "<< npm start" command
6. I modified "package.json" file to change the proxy to the local server
7. I then modified the "App.js" file to mount to the server and retrieve the data in json format
8. The data is retrieved in displayed using html format 

To run the code:
1. make sure you have students.db in the same folder as the server.py file then do ">>python server.py"
2. note: if you then visit "local host/delete/<id#>" then that data is removed, same for "add", etc.
3. move to the client side folder and start react by typing "npm start"
