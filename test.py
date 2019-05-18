import airMonitors
from pprint import pprint
from datetime import datetime, timedelta

accountID = "xxxxxxxx"
licenceKey = "xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx"

api = airMonitors.AirMonitors(accountID, licenceKey)

try:
    print("Your available analyser models are:")
    for analyser in api.getAnalysers():
        print(analyser)

    print("Your available sensors are:")
    for sensor in api.getSensors():
        print(sensor)

    print("Your available data sensors are:")
    for sensor in api.getDataSensors():
        print(sensor)

    print("Your available diagnostic sensors are:")
    for sensor in api.getDiagnosticSensors():
        print(sensor)

    print("Your available units are:")
    for unit in api.getUnits():
        print(unit)

    print("Your available shared stations are:")
    pprint(api.getSharedStations())

    print("Your available owned stations are:")
    pprint(api.getOwnedStations())

    print("Your available stations within 100km of Greenwich (51.4779, 0.0015) are:")
    pprint(api.getLocalStations(51.4779, 0.0015, 100))

    print("Your available stations are:")
    stationList = api.getStations()
    pprint(stationList)

    for station in stationList:
        stationName = station["StationName"]
        uniqueId = station["UniqueId"]
        startDate = datetime.today() - timedelta(hours=2)
        endDate = datetime.today()

        print(f"Station setup for {stationName} ({uniqueId}) is:")
        pprint(api.getStationSetup(uniqueId))

        print(f"{stationName} ({uniqueId}) has data for:")
        pprint(api.getStationPeriod(uniqueId))

        print(f"Calibration data for {stationName} ({uniqueId}) {startDate:%Y-%m-%dT%H:%M:%S+00:00} - {endDate:%Y-%m-%dT%H:%M:%S+00:00} is:")
        pprint(api.getCalibrationData(startDate, endDate, uniqueId))

        print(f"Data for {stationName} ({uniqueId}) {startDate:%Y-%m-%dT%H:%M:%S+00:00} - {endDate:%Y-%m-%dT%H:%M:%S+00:00} is:")
        pprint(api.getStationData(startDate, endDate, uniqueId))

        print(f"Latest data for {stationName} ({uniqueId}) is:")
        pprint(api.getLatestStationData(1, uniqueId))

        print(f"30 minute average data for {stationName} ({uniqueId}) {startDate:%Y-%m-%dT%H:%M:%S+00:00} - {endDate:%Y-%m-%dT%H:%M:%S+00:00} is:")
        pprint(api.getStationData(startDate, endDate, uniqueId, averagePeriod = airMonitors.AveragePeriod.Minutes_30))

except airMonitors.AirMonitorsException as e:
    print(e.message)
