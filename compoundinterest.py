# P is principle amount
# R is the rate and
# T is the time span

def compound_interest(principle,rate,time):
    # calculates compound interest
    CI = principle * (pow((1+rate/100),time))
    print("Compund Interest is",CI)
# Driver code
compound_interest(10000,10.25,5)
