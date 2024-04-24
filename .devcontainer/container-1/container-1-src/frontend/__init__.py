import asyncio
import os
from os import path
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

global signinstatus
signinstatus = False

db = SQLAlchemy()
DB_NAME = "cally-main.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)
  
  create_database(app)
  
  return app
  
def create_database(app):
  if not path.exists("./instance/" + DB_NAME):
    print("no DB")
    with app.app_context():
      db.create_all()
    print("Created database!")
  else:
    print("db exists")