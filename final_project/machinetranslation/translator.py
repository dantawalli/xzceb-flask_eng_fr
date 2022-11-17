"""
This function returns the sum of the given numbers
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
LANGUANGE_TRANSLATOR = 'null'

def translator_instance():
    """
    This function returns the sum of the given numbers
    """
    authenticator = IAMAuthenticator(apikey)
    LANGUANGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
    LANGUANGE_TRANSLATOR.set_service_url(url)

def english_to_french(english_text):
    """
    This function returns the sum of the given numbers
    """
    french_text = LANGUANGE_TRANSLATOR.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """
    This function returns the sum of the given numbers
    """
    english_text = LANGUANGE_TRANSLATOR.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text
