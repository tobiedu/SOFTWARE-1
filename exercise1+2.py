def pounds_to_kgs(stones, pounds):
    return (stones * 14 + pounds) / 2.205

def kgs_to_pounds(kgs):
    return kgs * 2.205

def weight():
    opt = input("\nWhich way?\n1: Pounds to Kilograms\n2: Kilograms to Pounds\nINPUT: ")
    if opt == "1":
        st = int(input("\nEnter the amount of stones the object weights: "))
        po = int(input("Enter the amount of pounds the object weights: "))
        print("\n",pounds_to_kgs(st,po), "kg\n")
    elif opt == "2":
        kg = int(input("Enter the amount of kilograms the object weights: "))
        print("\n",kgs_to_pounds(kg), "lbs\n")
    return

def miles_to_km(miles):
    return miles * 1.6

def km_to_miles(km):
    return km / 1.6

def distance():
    opt = input("\nWhich way?\n1: Miles to Kilometers\n2: Kilometers to Miles\nINPUT: ")
    dis = int(input("\nEnter the distance: "))
    if opt == "1":
        print("\n",miles_to_km(dis), "kms\n")
    elif opt == "2":
        print("\n",km_to_miles(dis), "miles\n")
    return

while True:
    choice = input("Which Conversion?\n1: Weight\n2: Distance\nOther: exit\nINPUT: ")
    if choice == "1":
        weight()
    elif choice == "2":
        distance()
    else:
        break

