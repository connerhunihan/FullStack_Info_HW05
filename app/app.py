# Where you configure the app; where the files that run your app are 
# Import other libraries to run on your app; initialization

from flask import Flask

""" 1. Creating a flask application instance, the name argument is passed to flask
application constructor. It's used to determine the root path"""
app = Flask(__name__)

import views