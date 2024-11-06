def mood_response(mood):
    # Dictionary of mood responses
    responses = {
        "happy": "That's wonderful! Keep smiling!",
        "sad": "I'm sorry to hear that. Hope things get better soon!",
        "excited": "That's awesome! What's got you pumped up?",
        "angry": "Take a deep breath. It's okay to feel this way.",
        "tired": "Rest up! A break might be just what you need.",
    }
    
    # Get the response for the mood if available; otherwise, give a generic response
    return responses.get(mood.lower(), "I'm here for you no matter how you're feeling.")

