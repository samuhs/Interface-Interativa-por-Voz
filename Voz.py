#from interface import *

import speech_recognition as sr

class Speech:

    def voz (self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
        try:
            #print("You said " + r.recognize_google(audio,language='pt'))
            x= r.recognize_google(audio,language='pt')
            print (x)
            return x
        except sr.UnknownValueError:
            print ("erro 1")
            return "Could not understand audio"
        except sr.RequestError as e:
            print ("erro2")
            return "Could not request results; {0}".format(e)

    def procurar_palavra(self):
         x = self.voz()
         while True:

             if 'banana' in x:
                 return 'banana'
             elif 'maça' in x:
                 return 'maça'

             else:
                 print('palavra nao encontrada , fale dnv!')
                 x=self.voz()



#x= Speech()
#x.procurar_palavra()
