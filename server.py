''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This function returns the emotion detected from the given input string.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        display_text = "Invalid text! Please try again!"
    else:
        display_text_list = [
            "For the given statement, the system response is",
            f"'anger': {response['anger']},",
            f"'disgust': {response['disgust']},",
            f"'fear': {response['fear']},",
            f"'joy': {response['joy']} and",
            f"'sadness': {response['sadness']}.",
            f"The dominant emotion is {response['dominant_emotion']}."
        ]
        display_text = " ".join(x for x in display_text_list)

    return display_text

@app.route("/")
def render_index_page():
    ''' This function renders the homepage.'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
