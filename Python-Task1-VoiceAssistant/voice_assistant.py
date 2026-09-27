import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Sorry, there is a problem with the speech recognition service.")
        return ""


def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today's date is " + current_date)

        elif "search" in command:
            topic = command.replace("search", "").strip()

            if topic:
                speak("Searching for " + topic)
                webbrowser.open(
                    "https://www.google.com/search?q=" + topic.replace(" ", "+")
                )
            else:
                speak("Please tell me what you want to search for.")

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command:
            speak("Sorry, I don't understand that command.")


if __name__ == "__main__":
    main()