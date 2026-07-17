from flask import Flask, render_template
import os

# Initialize the Flask application
application = Flask(__name__, template_folder='.')

@application.route('/')
def home():
    # Serves the index.html file to the visitor
    return render_template('index.html')

if __name__ == '__main__':
    # Binds the application to port 80 to make it publicly accessible on your VM
    port = int(os.environ.get('PORT', 80))
    application.run(host='0.0.0.0', port=port)
