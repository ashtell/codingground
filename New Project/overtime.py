def computepay(h, r) :
    print "In computepay", h, r
    if h <= 40 :
        p = r * h
    else :
        p = r * 40 + (r * 1.5 * (h - 40))
    print "Finished with computepay", p
    print p



try: 
    inp = raw_input("Enter Hours: ")
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
    
except:
    print "Error, please enter numeric input"
    quit()

print "In the main code",rate, hours
pay = computepay(rate, hours)
print "We are back", pay