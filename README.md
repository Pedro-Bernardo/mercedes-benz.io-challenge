# Mercedes-Benz.io Code Challenge - Service availability

**2nd Place**  
**Name:** Pedro Miguel Sousa Bernardo  
**e-mail:** pedro_bernardo@icloud.com    
**github:** https://github.com/Pedro-Bernardo  
**website:** http://web.tecnico.ulisboa.pt/ist186500/  
**college:** Instituto Superior Técnico, Universidade de Lisboa  
**degree/year:** Licenciatura em Engenharia Informática e de Computadores, 3º ano  

It was a great project, a lot of fun and I got to learn some more about python which is always great!   

## Running the application
Requirements: **python3**  
Every module used should be included in every python3 installation, so **python3 is the only dependency**.

This module was developed and tested in macOS Mojave 10.14.3. It was also tested in Arch Linux 4.20.12, x86_64

1. Navigate to the project directory
2. a) run the following:
``` bash
                    $> ./statuschecker <command> [args...]
```
2. b) If this doesn't work, run it directly with python3 like so:
``` bash
                 $> python3 statuschecker <command> [args...]
```




## Design Choices
The tool's name is **statuschecker**.    

Every bonus was implemented.

For this challenge I decided to store the tool's data in local JSON files. The history file is called *history.json* and the config is *config.json*.

My solution monitors the availability of the following services:
- GitLab - http://status.gitlab.com
- Slack - https://status.slack.com
- BitBucket - https://status.bitbucket.org
- GitHub - https://www.githubstatus.com 
    - not monitoring https://status.github.com since it has been deprecated.

It was implemented in Python3 and it has the following directory structure:

```
|_ slackstatus (the executable)  (cmd line arg parsing and command calling)
|_ config.json  
|_ history.json  
|_ core    
|   |_ .py modules        (main application logic)
|   |_ commands           (directory where the commands are implemented)
|   |   |_ DoPoll.py
|   |   |_ DoFetch.py
|   |       ...
|   |_ parsers            (status response parsers for the various services)
|       |_ GitLabParser.py
            ...
```

When the tool launches, it uses a python module called *argparse* to parse the command line arguments, identifying the command to be called. These arguments, as well as the ServiceStatus classes are passed to the correct command (as in the Command design pattern). The correct command is then executed.

In the core directory is implemented the Visitor design pattern, materialized in the StatusChecker class. The accepting classes are the Status classes (i.e., GitLabStatus, BitBucketStatus, etc...). Each class is implemented in a different file with their name.

The StatusChecker class implements the visitor method for each of the supported services. It uses python's urllib to query the specified service's url and retrieve it's *HTML*. It will also detect any problems with the status page itself or with the network connection, assigning the service's status to *"status unavailable"* if it can't establish the connection.  
If all goes well and it is able to get the status page's *HTML*, then it calls the correct parser for the given service, which has hardcoded information about where to retrieve the status information from in the *HTML*. It varies a bit from service to service. 


## Command details
### history
The history command outputs the result of every status query executed by the program (saved to *history.json*). These are shown chronologically and by service name.  
Example:
```
...
  -> 02/27/19 21:21:41 up
============================
=========[ gitlab ]=========
  -> 02/27/19 21:13:12 up
  -> 02/27/19 21:21:19 up
  -> 02/27/19 21:21:26 up
  -> 02/27/19 21:21:34 up
  -> 02/27/19 21:21:43 up
============================
...
```

### backup
The backup command takes a path argument and, if it can, it will write plain json to it, effectively copying the contents of the *history.json* file to the specified path.  
The --format=txt option saves the entries in the following format (also grouped by service):
```
[github] 02/27/19 21:13:11 - up
[github] 02/27/19 21:21:18 - up
[github] 02/27/19 21:21:26 - up
[github] 02/27/19 21:21:33 - up
[github] 02/27/19 21:21:42 - up
[github] 02/27/19 21:21:49 - up
```

### restore
The restore command can only restore if the data in the specified file is in *json*, and if the file extension is *.json* or *.txt*.
I assumed the custom formats from backup were not for restoring purposes but for *backup* purposes only, as the name suggests. I had plans to implement these features but time was lacking.



