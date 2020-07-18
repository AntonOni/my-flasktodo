#!flask/bin/python
from app import app1, port

app.run(host='0.0.0.0', port=port, use_reloader=True)