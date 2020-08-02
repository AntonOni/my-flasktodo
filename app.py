#!flask/bin/python
from app import app, port

app.run(host='0.0.0.0', port=port, use_reloader=True)
