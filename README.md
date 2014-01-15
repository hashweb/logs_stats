Logs & Stats
======

Prerequesits
--

* Vagrant
* PostgreSQL
* psycopg2 


Getting started
--

You're best of using a VM (Virtualbox), a vagrantFile is already provided so once vagrant is installed you can just vagrantUp.

Inside your virtual machine you will need to install postgresql.
Once your postgres is up and running you will need to run the logs_stats.sql against the database to create your tables

You can run the setup.py script to do some of this for you.

* First install Vagrant by doing
```sh
gem install vagrant
```

* run the setup.py script (on host machine)
```sh
python setup.py
```

* This will create a config.json file (in that file add your shared folder), postgresql and vagrant use this. Once vagrant is setup run setup.py again from the guest machine to setup your database.

(skip this if the above is done....)
A config.json file needs to be created and inserted into the root. The current structure should look something like this.
```json
{
    "db": {
        "host": "Your host, usually 127.0.0.1",
		"dbname": "logs_stats",
		"user": "your DB User",
		"password": "Your DB Password"
    },    
    "vm_config" : {
		"shared_folder": {
			"name": "name of shared folder",
			"path": "path on VM to shared folder",
			"host_path" : "path on host manchine (usually ../logs_stats)"
		}
	}
}
```
logs.hashweb.org