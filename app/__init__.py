"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cglqakpmbg56g40033qg-a.oregon-postgres.render.com",
        database="campus_workshop",
        user="campus_workshop_user",
        password="diXZ1zqhgrz4WLmyixA6M7q8FWUzUO9Q")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
