#Now we are learning about format strings :D
#That means that every time I am putting double quotes to something, it is a strings

my_name = 'Carla Naujoks'
my_age = 19 # yes it's true :(
my_height = 1.65 #cm
my_weight = 65
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#Now we are using formatters %s, %r and %d. Das zeichen wird durch den Wert auf der rechten Seite ersetzt. Nicht vergessen: % davor setzen!!!
print "Let's talk about %s." % my_name
print "She's %s centimeters tall." %my_height
print "She's %s kg heavy." % my_weight
print "Actually that's not too heavy"
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s, because she doesn't like coffee." % my_teeth

#I bet this line is not as tricky as you think it is, Zed!!
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
