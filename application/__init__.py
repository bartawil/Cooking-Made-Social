from flask import Flask
from flask_session import Session
import mysql.connector
from application.forms import CreateRecipeForm, FindRecipeForm

workshop_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='database_workshop'
)

workshop_cursor = workshop_db.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = '2136cdc56a8ad364b251f9bb645d1e56' # Create S.K. for anti csrf attack
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

from application import routs
