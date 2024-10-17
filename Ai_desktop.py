import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def wish_me():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")
    speak("I am Aegis, your personal assistant. How can I assist you today ?")


def take_command():
    """Listen for user commands and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        speak("I didn't catch that. Could you please repeat?")
        return "None"
    
    except sr.RequestError:
        speak("Sorry, my speech service is down. Please try again later.")
        return "None"

    return query.lower()

def main():
    """Main function to handle user commands."""
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("Multiple results found, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on Wikipedia for your query.")
        

        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open('https://www.youtube.com')



        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open('https://www.google.com')



        elif 'open w3 schools' in query:
            speak("Opening W3Schools.")
            webbrowser.open('https://www.w3schools.com')



        elif 'play music' in query:
            music_dir = 'D:\\Movies\\Punjabi Song'
            try:
                songs = os.listdir(music_dir)
                if songs:
                    speak(f"Playing {songs[0]}")
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the directory.")
            except FileNotFoundError:
                speak("Sorry, I couldn't find the music directory.")


        
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
            print(str_time)



        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            try:
                speak("Opening Chrome.")
                os.startfile(chrome_path)
            except FileNotFoundError:
                speak("Chrome is not installed on your system.")

                

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I'm sorry, I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
