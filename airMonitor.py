import requests
import json
from enum import Enum
from datetime import datetime, timedelta

class SensorType(Enum):
    Data = "data"
    Diagnostic = "diagnostic"
    All = ""

class TimeConvention(Enum):
    TimeBeginning = "TimeBeginning"
    TimeEnding = "TimeEnding"

class AveragePeriod(Enum):
    Minutes_5 = "AVG5"
    Minutes_10 = "AVG10"
    Minutes_15 = "AVG15"
    Minutes_20 = "AVG20"
    Minutes_30 = "AVG30"
    Hours_1 = "AVG60"
    Hours_2 = "AVG120"
    Hours_3 = "AVG180"
    Hours_4 = "AVG240"
    Hours_6 = "AVG360"
    Hours_8 = "AVG480"
    Hours_12 = "AVG720"
    Hours_24 = "AVG1440"

class AirMonitors:
    """
    Wrapper class for Air Monitors api
    
    :param accountID: Your Air Monitors account id
    :param LicenceKey: Your Air Monitors licence key
    """

    apiBase = "https://api.airmonitors.net/3.5"

    def __init__(self, accountID, licenceKey):
        self.accountID = accountID
        self.licenceKey = licenceKey

    def getAnalysers(self) -> list:
        """
        This call will return a list containing all available analyser types
        :returns: list of AnalyserModel (string)
        """
        path = "/analysers"
        return self.AirMonitorsRequest(path)

    def getCalibrationData(self, startDate: datetime, endDate: datetime, uniqueId: int) -> list:
        """
        This call will return all available records for a defined station between and including the two defined timestamps.

        Data will be returned with the most recent record first in a descending order.
        
        :param startDate: the timestamp of the first record to retreive (inclusive)
        :param endDate: the timestamp of the last record to retreive (inclusive)
        :param uniqueId: ID of the station to get data from

        :returns: 
        """
        path = f"/calibrationdata/{startDate:%Y-%m-%dT%H:%M:%S+00:00}/{endDate:%Y-%m-%dT%H:%M:%S+00:00}/{uniqueId}"
        return self.AirMonitorsRequest(path)

    def getSensors(self) -> list:
        """
        This call will return a list containing all available sensor types.
        
        :returns: 
            SensorName (string)
            SensorLabel (string)
            Type (string)
        """
        
        path = "/sensors"
        return self.AirMonitorsRequest(path)

    def getDataSensors(self) -> list:
        """
        This call will return a list containing all available data sensor types.
        
        :returns: 
            SensorName (string)
            SensorLabel (string)
            Type (string)
        """
        
        path = "/sensors/data"
        return self.AirMonitorsRequest(path)

    def getDiagnosticSensors(self) -> list:
        """
        This call will return a list containing all available diagnostic sensor types.
        
        :returns: 
            SensorName (string)
            SensorLabel (string)
            Type (string)
        """
        
        path = "/sensors/diagnostic"
        return self.AirMonitorsRequest(path)

    def getStations(self) -> list:
        """
        This call will return a list containing all stations that you have access to. This includes any stations that have been shared with you or your organisation.
        
        :returns: 
            uniqueId (string)
            StationType (string)
            StationName (string)
            SerialNumber (string)
            Firmware (string)
            IMSI (int) *null
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            CustomerId (string) *null (shared)

        """

        path = "/stations"
        return self.AirMonitorsRequest(path)

    def getSharedStations(self) -> list:
        """
        This call will return a list containing all stations that have been shared with you or your organisation.
        
        :returns: 
            uniqueId (string)
            StationType (string)
            StationName (string)
            SerialNumber (string)
            Firmware (string)
            IMSI (int) *null
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            CustomerId (string) *null (shared)

        """

        path = "/stations/shared"
        return self.AirMonitorsRequest(path)

    def getOwnedStations(self) -> list:
        """
        This call will return a list containing all stations that your organisation own.
        
        :returns: 
            uniqueId (string)
            StationType (string)
            StationName (string)
            SerialNumber (string)
            Firmware (string)
            IMSI (int) *null
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            CustomerId (string) *null (shared)

        """

        path = "/stations/owned"
        return self.AirMonitorsRequest(path)

    def getLocalStations(self, latitude: float, longitude: float, distance: int) -> list:
        """
        This call will return a list containing all stations within a given distance (km) to given latitude and longitude coordinates.

        Stations without a latitude or longitude present will be disregarded.
        
        :param latitude: the latitude to search local to
        :param longitude: the longitude to search local to
        :param distance: the maximum distance in km from the given longitude/latitude

        :returns: 
            uniqueId (string)
            StationType (string)
            StationName (string)
            SerialNumber (string)
            Firmware (string)
            IMSI (int) *null
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            CustomerId (string) *null (shared)

        """

        path = f"/stations/{latitude:.4f},{longitude:.4f}/{distance}"
        return self.AirMonitorsRequest(path)

    def getStationSetup(self, uniqueId: int) -> list:
        """
        This call will return a list containing the current setup of a station.

        :param uniqueId: the uniqueId of the station
        
        :returns: 
            Channel (int) *null
            SensorName (string)
            SensorLabel (string)
            Type (string)
            UnitName (string)
            Unit (string)
            Rate (int)

        """

        path = f"/stations/setup/{uniqueId}"
        return self.AirMonitorsRequest(path)

    def getStationData(self, startDate: datetime, endDate: datetime, uniqueId: int, sensorTypes: SensorType = None, sensors: list = None, timeConvention: TimeConvention = None, averagePeriod: AveragePeriod = None) -> list:
        """
        This call will return all available records for a defined station between and including the two defined timestamps.

        Data will be returned with the most recent record first in a descending order.

        :param startDate: the timestamp of the first record to retreive (inclusive)
        :param endDate: the timestamp of the last record to retreive (inclusive)
        :param uniqueId: the uniqueId of the station
        :param sensorTypes: data|diagnostic|datadiagnostic

        :returns:
            TBTimestamp (ISO8601 datetime)
            TETimestamp (ISO8601 datetime)
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            Channels (array)
                SensorName (string)
                SensorLabel (string)
                Channel (int) *null
                PreScaled (float)
                Scaled (float)
                UnitName (string)
                Slope (float)
                Offset (float)
                Status (string)


        """

        path = "/stationdata"
        if sensorTypes != None:
            path += "/" + sensorTypes.value
        if timeConvention != None:
            path += "/" + timeConvention.value
        if averagePeriod != None:
            path += "/" + averagePeriod.value
        path += f"/{startDate:%Y-%m-%dT%H:%M:%S+00:00}/{endDate:%Y-%m-%dT%H:%M:%S+00:00}/{uniqueId}"
        if sensors != None:
            path += "/" + "-".join(sensors)
        return self.AirMonitorsRequest(path)

    def getLatestStationData(self, records: int, uniqueId: int, sensorTypes: SensorType = None, sensors: list = None, averagePeriod: AveragePeriod = None) -> list:
        """
        This call will return the last x number of records for a defined station.

        Data will be returned with the most recent record first in a descending order.

        :param records: return the x most recent records
        :param uniqueId: the uniqueId of the station
        
        :returns:
            TBTimestamp (ISO8601 datetime)
            TETimestamp (ISO8601 datetime)
            Latitude (float) *null
            Longitude (float) *null
            Altitude (float) *null
            Channels (array)
                SensorName (string)
                SensorLabel (string)
                Channel (int) *null
                PreScaled (float)
                Scaled (float)
                UnitName (string)
                Slope (float)
                Offset (float)
                Status (string)

        """

        path = "/stationdata"
        if sensorTypes != None :
            path += "/" + sensorTypes.value
        if averagePeriod != None:
            path += "/" + averagePeriod.value
        path += f"/latest/{records}/{uniqueId}"
        if sensors != None:
            path += "/" + "-".join(sensors)
        return self.AirMonitorsRequest(path)

    def getStationPeriod(self, uniqueId: int) -> list:
        """
        This call will return the first and last timestamp for data from a given station

        :param uniqueId: the uniqueId of the station
        
        :returns:
            FirstTBTimestamp (ISO8601 datetime)
            FirstTETimestamp (ISO8601 datetime)
            LastTBTimestamp (ISO8601 datetime)
            LastTETimestamp (ISO8601 datetime)

        """

        path = "/stationdata/period/{uniqueId}"
        return self.AirMonitorsRequest(path)

    def getUnits(self):
        """
        This call will return a list containing all available units.

        :returns:
            UnitName (string)
            Unit (string)


        """

        path = "/units"
        return self.AirMonitorsRequest(path)
        
    def AirMonitorsRequest(self, path: str):
        url = f"{self.apiBase}/GET/{self.accountID}/{self.licenceKey}{path}"
        r = requests.get(url)

        try:
            return json.loads(r.text) if r.status_code == 200 and r.text != "NO DATA WAS FOUND FOR YOUR GIVEN PARAMETERS" else None
        except:
            if r.status_code == 200:
                raise AirMonitorsException(r)       
            raise

class AirMonitorsException(Exception):
    """
    Exception wrapper for AirMonitors API
        `message`: the error message
    """
    def __init__(self, response): 
        self.message = response.text         

def AirMonitorsApi_Test():

    print("Enter your account details to test the api.")
    
    accountID = input("Account ID: ")
    licenceKey = input("Licence Key: ")

    print("Running AirMonitors API tests:")

    api = AirMonitors(accountID, licenceKey)
    
    try:
        print("Your available stations are:")
        print(api.getStations())
    
    except AirMonitorsException as e:
        print(e.message)
    
if __name__ == "__main__":
    AirMonitorsApi_Test()
