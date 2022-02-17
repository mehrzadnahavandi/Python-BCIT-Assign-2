# Mehrzad Nahavandi
# A01231818

import re
import json

def search_by_city_and_bedroom_number(city_name,number_of_bedrooms):
    """find and make a text file based on city name and number of bedrooms"""
    with open("listings.txt", 'r') as listing :
        text = listing.readlines()
        # print(text)
        pattern1 = "\D"+city_name + " BC"
        pattern2 = ",["+ number_of_bedrooms + "-9],[0-9]"
        with open ("report.text", 'a') as report:
            report.write("Listing of properties in " + city_name + " and has " + str(number_of_bedrooms) + " bedrooms"'\n')
            for line in text:
                if re.search(pattern1, line, re.I) and re.search(pattern2,line) :
                    # print(line.strip())
                    report.write(line)





def search_by_price_range():
    """finds and retursn properties with specific price range"""
    with open("listings.txt", 'r') as listing:
        text = listing.readlines()
        # print(text)
        pattern1 =",[5-9[5-9][0-9][0-9][0-9][0-9]|1000000,"

        with open("report.text", 'a') as report:
            report.write("Listing of properties with price between 550000 and 1000000: "'\n')
            for line in text:
                if re.search(pattern1,line):
                    # print(line.strip())
                    report.write(line)





def search_by_city_and_propert_type(city_name,property_type):
    """finds and returns properties with given city name and property type"""
    with open("listings.txt", 'r') as listing :
        text = listing.readlines()
        # print(text)
        pattern1 = "\D"+city_name + " BC"
        pattern2 = ","+property_type
        with open("report.text", 'a') as report:
            report.write("Listing of "+ property_type.title() +" in " + city_name.title() + ":"'\n')
            for line in text:
                if re.search(pattern1,line,re.I) and re.search(pattern2,line,re.I):
                    # print(line.strip())
                    report.write(line)




def reduce_price():
    """reduces 1000 from the price of those properties with 30 days or more for active listing dys """
    with open("listings.txt", 'r') as listing :
        text = listing.readlines()
        #print(text)
        pattern ="[3-9][0-9]$"
        with open("report.text", 'a') as report:
            report.write("listing of prperties with reduced price:"'\n')
            for line in text:
                if re.search(pattern,line):
                    new_list = re.split(",",line)
                    new_list[2] = int(new_list[2]) - 10000
                    new_list1 = ",".join(str(item) for item in new_list)
                    #print(new_list1)
                    report.write(new_list1)






def search_by_postal_code_range(starting_character, ending_number):
    """finds and returns properties with given postal code parameter at starting and ending"""
    with open("listings.txt", 'r') as listing :
        text = listing.readlines()
        # print(text)
        pattern = starting_character.upper() + "\d[A-Z] \d[A-Z]" + "[" + ending_number + "-9]"
        with open("report.text", 'a') as report:
            report.write("Listing that have a postal code that stars with " + starting_character.title() + " and ends with " + ending_number + " or more:"'\n')
            for line in text:
                if re.search(pattern,line):
                    # print(line.strip())
                    report.write(line)




def get_listing(MLS):
    """finds and returns property info based on given MLS"""
    with open("listings.txt", 'r') as listing :
        text = listing.readlines()

        # print(text)
        pattern = MLS
        address_pattern1=re.compile(",(\d.*\w[A-Z][0-9])")
        price_pattern2=re.compile(",(\d{6,7})")
        bedroom_pattern3=re.compile(",(\d),")
        bathroom_pattern4=re.compile(",[0-9],([0-9])")
        property_pattern5=re.compile(",(Condo|House|Townhouse)")
        active_days_pattern6=re.compile("(\d{1,2})$")
        with open("report.text", 'a') as report:
            report.write("Details of MLS " + MLS + " are:"'\n')
            for line in text:
                if re.search(pattern,line):
                    dic = {'MLS':MLS ,
                           'address':address_pattern1.search(line).group(1),
                           'price':price_pattern2.search(line).group(1),
                           'bedrooms':bedroom_pattern3.search(line).group(1),
                           'bathrooms':bathroom_pattern4.search(line).group(1),
                           'property_type':property_pattern5.search(line).group(1),
                           'active_listing_days':active_days_pattern6.search(line).group(1)
                           }
                    print(dic)
                    report.write(json.dumps(dic))