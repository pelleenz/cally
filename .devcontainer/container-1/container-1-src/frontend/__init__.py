from flask import Flask

global signinstatus
signinstatus = False

def create_app():
  app = Flask(__name__)
  return app
