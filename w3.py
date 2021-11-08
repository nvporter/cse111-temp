def main():
    start = int(input('Enter the starting odemeter number (in miles): '))
    end = int(input('Enter the ending odemeter number (in miles): '))
    fuel = int(input('Enter amount of fuel that was consumed (in gallons): '))

    mpg = miles_per_gallon(start, end, fuel)
    lp100k = lp100k_from_mpg

    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    
    print(f'{mpg:.2f}')
    
    mpg = (end - start) / fuel




    return mpg



def lp100k_from_mpg(mpg):

    return

main()

