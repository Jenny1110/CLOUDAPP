from flask import Flask, render_template, jsonify
import time

app = Flask(__name__, template_folder='.')

# Captures boot timestamp to monitor uptime calculations
DEPLOY_TIME = time.time()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health():
    """Endpoint for monitoring tool polling."""
    current_uptime = int(time.time() - DEPLOY_TIME)
    return jsonify({
        "status": "HEALTHY",
        "system_uptime_seconds": current_uptime,
        "database_connectivity": "CONNECTED",
        "error_count": 0
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
