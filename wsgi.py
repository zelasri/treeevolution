""" Module for WSGI run of Flask app
"""
from web.app import app

if __name__ == '__main__':
    app.run()