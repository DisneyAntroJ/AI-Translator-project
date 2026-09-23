from googletrans import Translator

translator = Translator()

def translate_text(text, language):
    translated = translator.translate(text, dest=language)
    return translated.text