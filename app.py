from flask import Flask, request, jsonify, send_from_directory
from gpt2_model import generate_response
from music_api import get_music_recommendation

# Initialize Flask app
app = Flask(__name__, static_folder = 'static', static_url_path='')

# Flask route to handle user messages
@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # Generate GPT-2 chatbot response
    gpt2_response = generate_response(user_input)
    
    # Get a music recommendation based on user inputs
    recommended_tracks = get_music_recommendation(user_input)
    
    # Combine GPT-2 response with music recommendations
    response = {
        "chatbot_response": gpt2_response,
        "recommended_tracks": recommended_tracks
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
