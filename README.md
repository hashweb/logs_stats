Logs & Stats
======


Getting started
--

You're best of using a VM (Virtualbox), a vagrantFile is already provided so once vagrant is installed you can just vagrantUp.

Inside your virtual machine you will need to install postgresql.
Once your postgres is up and running

A config.json file needs to be created and inserted into the root. The current structure should look something like this.
```json
{
    "db": {
        "host": "Your host, usually 127.0.0.1",
		"dbname": "logs_stats",
		"user": "your DB User",
		"password": "Your DB Password""
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
