from dotenv import load_dotenv
import os
import joblib

load_dotenv(override=True)


# Load variables from .env file
APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# src folder path
SRC_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

# Artifacts folder path
ARTIFACTS_FOLDER_PATH = os.path.join(SRC_FOLDER_PATH, "artifacts")

# models
bow_vectorizer = joblib.load(os.path.join(ARTIFACTS_FOLDER_PATH, "bow_vectorizer.pkl"))
svm_model = joblib.load(os.path.join(ARTIFACTS_FOLDER_PATH, "svm_bow.pkl"))

# Some constants
EMOTIOCS_MEANINGS = {
    ":)": "Happy",
    ":(": "Sad",
    ":D": "Very Happy",
    ":|": "Neutral",
    ":O": "Surprised",
    "<3": "Love",
    ";)": "Wink",
    ":P": "Playful",
    ":/": "Confused",
    ":*": "Kiss",
    ":')": "Touched",
    "XD": "Laughing",
    ":3": "Cute",
    ">:(": "Angry",
    ":-O": "Shocked",
    ":|]": "Robot",
    ":>": "Sly",
    "^_^": "Happy",
    "O_o": "Confused",
    ":-|": "Straight Face",
    ":X": "Silent",
    "B-)": "Cool",
    "<(‘.'<)": "Dance",
    "(-_-)": "Bored",
    "(>_<)": "Upset",
    "(¬‿¬)": "Sarcastic",
    "(o_o)": "Surprised",
    "(o.O)": "Shocked",
    ":0": "Shocked",
    ":*(": "Crying",
    ":v": "Pac-Man",
    "(^_^)v": "Double Victory",
    ":-D": "Big Grin",
    ":-*": "Blowing a Kiss",
    ":^)": "Nosey",
    ":-((": "Very Sad",
    ":-(": "Frowning",
}

# The mapping for the prediction
SENTIMENT_MAPPING = {
            0: "Negative",
            1: "Positive",
            2: "Neutral"
        }