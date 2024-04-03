def delivering_package(truck):
    truck_enroute = truck
    truck_package_list = truck_enroute.package_list
    package_hubs_with_deadlines = []
    package_hubs = []
    wgu_hub = addressStrList[0]
    distance_traveled = 0.0
    start_time = truck_enroute.start_time
    print(start_time)
#--------------creating a hub list for packages with deadlines and without---------------
    for i in range(len(truck_package_list)):
        if truck_package_list[i].delivery_deadline == 'EOD':
            package_hubs.append(truck_package_list[i].address)
        else:
            package_hubs_with_deadlines.append(truck_package_list[i].address)
#-------------using wgu as the initial hub to compare to a random hub in package_hub_with_deadline---
    if len(package_hubs_with_deadlines) != 0:
        hub_distance = distance_calculator(wgu_hub, package_hubs_with_deadlines[0])
    else:
        hub_distance = distance_calculator(wgu_hub, package_hubs[0])
    hub_at = ''
# ------------ After that comparing it to all hubs in package_hub to find the closest hub
    if len(package_hubs_with_deadlines) != 0:
        for i in range(len(package_hubs_with_deadlines)):
            hub_distance_temp = distance_calculator(wgu_hub, package_hubs_with_deadlines[i])
            if hub_distance >= hub_distance_temp:
                hub_distance = hub_distance_temp
                hub_at = package_hubs_with_deadlines[i]
    else:
        for i in range(len(package_hubs)):
            hub_distance_temp = distance_calculator(wgu_hub, package_hubs[i])
            if hub_distance >= hub_distance_temp:
                hub_distance = hub_distance_temp
                hub_at = package_hubs[i]
#---------prints out updated hublist and which hub the truck is currently at
    # also, removes current hub from package_hub_with_deadlines list
    # prints updates how far the truck has traveled
    if len(package_hubs_with_deadlines) != 0:
        package_hubs_with_deadlines.remove(hub_at)
    else:
        package_hubs.remove(hub_at)
    distance_traveled += hub_distance
    time_driven_min = distance_traveled * (60/18)
    if len(package_hubs) == 0 and len(package_hubs_with_deadlines) == 0:
        distant_back_wgu_hub = distance_calculator(hub_at, wgu_hub)
        distance_traveled += distant_back_wgu_hub
        time_driven_min = time_driven_min * 2
    else:
        pass
#------This is the loop that goes until the package_hub list is zero and then goes back to WGU
    while len(package_hubs_with_deadlines) != 0:
        hub_distance = distance_calculator(hub_at, package_hubs_with_deadlines[0])
        for i in range(len(package_hubs_with_deadlines)):
            hub_distance_temp = distance_calculator(hub_at, package_hubs_with_deadlines[i])
            if hub_distance >= hub_distance_temp:
                hub_distance = hub_distance_temp
                hub_new = package_hubs_with_deadlines[i]
        hub_at = hub_new
        package_hubs_with_deadlines.remove(hub_at)
        distance_traveled += hub_distance
        time_driven_min = distance_traveled * (60 / 18)
    while len(package_hubs) != 0:
        hub_distance = distance_calculator(hub_at, package_hubs[0])
        for i in range(len(package_hubs)):
            hub_distance_temp = distance_calculator(hub_at, package_hubs[i])
            if hub_distance >= hub_distance_temp:
                hub_distance = hub_distance_temp
                hub_new = package_hubs[i]
        hub_at = hub_new
        package_hubs.remove(hub_at)
        distance_traveled += hub_distance
        time_driven_min = distance_traveled * (60 / 18)
        if len(package_hubs) != 0:
            pass
        else:
            distant_back_wgu_hub = distance_calculator(hub_at, wgu_hub)
            distance_traveled += distant_back_wgu_hub
            time_driven_min = time_driven_min + (distant_back_wgu_hub * (60/18))
    return distance_traveled, time_driven_min