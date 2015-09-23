import sys
import urllib2
import json

locations = []

if __name__=='__main__':    
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' \
           % (sys.argv[1], sys.argv[2]))
    request = urllib2.urlopen(url)
    print request
    metadata = json.loads(request.read())
    VMD = metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]\
                  ["VehicleActivity"]
    lineNumber = sys.argv[2]
    print 'Bus Line: %s' % (lineNumber)
    for item in VMD:
            locations.append(item["MonitoredVehicleJourney"]\
                                 ["VehicleLocation"])
    busNumber = len(locations)
    print 'Number of Active Buses : %i' % busNumber
    for j in range(busNumber):
        print 'Bus %d is at latitude %f and longitude %f' \
        % (j, locations[j]["Latitude"], locations[j]["Longitude"])