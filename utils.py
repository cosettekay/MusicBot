# Utility function to format the chatbot's response (optional)
def format_response(chatbot_response, recommended_tracks):
    response = f"Chatbot says: {chatbot_response}\n"
    response += "Here are some recommended tracks:\n"
    for track in recommended_tracks:
        response += f"- {track}\n"
    return response
