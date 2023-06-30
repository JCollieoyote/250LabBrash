class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: {str(self.is_annual).lower()}')
        print(f'   Color of flowers: { self.color_of_flowers }')

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects 
def print_list(garden):
    for i, plant in enumerate(garden, start=1):
        print(f'Plant {i} Information:')
        plant.print_info()
        print()


if __name__ == "__main__":
    my_garden = []
    # TODO: Declare a list called my_garden that can hold object of type plant

    user_string = input()
    
    while user_string != '-1':
        plant_details = user_string.split()
        plant_type = plant_details[0]
        plant_name = plant_details[1]
        plant_cost = int(plant_details[2])

        if plant_type == 'plant':
            my_garden.append(Plant(plant_name, plant_cost))
        elif plant_type == 'flower':
            is_annual = plant_details[3] == 'true'
            color_of_flowers = plant_details[4]
            my_garden.append(Flower(plant_name, plant_cost, is_annual, color_of_flowers))

        user_string = input()

    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)