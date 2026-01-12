"""
AIM Flask Backend
-----------------
Main Flask application to process messages, log interactions,
and provide real-time status updates for the AIM project.
"""

from flask import Flask, request, jsonify
from datetime import datetime
from Process_Conversation import process_text
from json_converter import log_conversation
import threading
import requests
import time

app = Flask(__name__)

# --- ROUTES ---

@app.route('/process', methods=['POST'])
def process_conversation():
    """Handle incoming messages from the frontend (Tampermonkey script)."""
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    # Process the message
    ai_response = process_text(user_input)

    # Log the conversation
    log_conversation(user_input, ai_response)

    return jsonify({
        "response": ai_response,
        "timestamp": datetime.now().isoformat()
    })


@app.route('/ping', methods=['GET'])
def ping():
    """Simple route to confirm Flask server is alive."""
    return jsonify({
        "status": "online",
        "time": datetime.now().isoformat()
    }), 200


# --- HEARTBEAT MONITOR (Optional) ---
def heartbeat():
    """Ping the Flask server every 30 seconds to verify connection."""
    while True:
        try:
            res = requests.get("http://127.0.0.1:5005/ping", timeout=5)
            if res.ok:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Flask active")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️ Flask returned non-OK")
        except requests.exceptions.RequestException:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Flask unreachable")
        time.sleep(30)


# --- MAIN ENTRY POINT ---
if __name__ == '__main__':
    # Start heartbeat monitor thread (non-blocking)
    threading.Thread(target=heartbeat, daemon=True).start()

    # Run Flask app on port 5005
    app.run(host='127.0.0.1', port=5005, debug=True)
