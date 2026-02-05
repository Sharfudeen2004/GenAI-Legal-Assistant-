from langdetect import detect, detect_langs, LangDetectException

def detect_language(text):
    try:
        lang = detect(text)
        return lang   # example: 'en', 'hi', 'ta', 'fr'
    except LangDetectException:
        return "unknown"

def detect_language_with_confidence(text):
    try:
        langs = detect_langs(text)
        return [(str(l.lang), round(l.prob, 2)) for l in langs]
    except LangDetectException:
        return [("unknown", 0.0)]
