# ThreadsInterview
Threads Interview python task

# ThreadsInterview
Threads Interview python task

Prerequisites:
1. Pandas
    Install Pandas : pip install pandas

Assumptions:
1. Code is written in Windows Operating system.
2. Code is tested with python2.7
3. Named the program as tipt-visualiser(tool for internet provider technicians)
Run:
python tipt-visualiser.py

It will ask for postcode, depending on postcode it will read the csv file present in current directory under
2016_fixed_pc_r01.

Result:
$ python tipt-visualiser.py
Enter the Postcode : AB101UP
| ------ Average download speed (Mbit/s) -- Average upload speed (Mbit/s) -- Availability -- |
|  SFBB            48.5                                10.0                      Available     |
|  UFBB            8.0                                0.0                      UnAvailable     |
|  NGA             8.0                                0.8                      Available     |
|--------------------------------------------------------------------------------------------|
