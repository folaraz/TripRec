import geopy.distance
from geopy.geocoders import Nominatim
from dblogic import getTouristLocations


def GetLatLong(start):
    latitide = ''
    longitude = ''
    n = 0
    while n < 5 and longitude == '':
        n += 1
        geolocator = Nominatim(user_agent="Deji_is_a_Fool")
        location = geolocator.geocode("{} Nigeria".format(start))
        latitide, longitude = location.latitude, location.longitude
    return (latitide, longitude)


def GetDistance(start, end):
    return geopy.distance.vincenty(start, end).km


def calCost(start, end):
    distance = GetDistance(start, end)
    cost = (140 * distance)/ 12.5
    return cost


def getCost(start):
    start = GetLatLong(start)
    possibleDestinations = getTouristLocations()
    distanceCost = {}
    for c in possibleDestinations:
        locDetails= possibleDestinations[c]
        distanceCost[c] =[int(calCost(start,(locDetails[0],locDetails[1]))), locDetails[2], locDetails[3]]
    return distanceCost


def locationsWithinBudget(budget, start, zone):
    distance_cost = getCost(start)
    allowable_locations = {}
    other_recommendations = {}
    for loc in distance_cost:
        distance_details = distance_cost[loc]
        cost = distance_details[0]
        geographical_zone = distance_details[1]
        if cost <= budget and geographical_zone == zone:
            allowable_locations[loc] = {"cost": cost, "state": distance_details[2]}
        elif cost <= budget:
            other_recommendations[loc] = {"cost": cost, "state": distance_details[2]}

    if bool(allowable_locations):
        return allowable_locations
    elif bool(other_recommendations):
        return other_recommendations
    else:
        return "No Tourism fits your filter and budget"






