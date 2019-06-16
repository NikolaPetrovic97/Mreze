from tkinter import *
import http.server
from urllib.parse import urlparse, parse_qs
from threading import Thread
from socketserver import ThreadingMixIn

Server = http.server.HTTPServer
BaseHandler = http.server.BaseHTTPRequestHandler

sizeX = 640
sizeY = 480
margin = 20
x1 = margin
y1 = margin
x2 = sizeX - margin
y2 = sizeY - margin
width = sizeX - 2 * margin
height = sizeY - 2 * margin

n = 20
stanje = [[0 for i in range(n)] for i in range(n)]

korisnici = {}


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mreze 2018/2019")
        self.w = Canvas(master, width=sizeX, height=sizeY)

        self.w.pack()
        self.drawLines(self.w)

        self.greet_button = Button(master, text="Reset", command=lambda: self.greet(self.w))
        self.greet_button.pack()

        self.greet_button = Button(master, text="Print", command=lambda: self.printStanje())
        self.greet_button.pack()

    def printStanje(self):
        print("*" * 10 + " TOP LISTA" + "*" * 10)
        for i in korisnici:
            x = 0
            for j in stanje:
                x += j.count(korisnici[i][1])
            print(str(korisnici[i][1]) + ") " + str(i) + ": " + str(korisnici[i][0]) + " -> " + str(x))
        print("*" * 30)

    def greet(self, w):
        global stanje
        global korisnici
        stanje = [[0 for i in range(n)] for i in range(n)]
        korisnici = {}
        self.reDraw(w)

    def drawRect(self, x, y, color, ime, w):
        left = x * width // n + margin
        top = y * height // n + margin
        w.create_rectangle(left, top, left + width // n, top + height // n, fill=color, width=0)
        w.create_text(left + (width // n) // 2, top + (height // n) // 2, fill="black", font="Times 10 italic bold", text=ime)

    def reDraw(self, w):
        for i in range(len(stanje)):
            for j in range(len(stanje[i])):
                if (stanje[i][j] != 0):
                    self.drawRect(i, j, "#DDD", "", w)
                else:
                    self.drawRect(i, j, "#DDD", "", w)
        self.drawLines(w)

    def drawLines(self, w):
        for i in range(n + 1):
            for j in range(n + 1):
                w.create_line(margin + i * width // n, y1, margin + i * width // n, sizeY - margin, fill="#FFFFFF")
                w.create_line(x1, y1 + j * height // n, x2, y1 + j * height // n, fill="#FFFFFF")

    def setData(self, x, y, boja, ime, w):
        global korisnici
        global stanje

        if (stanje[x][y] == 0):
            if (ime not in korisnici):
                id = len(korisnici) + 1
                korisnici[ime] = [boja, id]
            else:
                id = korisnici[ime][1]
            stanje[x][y] = id
            self.drawRect(x, y, boja, str(id), w)
            return True
        return False


class S(BaseHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        p = parse_qs(urlparse(self.path).query)
        if (len(p) == 0):
            self.wfile.write(str.encode(
                "<html><body><h1>Dobro dosli!</h1><h3>Molim vas da unesete odgovarajuce parametre!</3></body></html>"))
        elif ("ime" in p and "boja" in p and "x" in p and "y" in p):
            try:
                x = int(p["x"][0])
                y = int(p["y"][0])
                if (my_gui.setData(x, y, "#" + p["boja"][0], p["ime"][0], my_gui.w)):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(str.encode(
                        "<html><body><h1>Dobro dosli!</h1><h3>Odlicno! Popunili ste polje: " + str(x) + ", " + str(
                            y) + "</3></body></html>"))
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(str.encode(
                        "<html><body><h1>Dobro dosli!</h1><h3>Polje je zauzeto! <b>Zao mi je!</b></3></body></html>"))
            except Exception as e:
                print(e)
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str.encode("Page not found. (404)"))
                self.wfile.write(str.encode("<html><body><h1>Dobro dosli!</h1><h3>Super!</3></body></html>"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str.encode("Page not found. (404)"))

    """def do_GET(self):
        global my_gui
        my_gui.reDraw(my_gui.w)
        self._set_headers()
        self.wfile.write(str.encode("<html><body><h1>hi!</h1></body></html>"))"""

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(str.encode("<html><body><h1>POST!</h1></body></html>"))

class ThreadedHTTPServer(ThreadingMixIn, Server):
    """Handle requests in a separate thread."""

def run():
    server_address = ('192.168.81.10', 80)
    httpd = ThreadedHTTPServer(server_address, S)

    print('Starting httpd...')

    thread = Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()


root = Tk()
my_gui = MyFirstGUI(root)

run()

root.mainloop()