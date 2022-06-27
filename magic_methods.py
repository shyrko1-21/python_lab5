class Airline:
    __plainType = "Boeing"
    daysOfWeek = []

    def __init__(self, destination, flightNumber, departureTime, daysOfWeek):
        self.destination = destination
        self.flightNumber = flightNumber
        self.departureTime = departureTime
        self.daysOfWeek = daysOfWeek

    # методы класса
    def getPlainType(self):
        return self.__plainType

    def setDestination(self, destination):
        self.destination = destination

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def setPlainType(self, plainType):
        self.__plainType = plainType

    def setDepartureTime(self, departureTime):
        self.departureTime = departureTime

    def setDaysOfWeek(self, daysOfWeek):
        self.daysOfWeek = daysOfWeek

    # статический метод
    @staticmethod
    def getAirlineName():
        return "Etihad"

    # метод класса
    @classmethod
    def ibizaFlight(cls, flightNumber, departureTime, daysOfWeek):
        ibizaFlight = cls("Ibiza", flightNumber, departureTime, daysOfWeek)
        return ibizaFlight

    def __str__(self):
        return f"Пункт назначения: {self.destination}, Номер рейса: {self.flightNumber}, Тип самолета: {self.__plainType}," \
               f"Время вылета: {self.departureTime}, Дни недели: {self.daysOfWeek}"

    def __add__(self, dayOfWeek):
        if dayOfWeek not in self.daysOfWeek:
            self.daysOfWeek.append(dayOfWeek)

    def __eq__(self, flight):
        if self.destination == flight.destination:
            return True
        return False

    def __getattr__(self, item):
        if item == "country":
            if self.destination == "Madrid":
                print("Spain")
            elif self.destination == "London":
                print("Great Britain")
            elif self.destination == "Amsterdam":
                print("Netherlands")

    def __delattr__(self, item):
        if item == "destination":
            print("Нет прав на удаление атрибута")

madridFlight = Airline("Madrid", "B1423", "10:00", ["Monday", "Tuesday"])
londonFlight =  Airline("London", "A1234", "09:00", ["Saturday"])
amsterdamFlight1 = Airline("Amsterdam", "B4543", "11:00", ["Monday", "Friday", "Sunday"])
amsterdamFlight2 = Airline("Amsterdam", "B4500", "08:00", ["Monday"])
airlineList = list()
airlineList.append(madridFlight)
airlineList.append(londonFlight)
airlineList.append(amsterdamFlight1)
airlineList.append(amsterdamFlight2)

print(madridFlight)
madridFlight.__add__("Sunday")
print(madridFlight)
print(madridFlight.__eq__(londonFlight))
madridFlight.__getattr__("country")
madridFlight.__delattr__("destination")