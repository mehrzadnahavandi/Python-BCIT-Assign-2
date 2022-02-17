# Mehrzad Nahavandi
# A01231818

import assignment2

def main():

    city_name = input("enter the city name: ").lower()
    number_of_bedrooms = input("enter number of bedrooms: ")
    assignment2.search_by_city_and_bedroom_number(city_name, number_of_bedrooms)

    assignment2.search_by_price_range()

    city_name = input("enter the city name: ").lower()
    property_type = input("enter the property type: ").lower()
    assignment2.search_by_city_and_propert_type(city_name,property_type)

    assignment2.reduce_price()



    starting_character = input("enter the starting character: ")
    ending_number = input("enter th ending number: ")
    assignment2.search_by_postal_code_range(starting_character, ending_number)


    MLS = input("enter the MSL: ")
    assignment2.get_listing(MLS)





if __name__ == "__main__":
    main()