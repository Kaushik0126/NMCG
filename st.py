import speech_recognition as sr
import pyttsx3
def speech():

    r = sr.Recognizer() 

    # Function to convert text to
    # speech
    def SpeakText(command):
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
        
        
    # Loop infinitely for user to
    # speak

    while(1): 
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2,duration=0.1)
                
                #listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                # print("Did you say ",MyText)
                SpeakText(MyText)
                # print(type(MyText))
                return MyText     
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)
            
        except sr.UnknownValueError:
            return "voice not recognized / There is an ambient noise."
# print(speech())