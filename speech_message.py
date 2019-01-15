import speech_recognition as sr
import http.client
import threading
import speech_number

class speech_message(threading.Thread):
    def run(self):
        reco = sr.Recognizer()
        with sr.Microphone() as source:
            print("tell me message sir")
            audio = reco.listen(source)

            try:
                text = reco.recognize_google(audio)
                print("you said {}".format(text))
            except:
                print("sorry")
        msg = ""
        words = text.split(" ")
        for i in range(0,len(words)):
             msg = msg + words[i] +"%20"

        person = speech_number.speech_number.call_speech_number()

        if person == "DAD"or"dad"or"Dad":
            number = 6239816767
            print("message send to dad")
        elif person == "MOM"or"mom"or"Mom":
            number = 7888417191
            print("message send to mom")
        elif person == "BROTHER"or"Brother"or"brother":
            number = 8591358556
            print("message send to dad")
        elif person == "UNCLE"or"Uncle"or"uncle":
            number = 7814777243
            print("message send to Uncle")
        else:
            print("wrong input")

        api = "/api/sendhttp.php?sender=MSGIND&route=4&mobiles={}&authkey=231367A7r8pgXLE5b706965&encrypt=1&country=91&message={}&unicode=1&afterminutes=&response=json&campaign=bhimsen".format(number,msg)
        print(api)
        conn = http.client.HTTPConnection("api.msg91.com")
        conn.request("GET", api)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))