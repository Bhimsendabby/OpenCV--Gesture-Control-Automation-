import http.client
import threading

class message(threading.Thread):
    def run(self):
        conn = http.client.HTTPConnection("api.msg91.com")
        conn.request("GET", "/api/sendhttp.php?sender=MSGIND&route=4&mobiles=6239816767&authkey=231367A7r8pgXLE5b706965&encrypt=1&country=91&message=i%20am%20busy%20now%20Dad%20Bhim&unicode=1&afterminutes=&response=json&campaign=bhimsen")

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

