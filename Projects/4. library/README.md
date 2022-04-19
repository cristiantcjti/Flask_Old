## How to run this project

'''
<br>sh<br>
export FLASK_APP=app (To import the Flask CLI)<br>
export FLASK_ENV=Development<br>
export FLASK_DEBUG=True<br>

flask run
'''

## How to run the migrations
'''
<br>sh<br>
flask db init<br>
flask db migrate<br>
flask db upgrade<br>
flask db downgrade(in case you want to drop the DB)<br>
'''