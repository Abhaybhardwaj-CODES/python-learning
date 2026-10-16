import speech_recognition as sr
import webbrowser
import pyttsx3
recoginizer = sr.Recognizer()
engine = pyttsx3.init()

 
          

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
     if 'open google' in c.lower() :
          webbrowser.open("https://google.com") 
          
     elif 'open chrome' in c.lower() :
          webbrowser.open("https://googlechrome.com") 
          
     elif 'open instagram' or "open insta" in c.lower() :
          webbrowser.open("https://instagram.com") 
     elif 'open youtube' in c.lower():
          webbrowser.open("https://youtube.com")
     else:
         speak("sorry sir i can not preform the given list its not in my program")      
          

          
    
     

if  __name__ =="__main__":
      speak("Initializing friday....")
while True:

     r=sr.Recognizer()


     print("Recoginizing....")
     try:
      with sr.Microphone() as source:
          print("listening......")
          audio = r.listen(source)  
          word = r.recognize_google(audio)
          if "friday" in word.lower():
                speak("Yes")

          with sr.Microphone() as source:
               print("friday is awake")
               audio = r.listen(source) 
               command = r.recognize_google(audio)

               processcommand(command)
         


     except sr.UnknownValueError:
          print("I can not understand the words that are coming out of your mouth")
     except sr.RequestError as e:
          print("OONA error: {0}".format(e))     

      