from flask import Flask
from app.routes import main
from app.models import db

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprint
app.register_blueprint(main, url_prefix='/api')


@app.route('/')
def home():
    return {'message': 'Welcome to the Library Management System'}

if __name__ == '__main__':
    app.run(debug=True)
