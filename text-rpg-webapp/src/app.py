from flask import Flask, render_template
from routes import main_routes

app = Flask(__name__)

# Register the main routes
app.register_blueprint(main_routes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)