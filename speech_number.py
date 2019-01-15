import speech_recognition as sr1

class speech_number():
    @classmethod
    def call_speech_number(cls):
        recog = sr1.Recognizer()
        with sr1.Microphone() as source1:
            print("tell me the person to send this message to")
            print("DAD")
            print("MOM")
            print("BROTHER")
            print("UNCLE")

            audio1 = recog.listen(source1)

            try:
                person = recog.recognize_google(audio1)
                print("you said {}".format(person))
            except:
                print("sorry")

        return person