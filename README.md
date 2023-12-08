# assignment
Winnipeg Transit
Winnipeg Transit file name: 'on_time_performance_2021_08.zip'
http://wpgopendata.blob.core.windows.net/transit-on-time-archive/on_time_performance_2021_08.zip
Only the 'Weekday' data from 2021-08-03T12:57:00 to 2021-08-03T16:44:29 is taken for analysis.
The code has been tested on Python 3.9.7.
The code reads on-time arrival data from the Winnipeg Transit file, which is shortened in size by taking only 'Weekday' data for bus routes 11 and 71. The original full file is too large (over 550 MB) for processing. The percentage of times when the bus deviates from on-time, i.e., late arrival or early arrivals are computed, and plotted as bar plot. The green color shows early arrivals and the red color shows late arrivals. Another subplot simply shows the time series of all deviations.
