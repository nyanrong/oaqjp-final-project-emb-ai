import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze} }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    if (response.status_code ==  400):
        response_json = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_dict, key=lambda k: emotion_dict.get(k))
        response_json = {
            "anger": emotion_dict["anger"],
            "disgust": emotion_dict["disgust"],
            "fear": emotion_dict["fear"],
            "joy": emotion_dict["joy"],
            "sadness": emotion_dict["sadness"],
            "dominant_emotion": dominant_emotion
        }
    return response_json


    