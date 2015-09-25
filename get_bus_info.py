import sys
import urllib2
import json
import csv

if __name__=='__main__':
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' \
            % (sys.argv[1], sys.argv[2]))
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    VA = metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]\
                 [0]["VehicleActivity"]
    with open(sys.argv[3], 'w') as busdatacsv:
        buswriter = csv.writer(busdatacsv, delimiter = ',')
        buswriter.writerow(("Latitude", "Longtitude", 
                            "Stop Name", "Stop Status"))
        for i in range(len(VA)):
            busLatitude = (VA[i]["MonitoredVehicleJourney"]
                             ["VehicleLocation"]["Latitude"])
            busLongitude = (VA[i]["MonitoredVehicleJourney"]
                              ["VehicleLocation"]["Longitude"])
            if VA[i]["MonitoredVehicleJourney"]["OnwardCalls"] != {}:
                stopName = (VA[i]["MonitoredVehicleJourney"]["OnwardCalls"]
                              ["OnwardCall"][0]["StopPointName"])
                busDistance = (VA[i]["MonitoredVehicleJourney"]["OnwardCalls"]
                                 ["OnwardCall"][0]["Extensions"]["Distances"]
                                 ["PresentableDistance"])
                buswriter.writerow((busLatitude, busLongitude,
                                    stopName, busDistance))
            else:
                buswriter.writerow((busLatitude, busLongitude, "NA", "NA"))
    print 'csv file printed'
