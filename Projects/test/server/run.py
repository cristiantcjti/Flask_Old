import os
from app import create_app

app = create_app(os.path.abspath('settings.py'))
app.run(debug=True, use_reloader=True)

