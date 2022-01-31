
school_starts_hour= eval(input("Please enter the hour when school starts: "))

school_starts_minute= eval(input("Please enter the minute when school starts: "))

school_starts_at_total_minute= school_starts_hour*60+school_starts_minute

print("The school starts time is ", school_starts_hour,":",
   "school_starts_at_total_minute")

stop_number= eval(input("Please enter your stop number: "))

TOTAL_TRIP_TIME=45
bus_departure_time=school_starts_at_total_minute-TOTAL_TRIP_TIME

arrival_time_for_stop={bus_departure_time+(stop_number-1)*(2+3)}-2

departure_time_for_stop=arrival_time_for_stop+2

#stitch the time from minutes to hours

Print("The bus will be at stop number", stop_number,"between",
      arrival_time_for_stop//60,":","arrival_time_for_stop%60",
      "and", departure_time_for_stop//60,":","departure_time_for_stop%60")

#The length of the trip from stop to school
The_length_of_the_trip= {TOTAL_TRIP_TIME-(stop_number-1)*(2+3)}-2
print("The length of the trip from stop to school is ",
      The_length_of_the_trip,"minutes")

#The cost of the ticket from stop
cost_of_ticket=(The_length_of_the_trip)//(stop_number-1)*15+100

#switch the cents to dollars
print("The cost of the ticket from ",stop_number,'is $',
      cost_of_ticket//100,","cost_of_ticket%100)

