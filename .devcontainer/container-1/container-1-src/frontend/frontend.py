import asyncio
from frontend import create_app
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from os import path
from werkzeug.security import generate_password_hash, check_password_hash

async def frontend():
  
  app = create_app()
  app.run(debug=True)
    
  while True:
    print("frontend")
    await asyncio.sleep(10)

async def main():
  t1 = asyncio.create_task(frontend())
  await asyncio.gather(t1)
    
if __name__ == "__main__":
  asyncio.run(main())