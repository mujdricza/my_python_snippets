# Install and use MongoDB 

The following notes summarizes installing MongoDB under WSL2 for my local experiments
(on CLI and via Python).

See documentation under
https://www.mongodb.com/docs/manual/tutorial/


## Install for Ubuntu

See documnetation:
https://www.mongodb.com/docs/manual/administration/install-community/?operating-system=linux&linux-distribution=ubuntu&linux-package=default&search-linux=with-search-linux
- e.g. MongoDB 8.2 Community Edition

NOTE: 
The mongodb package provided by Ubuntu is not maintained by MongoDB Inc. and conflicts with the official mongodb-org package.

If not yet installed, do:
```
$ sudo apt install gnupg curl
```

Get MongoDB:
```
$ wget -qO - https://www.mongodb.org/static/pgp/server-8.0.asc |  gpg --dearmor | sudo tee /usr/share/keyrings/mongodb.gpg > /dev/null 
$ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.2.list
```

```
$ sudo apt update
$ sudo apt install -y mongodb-org
```
Then
```
-> emm@axx-PF3L1VPD:~ $ cat /etc/apt/sources.list.d/mongodb-org-8.2.list
deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.2 multiverse
```

Notes: 
* If the ulimit value for number of open files is under 64000, MongoDB generates a startup warning.
* If you installed through the package manager, the data directory /var/lib/mongodb and the log directory /var/log/mongodb are created during the installation.
* The official MongoDB package includes a configuration file (/etc/mongod.conf).


Using `systemd`:
```
$ emm@axx-PF3L1VPD:~ $ ps --no-headers -o comm 1
systemd

# Start MongoDB.
$ sudo systemctl start mongod

# OR if needed
$ sudo systemctl daemon-reload
$ sudo systemctl start mongod

# Verify that MongoDB has started successfully.
$ sudo systemctl status mongod

# optionally, if needed:
$ sudo systemctl enable mongod

# Stop MongoDB.
$ sudo systemctl stop mongod

# Restart MongoDB.
$ sudo systemctl restart mongod
```

Using local MongoDB via MongoDB Shell: https://www.mongodb.com/docs/mongodb-shell/
```
# Simple command for local databases
$ mongosh

# with more info for connecting remote hosts
# mongodb://{user}:{password}@{host}:{port}
# e.g.
$ mongosh mongodb://root:sqqmKJo7B6hj107AqPxSTXa4@172.21.30.245:27017

# some basic command examples
test> show dbs
admin          100.00 KiB
config          60.00 KiB
entertainment   64.00 KiB
local           72.00 KiB
test> use entertainment
switched to db entertainment
entertainment> show collections
movies
entertainment> db.movies.aggregate([{ $group: { _id: "$year", movie_count: { $sum: 1 } } }, { $sort: { movie_count: -1 } }, {$limit:1}])
[ { _id: 2016, movie_count: 73 } ]

# quit
entertainment> exit
```

Export and import data
```
# Export data to JSON
$ mongoexport --db <database_name> --collection <collection_name> --out <output_file.json>
# e.g.
$ $ curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-DB0151EN-edX/labs/FinalProject/movies.json
$ mongoimport -u root -p sqqmKJo7B6hj107AqPxSTXa4 --authenticationDatabase admin --db entertainment --collection movies --file movies.json --host mongo

# Import data from JSON
$ mongoimport --db <database_name> --collection <collection_name> --file <input_file.json>
# e.g.
$ mongoexport --db entertainment --collection movies --out partial_data.csv --type=csv --fields _id,title,year,rating,Director
```
    
