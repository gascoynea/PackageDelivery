# Adam Gascoyne, 001254864
# import from csv, Hashtable, Package, Truck, and datetime to pull data from the different objects and files
import csv
import HashTable
import Package
import Truck
from datetime import datetime, timedelta, time

# Pulling addresses from the addresses.csv file into the list addressData.
# Doing this with a single for loop creates an 0(n).
addressData = []
with open("addresses.csv", 'r', encoding='UTF-8-sig') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for line in data:
        addressData.append(line)
# Distance date is read through a for loop of 0(n) just like the address data.
distanceData = []
with open('WGUPS Distance Table.csv', 'r', encoding='UTF-8-sig') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for row in data:
        distanceData.append(row)
#  Package data works the same as well and is 0(n).
packageData = []
with open('WGUPS Package File (1).csv', 'r', encoding='UTF-8-sig') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for row in data:
        packageData.append(row)
# Using the data the WGUPS Package File (1).csv that was put into the packageData we
# use a for loop to create Package objects form the Package.py with the data from PackageData
# to create a list of package_data as packages_list. This is 0(n).
packages_list = []
for i in range(40):
    packages_list.append(
        Package.Package(int(packageData[i][0]), packageData[i][1], packageData[i][2],
                        packageData[i][3], packageData[i][4], packageData[i][5],
                        packageData[i][6], packageData[i][7], 'At Hub'))
# With the package_list data keys and values are created and used with the built-in insert function
# from the Hashtable class in Hashtable.py to populate the Hashtable. It is 0(n).
for i in range(40):
    key = packages_list[i].package_id
    value = [packages_list[i].package_id, packages_list[i].address, packages_list[i].city, packages_list[i].state,
             packages_list[i].zipcode, packages_list[i].delivery_deadline, packages_list[i].weight_kgs,
             packages_list[i].notes, packages_list[i].status]

    HashTable.H.insert(key, value)
# for loop for creating an address list called addressStrList from the data in addressData.
#  It is 0(n).
addressStrList = []
for i in range(len(addressData)):
    address = (addressData[i])
    addressStr = address[0]
    addressStrList.append(addressStr)
# for loop using the data from distanceData to create a dictionary called hubToHub. It is 0(n).
hubToHub = {}
for i in range(len(distanceData)):
    key = addressStrList[i]
    value = distanceData[i]
    hubToHub[i + 1] = {key: value}
# for loop populating the hubToHub dictionary with key, value pairs with the data from addressStrList.
#  It is 0(n).
for i in range(1, 28):
    hubToHub[i][addressStrList[i - 1]][0] = {addressStrList[0]: hubToHub[i][addressStrList[i - 1]][0]}
    hubToHub[i][addressStrList[i - 1]][1] = {addressStrList[1]: hubToHub[i][addressStrList[i - 1]][1]}
    hubToHub[i][addressStrList[i - 1]][2] = {addressStrList[2]: hubToHub[i][addressStrList[i - 1]][2]}
    hubToHub[i][addressStrList[i - 1]][3] = {addressStrList[3]: hubToHub[i][addressStrList[i - 1]][3]}
    hubToHub[i][addressStrList[i - 1]][4] = {addressStrList[4]: hubToHub[i][addressStrList[i - 1]][4]}
    hubToHub[i][addressStrList[i - 1]][5] = {addressStrList[5]: hubToHub[i][addressStrList[i - 1]][5]}
    hubToHub[i][addressStrList[i - 1]][6] = {addressStrList[6]: hubToHub[i][addressStrList[i - 1]][6]}
    hubToHub[i][addressStrList[i - 1]][7] = {addressStrList[7]: hubToHub[i][addressStrList[i - 1]][7]}
    hubToHub[i][addressStrList[i - 1]][8] = {addressStrList[8]: hubToHub[i][addressStrList[i - 1]][8]}
    hubToHub[i][addressStrList[i - 1]][9] = {addressStrList[9]: hubToHub[i][addressStrList[i - 1]][9]}
    hubToHub[i][addressStrList[i - 1]][10] = {addressStrList[10]: hubToHub[i][addressStrList[i - 1]][10]}
    hubToHub[i][addressStrList[i - 1]][11] = {addressStrList[11]: hubToHub[i][addressStrList[i - 1]][11]}
    hubToHub[i][addressStrList[i - 1]][12] = {addressStrList[12]: hubToHub[i][addressStrList[i - 1]][12]}
    hubToHub[i][addressStrList[i - 1]][13] = {addressStrList[13]: hubToHub[i][addressStrList[i - 1]][13]}
    hubToHub[i][addressStrList[i - 1]][14] = {addressStrList[14]: hubToHub[i][addressStrList[i - 1]][14]}
    hubToHub[i][addressStrList[i - 1]][15] = {addressStrList[15]: hubToHub[i][addressStrList[i - 1]][15]}
    hubToHub[i][addressStrList[i - 1]][16] = {addressStrList[16]: hubToHub[i][addressStrList[i - 1]][16]}
    hubToHub[i][addressStrList[i - 1]][17] = {addressStrList[17]: hubToHub[i][addressStrList[i - 1]][17]}
    hubToHub[i][addressStrList[i - 1]][18] = {addressStrList[18]: hubToHub[i][addressStrList[i - 1]][18]}
    hubToHub[i][addressStrList[i - 1]][19] = {addressStrList[19]: hubToHub[i][addressStrList[i - 1]][19]}
    hubToHub[i][addressStrList[i - 1]][20] = {addressStrList[20]: hubToHub[i][addressStrList[i - 1]][20]}
    hubToHub[i][addressStrList[i - 1]][21] = {addressStrList[21]: hubToHub[i][addressStrList[i - 1]][21]}
    hubToHub[i][addressStrList[i - 1]][22] = {addressStrList[22]: hubToHub[i][addressStrList[i - 1]][22]}
    hubToHub[i][addressStrList[i - 1]][23] = {addressStrList[23]: hubToHub[i][addressStrList[i - 1]][23]}
    hubToHub[i][addressStrList[i - 1]][24] = {addressStrList[24]: hubToHub[i][addressStrList[i - 1]][24]}
    hubToHub[i][addressStrList[i - 1]][25] = {addressStrList[25]: hubToHub[i][addressStrList[i - 1]][25]}
    hubToHub[i][addressStrList[i - 1]][26] = {addressStrList[26]: hubToHub[i][addressStrList[i - 1]][26]}


# This function is used to determine the distance from one hub to another.
# The nested loop causes this to become a 0(n^2).
def distance_calculator(hub1, hub2):
    hub_at = hub1
    hub_go = hub2
    # This nested if statement compares hub_at, hub_go and looks them up in the dict hubToHub for distances.
    # the if statement cause 2 0(n).  So it is 0(n).
    if hub_at in addressStrList and hub_go in addressStrList:
        # for loop is 0(n). So far this function is 0(n).
        for i in range(27):
            # if statement checks if hub_at is in addressStrList. So far this function is 0(n).
            if addressStrList[i] == hub_at:
                hub_at_key = i + 1
                # this loop checks if hub_go is also in addressStrList. If it is it will find the distance between
                # hub_at and hub_go. The nested loop causes this to become a 0(n^2).
                for j in range(27):
                    if addressStrList[j] == hub_go:
                        hub_go_key = j + 1
                        hub_at_distances = hubToHub[hub_at_key][hub_at][hub_go_key - 1][hub_go]
                        if hub_at_distances == '':
                            hub_go_distances = float(hubToHub[hub_go_key][hub_go][hub_at_key - 1][hub_at])
                            return hub_go_distances
                        else:
                            hub_at_distance_flt = float(hub_at_distances)
                            return hub_at_distance_flt
    else:
        print('not in')


#  This is where we instantiate truck objects and load them with package objects.
truck_1 = Truck.Truck(1, [packages_list[3], packages_list[11], packages_list[12],
                          packages_list[13], packages_list[14], packages_list[15],
                          packages_list[16], packages_list[18], packages_list[19],
                          packages_list[20], packages_list[21], packages_list[22],
                          packages_list[30], packages_list[33], packages_list[38],
                          packages_list[39]], addressStrList[0])
truck_2 = Truck.Truck(2, [packages_list[0], packages_list[1], packages_list[2],
                          packages_list[4], packages_list[6], packages_list[7],
                          packages_list[17], packages_list[28], packages_list[29],
                          packages_list[32], packages_list[35], packages_list[36],
                          packages_list[37]], addressStrList[0])
truck_3 = Truck.Truck(3, [packages_list[5], packages_list[8], packages_list[9],
                          packages_list[10], packages_list[23], packages_list[24],
                          packages_list[25], packages_list[26], packages_list[27],
                          packages_list[31], packages_list[34]], addressStrList[0])


# This is where we will find the main 0(n). This function will take in the truck objects.
def delivering_packages(truck):
    # We will read in the package ids from what is in the truck and use those
    # to get all the package data from the hashtable. Both are 0(n).
    package_ids = [truck.package_list[i].package_id for i in range(len(truck.package_list))]
    packages = [HashTable.H.get(package_ids[i]) for i in range(len(package_ids))]
    # This is for the specific instance the package has a wrong address for package 9.
    # It is 0(n)
    wrong_address = []
    if truck.truck_id == 3:
        for i in range(len(packages)):
            if packages[i][0] == 9:
                wrong_address.append(packages[i][0])
                package_wrong = packages[i]
        package_wrong_new = package_wrong
        package_wrong_new[1] = '410 S State St'
        package_wrong_new[2] = 'Salt Lake City'
        package_wrong_new[3] = 'UT'
        package_wrong_new[4] = '84111'
        HashTable.H.insert(9, package_wrong_new)
        packages.remove(package_wrong)
    # initial distance and hub_going are for the initial comparison to find the first hub from
    # the WGU start hub
    initial_distance = 1000
    hub_going = addressStrList[0]
    # This will check if truck_3 is being used and if so goes through a loop to compare pack 25.
    # and pack 6 to see which is closest to the wgu hub. This function is 0(n^2).
    # This also removes packages from the packages list.
    if truck.truck_id == 3:
        for pack in packages:
            if pack[0] == 25:
                hub_going = pack[1]
                package1 = pack
                dist_1 = distance_calculator(addressStrList[0], hub_going)
                truck.distance_travelled += dist_1
                truck.time = truck.start_time + timedelta(hours=truck.distance_travelled / 18)
                truck.location_at = hub_going
                for i in range(len(truck.package_list)):
                    if package1[0] == truck.package_list[i].package_id:
                        truck.package_list[i].delivered_time = truck.time
        packages.remove(package1)
        for pack in packages:
            if pack[0] == 6:
                hub_going = pack[1]
                package1 = pack
                dist_1 = distance_calculator(addressStrList[0], hub_going)
                truck.distance_travelled += dist_1
                truck.time = truck.start_time + timedelta(hours=truck.distance_travelled / 18)
                truck.location_at = hub_going
                for i in range(len(truck.package_list)):
                    if package1[0] == truck.package_list[i].package_id:
                        truck.package_list[i].delivered_time = truck.time
        packages.remove(package1)
    # The WGU hub is not in the truck hub list. So, it has to be manually compared to
    # all hubs of the trucks packages to get the first hub to deliver in nearest neighbor.
    # addressStrList[0] == Wgu hub
    # Also, this is only for truck_1 and 2.
    if truck.truck_id == 1 or truck.truck_id == 2:
        # because of the distance_calculator function the first for loop is a 0(n^2)
        for i in range(len(packages)):
            if distance_calculator(addressStrList[0], packages[i][1]) <= initial_distance:
                initial_distance = distance_calculator(addressStrList[0], packages[i][1])
                hub_going = packages[i][1]
                package_to_remove = packages[i]
        # truck update time, location, distance
        truck.distance_travelled += initial_distance
        truck.time = truck.start_time + timedelta(hours=truck.distance_travelled / 18)
        truck.location_at = hub_going
        packages.remove(package_to_remove)
        # updated delivered time for package. This is 0(n).
        for i in range(len(truck.package_list)):
            if package_to_remove[0] == truck.package_list[i].package_id:
                truck.package_list[i].delivered_time = truck.time
    # While loop that continues until the packages list length is 0
    # This is 0(n^2)
    while len(packages) != 0:
        # this will loop to find the closest distance to the current hub
        hub_dist = distance_calculator(hub_going, packages[0][1])
        for i in range(len(packages)):
            hub_dist_temp = distance_calculator(hub_going, packages[i][1])
            if hub_dist_temp < hub_dist:
                hub_dist = hub_dist_temp
                hub_at = packages[i][1]
            elif hub_dist_temp == hub_dist:
                hub_dist = hub_dist_temp
                hub_at = packages[i][1]
        hub_going = hub_at
        for i in range(len(packages)):
            if hub_going in packages[i][1]:
                package_to_remove = packages[i]
                packages.remove(package_to_remove)
                break
        truck.distance_travelled += hub_dist
        truck_time = truck.distance_travelled / 18
        truck.location_at = hub_going
        truck.time = truck.start_time + timedelta(hours=truck_time)
        for i in range(len(truck.package_list)):
            if package_to_remove[0] == truck.package_list[i].package_id:
                truck.package_list[i].delivered_time = truck.time
    # This code makes the truck go back to WGUPS hub when there are no packages left
    # and adds that time and distance to the truck. This is 0(n^2)
    if len(packages) == 0 and len(wrong_address) == 0:
        back_to_start = distance_calculator(hub_going, addressStrList[0])
        truck.distance_travelled += back_to_start
        truck_time = truck.distance_travelled / 18
        truck.location_at = addressStrList[0]
        truck.time = truck.start_time + timedelta(hours=truck_time)
    # This code is when there is only a pack left on truck_3 with the wrong address
    # This code will go to the last hub then back to WGUPS hub as well as adding both those
    # distance and time to the package object and truck object.
    # The code runs in 0(n^2).
    else:
        HashTable.H.insert(9,
                           [9, '410 S State St', 'Salt Lake City', 'UT', 'EOD', '2', 'Wrong address listed', 'At Hub'])
        wrong_address[0] = '410 S State St'
        distance_to_wrong_address = distance_calculator(hub_going, wrong_address[0])
        truck.distance_travelled += distance_to_wrong_address
        truck_time = truck.distance_travelled / 18
        truck.location_at = addressStrList[0]
        truck.time = truck.start_time + timedelta(hours=truck_time)
        for i in range(len(truck.package_list)):
            if package_wrong[0] == truck.package_list[i].package_id:
                truck.package_list[i].delivered_time = truck.time
        back_to_start = distance_calculator(wrong_address[0], addressStrList[0])
        truck.distance_travelled += back_to_start
        truck_time = truck.distance_travelled / 18
        truck.location_at = addressStrList[0]
        truck.time = truck.start_time + timedelta(hours=truck_time)
        wrong_address.remove(wrong_address[0])


# Using the delivery function with the 3 trucks
delivering_packages(truck_1)
delivering_packages(truck_2)
# truck 3 only leaves when truck 2 is back so its start time reflects that.
truck_3.start_time = truck_2.time
delivering_packages(truck_3)


# The user interface which gives the total times for trucks and distances for them. It also
# prompts the user to input a time that will give an update to the user for all packages being
# delivered.
class Main:
    # User Interface showing of truck total travel/time. Also initializes user input to start.
    print('------------------------------WGUPS------------------------------')
    print("Welcome to the WGUPS interface! Let's get started!\n")
    print(f"Truck 1 travelled: {truck_1.distance_travelled} miles, and started at: {truck_1.start_time} finished at {truck_1.time}.\n"
          f"Truck 2 travelled: {truck_2.distance_travelled} miles, and started at: {truck_2.start_time} finished at {truck_2.time}.\n"
          f"Truck 3 travelled: {truck_3.distance_travelled} miles, and started at: {truck_3.start_time} finished at {truck_3.time}.\n")
    print('The total distance travelled by our trucks for today is',
          truck_2.distance_travelled + truck_3.distance_travelled +
          truck_1.distance_travelled, 'miles.\n')
    start_input = input("Please type 'start' to begin looking up packages.")
    # starts prompt for user to give a time. It is 0(n)
    if start_input == 'start' or start_input == 'Start':
        try:
            time_input = input("Please input the time of day, in this format 'HH:MM:SS', "
                               "to view all package statuses at that point in time.")
            (hours, minutes, seconds) = time_input.split(":")
            time_lookup = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
            print(f"You chose the time: {time_lookup}\n")
            print("Thank you for your your input!\n")
            package_input = input("Please type 'Print' to print packages and their status at the inputted time.\n")
            # Asks user to print all status for the packages
            if package_input == "Print" or package_input == "print":
                for i in range(len(packages_list)):
                    packages_list[i].update_status(time_lookup)
                    print(f"Package {packages_list[i].package_id}: with the address"
                          f" '{packages_list[i].address}, {packages_list[i].city}"
                          f", {packages_list[i].state} {packages_list[i].zipcode}'"
                          f" weight: {packages_list[i].weight_kgs},"
                          f" delivery deadline: {packages_list[i].delivery_deadline},"
                          f"\ndelivery status: {packages_list[i].status}")
                    if packages_list[i].status == "Delivered":
                        print(f"Delivered at {packages_list[i].delivered_time}\n")
                    else:
                        print("Package en route awaiting delivery time.\n")
            else:
                print('you had a wrong input. Program closing...')
                exit()

        except ValueError:
            print('you had a wrong input. Program closing...')
            exit()

    else:
        print('you had a wrong input. Program closing...')
        exit()

