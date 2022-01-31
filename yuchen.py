#In minutes
TOTAL_TRIP_TIME = 45
WAIT_TIME = 2
TRAVEL_TIME = 3
CHARGED_MINS = 4
#In Cents
BASE_PRICE = 100
CHARGED_RATE = 15

schoolStartsHour = int(input("Please enter the hour when school starts: "))
schoolStartsMinute = int(input("Please enter the minute when school starts: "))
stopNumber = int(input("Please enter your stop number: "))

schoolStart = schoolStartsHour * 60 + schoolStartsMinute

busDepartureTime = schoolStart - TOTAL_TRIP_TIME
travelTime = (stopNumber - 1) * (TRAVEL_TIME + WAIT_TIME)
arrive = busDepartureTime + travelTime
arriveEnd = arrive + WAIT_TIME

arriveStr = str(arrive // 60) + ":" + str(arrive % 60).zfill(2)
arriveEndStr = str(arriveEnd // 60) + ":" + str(arriveEnd % 60).zfill(2)
print("The bus will be at stop number", stopNumber, "between", arriveStr, "and", arriveEndStr)

tripTime = schoolStart - arriveEnd
print("The length of the trip from stop number", stopNumber, "is", tripTime, "minutes")

ticketPrice = (tripTime // CHARGED_MINS) * CHARGED_RATE + BASE_PRICE
ticketPriceStr = "$" + str(ticketPrice // 100) + "." + (str(ticketPrice % 100).zfill(2))
print("The cost of the ticket from stop number", stopNumber, "is", ticketPriceStr)