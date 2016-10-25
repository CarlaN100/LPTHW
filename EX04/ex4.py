#Programmers have lousy memories
#how many cars there are today
cars = 100
#how much space is in each car?
space_in_a_car = 4.0
#how many cars are 'moving'?
drivers = 30
#how many people are just BEING driven?
passengers = 90
#how many cars are 'not moving'?
cars_not_driven =  cars - drivers
#look in line 7
cars_driven = drivers
#how many people can all carpools take?
carpool_capacity = cars_driven * space_in_a_car
#how many passengers are there in average in one car?
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "people to carpool today."
print "We need to put about", average_passengers_per_car, "passengers in each car."
