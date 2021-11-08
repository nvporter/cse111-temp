import math


def main():
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the can_sizes list, unpack the values
    # into the variables name, radius, height, and cost.
    for name, radius, height, cost in can_sizes:

        # Call the storage_efficiency and cost_efficiency functions.
        store_eff = storage_efficiency(radius, height)
        cost_eff =  cost_efficiency(radius, height, cost)

        # Print the can size name, storage
        # efficiency, and cost efficiency.
        print(f"{name} {store_eff:.1f} {cost_eff:.0f}")

    
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

    # Print the best storage and cost efficiencies.
    print("Best can size in storage efficiency:", best_store)
    print("Best can size in cost efficiency:", best_cost)


def storage_efficiency(radius, height):
  
    volume = cylinder_volume(radius, height)
    surf_area = cylinder_surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency


def cost_efficiency(radius, height, cost):
 
    volume = cylinder_volume(radius, height)
    efficiency = volume / cost
    return efficiency


def cylinder_volume(radius, height):
 
    volume = math.pi * radius**2 * height
    return volume


def cylinder_surface_area(radius, height):
  
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area


# Start this program by
# calling the main function.
main()
