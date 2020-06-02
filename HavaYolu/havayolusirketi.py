from datetime import datetime
from random import randint


class city:
    def  __init__(self, name):
        self.__name = name;
        self.__weather = randint(18,25)
        self.__havaDurumu = ["Sunny","Rainy","Cloudy","Snowy"][randint(0,3)]

    def getName(self):
        return self.__name

    def getWeather(self):
        return self.__weather

    def getHavaDurumu(self):
        return self.__havaDurumu

    def setWeather(self,weather:int):
        self.__weather = weather

    def setHavaDurumu(self,havaDurumu:int):
        if durum not in ["Sunny","Rainy","Cloudy","Snowy"]:
            pass
        else:
            self.__havaDurumu = havaDurumu

    def __str__(self):
        return self.__name

class Flight:
    def __init__(self,where:city,departure:city,date:datetime):
        self.__date = date
        self.__where = where
        self.__departure = departure

    def delay(self, howMuch:int):
        day = self.__date.day
        hour = self.__date.hour
        minutes = self.__date.minutes

        if(minutes + howMuch) >= 60:
            hour += int((minutes + howMuch) / 60)
            minutes = (howMuch + minutes) % 60

            if hour >=24:
                day += int(hour / 24)
                hour = hour % 24

        newdate = datetime(self.__date.year,self.__date.month,day,hour,minutes)
        self.__date = newdate

    def getdate(self):
        return self.__date

    def where(self):
        return self.__where

    def departure(self):
        return  self.__departure

class Passenger:
    def __init__(self, name:str, surname:str , tcno:int):
        self.__name = name
        self.__surname = surname
        self.__tcno = tcno

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getTC(self):
        return self.__tcno

class Ticket:
    def __init__(self,passenger:Passenger,flight:Flight,seatNo:str):
        self.__passenger= passenger
        self.__flight = flight
        self.__seatNo = seatNo

    def seatNo(self):
        return self.__seatNo

    def __str__(self):
        string = """
        Name:{}
        Surname:{}
        Tc:{}
        Flight Date:{}
        Flight Time:{}
        Where: {}         Weather:{}    C={}
        Departure:{}      Weather:{}    C={}
        Seat No:{}
        """.format(self.__passenger.getName(),self.__passenger.getSurname(),self.__passenger.getTC(),self.__flight.getdate(),self.__flight.getdate().time(),self.__flight.where().getName(),self.__flight.where().getHavaDurumu(),self.__flight.where().getWeather(),self.__flight.departure().getName(),self.__flight.where().getHavaDurumu(),self.__flight.where().getWeather(),self.seatNo())

        return string

    def getFlight(self):
        return self.__flight

class THY:
    def __init__(self):
        self.__activeTickets = list()
        self.__oldTickets = list()
        self.__activeflights = list()
        self.__doneFlights = list()

    def TakeTicket(self , passenger:Passenger , flight:Flight , seatNo):
        if flight in self.__activeflights:
            ticket = Ticket(passenger , flight , seatNo)
            self.__activeTickets.append(ticket)
            return ticket

    def createFlight(self, where:city , departure:city , date:datetime):
        flight = Flight(where,departure,date)
        self.__activeflights.append(flight)
        return flight

    def cancelTicket(self , ticket:Ticket):
        if ticket in self.__activeTickets:
            self.__activeTickets.remove(ticket)
            print("Ticket has been cancelled!!")

    def doneFlights(self , flight:Flight):
        for ticket in self.__activeTickets:
            if ticket.getFlight() == flight:
                self.__activeTickets.remove(ticket)
                self.__oldTickets.append(ticket)
        self.__activeflights.remove(flight)
        self.__doneFlights.append(flight)

    def delay(self , flight:Flight , minute:int):
        flight.delay(minute)


def Main():
    s = """01 Adana
02 Adıyaman
03 Afyon
04 Ağrı
05 Amasya
06 Ankara
07 Antalya
08 Artvin
09 Aydın
10 Balıkesir
11 Bilecik
12 Bingöl
13 Bitlis
14 Bolu
15 Burdur
16 Bursa
17 Çanakkale
18 Çankırı
19 Çorum
20 Denizli
21 Diyarbakır
22 Edirne
23 Elazığ
24 Erzincan
25 Erzurum
26 Eskişehir
27 Gaziantep
28 Giresun
29 Gümüşhane
30 Hakkari
31 Hatay
32 Isparta
33 İçel (Mersin)
34 İstanbul
35 İzmir
36 Kars
37 Kastamonu
38 Kayseri
39 Kırklareli
40 Kırşehir
41 Kocaeli
42 Konya
43 Kütahya
44 Malatya
45 Manisa
46 K.maraş
47 Mardin
48 Muğla
49 Muş
50 Nevşehir
51 Niğde
52 Ordu
53 Rize
54 Sakarya
55 Samsun
56 Siirt
57 Sinop
58 Sivas
59 Tekirdağ
60 Tokat
61 Trabzon
62 Tunceli
63 Şanlıurfa
64 Uşak
65 Van
66 Yozgat
67 Zonguldak
68 Aksaray
69 Bayburt
70 Karaman
71 Kırıkkale
72 Batman
73 Şırnak
74 Bartın
75 Ardahan
76 Iğdır
77 Yalova
78 Karabük
79 Kilis
80 Osmaniye
81 Düzce """
    citys = list()
    for i in s.split("\n"):
        citys.append(city(i))

    omer = Passenger("Omer","EKINCI",12345678901)
    thy = THY()
    flight1 = thy.createFlight(citys[5],citys[12],datetime(2020,5,28,7,40))
    ticket1 = thy.TakeTicket(omer,flight1,"A5")
    print(ticket1)

if __name__ == "__main__":
    Main()


