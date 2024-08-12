from flask import Flask, request, send_file  # Import Flask and necessary modules
from flask_restful import Api  # Import Flask-RESTful for creating REST APIs
from flask_cors import CORS  # Import Flask-CORS for handling Cross-Origin Resource Sharing
from flask_caching import Cache  # Import Flask-Caching for caching support
from flask_jwt_extended import JWTManager  # Import Flask-JWT-Extended for JWT authentication

from application.config import Configuration as Config  # Import configuration settings
from application.data.database import db  # Import database instance

# Initialize Flask application
app = Flask(__name__)

# Load configuration settings from the Configuration class
app.config.from_object(Config)

# Initialize Flask-RESTful API
api = Api(app)

# Initialize Flask-Caching
# cache = Cache(app)

# Initialize Flask-JWT-Extended for JWT support
jwt = JWTManager(app)

# Initialize database with the Flask app context
db.init_app(app)
app.app_context().push()

# Enable CORS (Cross-Origin Resource Sharing) for all routes
CORS(app, resources={r'/*': {'origins': '*'}})

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8083)  # Run the app in debug mode on port 8083
