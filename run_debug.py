""" Import app and run it in test mode
"""
from project import app, db
db.create_all()
app.run(debug=True)
