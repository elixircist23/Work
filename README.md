# Work

ELI's work

1. Set up MySQL server (and sqlite)
2. Create a database
3. Create a table within the database
4. Create a python database utility that lets you 'talk' to the database (SELECT, INSERT, UPDATE, etc)
5. Create a small client that makes use of the python database utility
	./client.py --insert -columna='BLAH' columnb='FOO'	(insert row with the given params)
	./client.py --delete -columna='BLAH'  				(delete row where columna='BLAH')

Now that you have a working backend, build a frontend

1. Create a small python webserver (use tornado)
2. Create endpoints that will call your database utility 
3. Simply present those results. Without any CSS/HTML the browser will display just text

4. Finally use HTML/JavaScript/CSS to make your results look pretty. Use AngularJS!
