
openai.api_key = API_KEY

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)


conversation = ""
user_name = "Shreyash"