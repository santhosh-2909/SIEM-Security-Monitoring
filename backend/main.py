from flask import Flask, render_template, jsonify
from log_processor import process_security_logs
import os

# Initialize Flask with specific template and static folders for the split architecture
app = Flask(__name__, 
            template_folder="../frontend/templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/dashboard')
def api_dashboard():
    data = process_security_logs()
    return jsonify({
        "stats": data["stats"],
        "top_threats": data["alerts"][:5],
        "health": data["stats"]["health"],
        "trends": data["trends"]
    })

@app.route('/api/alerts')
def api_alerts():
    data = process_security_logs()
    return jsonify(data["alerts"])

@app.route('/api/alerts/<int:alert_id>')
def api_alert_detail(alert_id):
    from log_processor import get_alert_details
    detail = get_alert_details(alert_id)
    if detail:
        return jsonify(detail)
    return jsonify({"error": "Alert not found"}), 404

@app.route('/api/logs')
def api_logs():
    data = process_security_logs()
    return jsonify(data["logs"])

@app.route('/api/assets')
def api_assets():
    data = process_security_logs()
    return jsonify(data["assets"])

@app.route('/api/reports')
def api_reports():
    data = process_security_logs()
    return jsonify(data["report"])

if __name__ == '__main__':
    print("--- SOC SENTINEL BACKEND ---")
    print("API Layer: http://localhost:5000/api/threats")
    print("UI Layer:  http://localhost:5000/")
    app.run(debug=True, port=5000)
