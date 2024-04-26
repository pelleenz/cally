import time
from frontend import create_app
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from os import path
from werkzeug.security import generate_password_hash, check_password_hash




def frontend():
   
  app = create_app()
  
  @app.route('/')
  def home():
    return "HELLO"
  
  
  
  app.run(debug=True)
