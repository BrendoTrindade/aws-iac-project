from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/')
def hello():
    return jsonify({
        'environment': 'development',
        'message': 'Hello from DevOps Project!'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
