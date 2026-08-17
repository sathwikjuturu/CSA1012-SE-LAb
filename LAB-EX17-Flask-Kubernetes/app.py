from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Flask API is running successfully!"
    })

@app.route('/hello')
def hello():
    return jsonify({
        "message": "Hello from LAB EX17!"
    })

@app.route('/about')
def about():
    return jsonify({
        "project": "Simple Flask API",
        "technology": "Python Flask",
        "deployment": "Docker and Kubernetes"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)