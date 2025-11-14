from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# OFFLINE Argos Translate
import argostranslate.package
import argostranslate.translate


def index(request):
    return render(request, "index.html")


# ------------------------------
#  OFFLINE TRANSLATION (Argos)
# ------------------------------
def offline_translate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "")
        source = data.get("source", "auto")
        target = data.get("target", "en")

        try:
            installed_languages = argostranslate.translate.get_installed_languages()

            if source == "auto":
                # Only for simple use (best guess)
                source = "en"

            from_lang = next((l for l in installed_languages if l.code == source), None)
            to_lang = next((l for l in installed_languages if l.code == target), None)

            if not from_lang or not to_lang:
                return JsonResponse({"success": False})

            translation = from_lang.get_translation(to_lang).translate(text)

            return JsonResponse({"success": True, "translation": translation})

        except Exception as e:
            return JsonResponse({"success": False})


# ---------------------------------
#  ONLINE TRANSLATION (LibreTranslate)
# ---------------------------------
def online_translate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "")
        source = data.get("source", "auto")
        target = data.get("target", "en")

        try:
            payload = {
                "q": text,
                "source": source,
                "target": target,
                "format": "text"
            }

            r = requests.post("https://libretranslate.de/translate", data=payload)
            translated = r.json().get("translatedText", "")

            return JsonResponse({"success": True, "translation": translated})

        except:
            return JsonResponse({"success": False})
