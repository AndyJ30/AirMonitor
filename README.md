# AirMonitor
Wrapper for the [Air Monitors](https://www.airmonitors.co.uk/) web api

# Usage
To use the Air Monitors library:

1. Include `airMonitors.py` in your module/project path
2. Import airMonitors
3. Create a new `AirMonitors` instance using your account id and licence key:
```python
  import airMonitors
  
  accountId = "xxxxxxxxxxx"
  licenseKey = "xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx"

  api = airMonitors.AirMonitors(username, password)
```

# Functions

## getAnalysers()
Gets a list of all available analyser types.

Returns a `list` of `dict`s containing the AnalyserModel name of each type:
```python
>>> api.getAnalysers()
[
  {'AnalyserModel': 'ACx'},
  {'AnalyserModel': 'ADAM4012'},
  {'AnalyserModel': 'ADAM4017'},
  {'AnalyserModel': 'ADAM4050'},
  ...
]
```

## getSensors()
Gets a list of all available sensors.

Returns a `list` of `dict`s containing the SensorName, SensorLabel and Type of all available sensors:

```python
>>> api.getSensors()
[
  {'SensorName': 'Ambient Temp Probe', 'SensorLabel': 'AMBTP', 'Type': 'diagnostic'},
  {'SensorName': 'Ambient Temperature', 'SensorLabel': 'PAMBT', 'Type': 'data'},
  {'SensorName': 'Ammonia', 'SensorLabel': 'NH3', 'Type': 'data'},
  ...
]
```

## getDataSensors()
Gets a list of all available "data" sensors.

Returns a `list` of `dict`s containing the SensorName, SensorLabel and Type of all available sensors:

```python
>>> api.getDataSensors()
[
  {'SensorName': 'Ambient Temperature', 'SensorLabel': 'PAMBT', 'Type': 'data'},
  {'SensorName': 'Ammonia', 'SensorLabel': 'NH3', 'Type': 'data'},
  {'SensorName': 'Auxiliary A', 'SensorLabel': 'AUXA', 'Type': 'data'},
  ...
]
```

## getDiagnosticSensors()
Gets a list of all available "diagnostic" sensors.

Returns a `list` of `dict`s containing the SensorName, SensorLabel and Type of all available sensors:

```python
>>> api.getDiagnosticSensors()
[
  {'SensorName': 'Ambient Temp Probe', 'SensorLabel': 'AMBTP', 'Type': 'diagnostic'},
  {'SensorName': 'Approximate Flow Rate', 'SensorLabel': 'APPFLOW', 'Type': 'diagnostic'}
  {'SensorName': 'ASC Tube Temp', 'SensorLabel': 'ASCTUBETEMP', 'Type': 'diagnostic'}
  ...
]
```

## getUnits()
Gets a list of all available units.

Returns a `list` of `dict`s containing the UnitName and Unit of all available units:

```python
>>> api.getUnits()
[
  {'UnitName': 'ATM', 'Unit': 'atm'},
  {'UnitName': 'Becquerel', 'Unit': 'Bq'},
  {'UnitName': 'Becquerel Per Meter Cubed', 'Unit': 'Bq/m3'},
  ...
]
```

## getStations()
Gets a list of all available stations.

Returns a `list` of `dict`s containing the Altitude, CustomerID, Firmware, IMSI, Latitude, Longitude, SerialNumber, StationName, StationType, and UniqueId of all available stations:

```python
>>> api.getStations()
[
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  ...
]
```

## getSharedStations()
Gets a list of all available shared stations.

Returns a `list` of `dict`s containing the Altitude, CustomerID, Firmware, IMSI, Latitude, Longitude, SerialNumber, StationName, StationType, and UniqueId of all available shared stations:

```python
>>> api.getSharedStations()
[
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  ...
]
```

## getOwnedStations()
Gets a list of all owned stations.

Returns a `list` of `dict`s containing the Altitude, CustomerID, Firmware, IMSI, Latitude, Longitude, SerialNumber, StationName, StationType, and UniqueId of all owned stations:

```python
>>> api.getOwnedStations()
[
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  ...
]
```

## getLocalStations( longitude, latitude, distance )
Gets a list of all available stations within the specified distance (km) from the specified coordinates.

Returns a `list` of `dict`s containing the Altitude, CustomerID, Firmware, IMSI, Latitude, Longitude, SerialNumber, StationName, StationType, and UniqueId of all available stations:

```python
>>> api.getLocalStations(0.0000, 0.0000, 100)
[
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  {'Altitude': None, 'CustomerId': 'xxxxxxxxxxxxxxxx', 'Firmware': 'xxxx', 'Imsi': 'xxxxxxxxxxxxxxxxxxxxx', 'Latitude': None, 'Longitude': None, 'SerialNumber': 0000000, 'StationName': 'xxxxxxxxxxxxxxxxxxx', 'StationType': 'xxxxxxxxx', 'UniqueId': 000000},
  ...
]
```

## getStationSetup( uniqueId )
Gets the details of all sensors on the specified station

`uniqueId`: uniqueId of the station to return data from  

Returns a `list` of `dict`s containing the sensor attributes for each sensor on the specified station:

```python
>>> api.getStationSetup( 123456 )
[
  {'Active': 'true', 'Channel': None, 'Rate': 900, 'SensorLabel': 'AIRPRES', 'SensorName': 'Air Pressure', 'Type': 'data', 'Unit': 'mbar', 'UnitName': 'Pressure (mbar)'},
  {'Active': 'true', 'Channel': None, 'Rate': 900, 'SensorLabel': 'CO2', 'SensorName': 'Carbon Dioxide', 'Type': 'data', 'Unit': 'ppm', 'UnitName': 'Parts Per Million'},
  {'Active': 'true', 'Channel': None, 'Rate': 900, 'SensorLabel': 'CO', 'SensorName': 'Carbon Monoxide', 'Type': 'data', 'Unit': 'ppb', 'UnitName': 'Parts Per Billion'},
  ...
]
```

## getStationPeriod( uniqueId )
Gets the range of data for the specified station.

`uniqueId`: uniqueId of the station to return data from  

Returns a `list` containing a `dict` containing First/Last Time Beginning/Time Ending dates for the available data:

```python
>>> api.getStationPeriod( 123456 )
[
  {'FirstTBTimestamp': '2019-01-01T00:00:00+00:00', 'FirstTETimestamp': '2019-01-01T00:00:00+00:00', 'LastTBTimestamp': '2019-05-01T00:00:00+00:00', 'LastTETimestamp': '2019-05-01T00:00:00+00:00'}
]
```

## getStationData( startDate, endDate, uniqueId, [sensorTypes], [sensors], [timeConvention], [averagePeriod])
Gets the recorded data from the specified station over the specified date range.

`startDate`: datetime to return data starting from (inclusive)  
`endDate`: datetime to return data until (inclusive)  
`uniqueId`: uniqueId of the station to return data from  
`sensorTypes`: (optional) Only return data for this sensor type. `airMonitors.SensorType.[Data|Diagnostic|All]`  
`sensors`: (optional) Only return data for sensors with labels in this `list` of `strings`.
`timeConvention`: (optional) Specify whether the startDate/endDate are compared against the Time Beginning or Time Ending timestamp of each record. `airMonitors.TimeConvention.[TimeBeginning|TimeEnding]`  
`averagePeriod`: (optional) Return average data at the specified interval, instead of the raw logs. `airMonitors.AveragePeriod.[Minutes_5|Minutes_10|Minutes_15|Minutes_20|Minutes_30|Hours_1|Hours_2|Hours_3|Hours_4|Hours_6|Hours_8|Hours_12|Hours_24]`

Returns a `list` of `dict`s containing the logged data:

```python
>>> startDate = datetime.today() - timedelta( hours=2 )
>>> endDate = datetime.today()
>>> api.getStationData( startDate, endDate,  123456 )
[
  {'Altitude': None,
    'Channels': [
      {'Channel': None, 'Offset': 0, 'PreScaled': 997.8, 'Scaled': 997.8, 'SensorLabel': 'AIRPRES', 'SensorName': 'Air Pressure', 'Slope': 1, 'Status': 'Valid', 'UnitName': 'Pressure (mbar)'}, 
      {'Channel': None, 'Offset': 200.109, 'PreScaled': 246.07, 'Scaled': 395.119, 'SensorLabel': 'CO', 'SensorName': 'Carbon Monoxide', 'Slope': 0.7925, 'Status': 'Valid', 'UnitName': 'Parts Per Billion'},
      ...
    ],
  'Latitude': None,
  'Longitude': None,
  'TBTimestamp': '2019-01-01T00:00:00+00:00',
  'TETimestamp': '2019-01-01T00:01:00+00:00'
  },
  ...
]
```

## getLatestStationData( records, uniqueId, [sensorTypes], [sensors], [averagePeriod])
Get the specified number of most recent records form the specified station.

`records`: the number of records to return  
`uniqueId`: uniqueId of the station to return data from  
`sensorTypes`: (optional) Only return data for this sensor type. `airMonitors.SensorType.[Data|Diagnostic|All]`  
`sensors`: (optional) Only return data for sensors with labels in this `list` of `strings`.
`averagePeriod`: (optional) Return average data at the specified interval, instead of the raw logs. `airMonitors.AveragePeriod.[Minutes_5|Minutes_10|Minutes_15|Minutes_20|Minutes_30|Hours_1|Hours_2|Hours_3|Hours_4|Hours_6|Hours_8|Hours_12|Hours_24]`

Returns a `list` of `dict`s containing the logged data:

```python
>>> api.getLatestStationData( 1,  123456 )
[
  {'Altitude': None,
    'Channels': [
      {'Channel': None, 'Offset': 0, 'PreScaled': 997.8, 'Scaled': 997.8, 'SensorLabel': 'AIRPRES', 'SensorName': 'Air Pressure', 'Slope': 1, 'Status': 'Valid', 'UnitName': 'Pressure (mbar)'}, 
      {'Channel': None, 'Offset': 200.109, 'PreScaled': 246.07, 'Scaled': 395.119, 'SensorLabel': 'CO', 'SensorName': 'Carbon Monoxide', 'Slope': 0.7925, 'Status': 'Valid', 'UnitName': 'Parts Per Billion'},
      ...
    ],
  'Latitude': None,
  'Longitude': None,
  'TBTimestamp': '2019-01-01T00:00:00+00:00',
  'TETimestamp': '2019-01-01T00:01:00+00:00'
  }
]
```

## getCalibrationData( startDate, endDate, uniqueId )
Gets the calibration data from the specified station over the specified date range.

`startDate`: datetime to return data starting from (inclusive)  
`endDate`: datetime to return data until (inclusive)  
`uniqueId`: uniqueId of the station to return data from  

Returns a `list` of `dict`s containing the calibration data:

```python
>>> api.getCalibrationData( startDate, endDate,  123456 )

TODO: add example return value

```
