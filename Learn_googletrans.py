"""
Learning Googletrans Module

This script demonstrates the basic usage of the googletrans module.
"""

# Import necessary modules
from googletrans import Translator
import httpx

def main():
    """
    Main function to demonstrate googletrans usage.
    """
    # Define the headers manually to ensure they are not None
    user_agent = 'my-custom-user-agent'
    service_urls = ['translate.google.com']
    proxies = {'http': 'http://foo.bar:3128'}

    # Set the timeout parameter correctly
    timeout = httpx.Timeout(10.0)  # Timeout can be set as a float for seconds

    # Initialize the Translator
    translator = Translator(service_urls=service_urls, user_agent=user_agent, proxies=proxies, timeout=timeout, raise_exception=True)

    # Translate Text
    translated_text = translator.translate("生日快樂", src="auto", dest="en")
    print(f"Original Text: 生日快樂")
    print(f"Translated Text: {translated_text.text} (Happy Birthday)")

    # Detect Language
    detected = translator.detect("Baiklah kawan")
    print(f"Detected Language: {detected.lang} (Malay)")

    # Example of handling errors
    try:
        translated = translator.translate("Saya kebebasan", src="auto", dest="en")
        print(f"Translated Text: {translated.text} (I'm freedom)")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

"""
Translated Object:
    When you call the translate method, it returns a Translated object which contains the following attributes:
        src (string): The source language detected or specified.
        dest (string): The destination language.
        origin (string): The original text.
        text (string): The translated text.
        pronunciation (string): Pronunciation of the translated text (if available).

Detected Object:
    When you call the detect method, it returns a Detected object which contains the following attributes:
        lang (string): The detected language code.
        confidence (float): Confidence of the detection.
"""