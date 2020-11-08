# SolusVMClient-AutoBoot
 Auto-boots any offline VPSes managed in SolusVM through their Client API

## Usage
### Example config.json:
```json
{
  "hostname": "https://vm.example.com:5656",
  "servers": {
      "server1":{
        "key": "1LKJI-MA47O-1AEFX",
        "hash": "6a5d4ad2erv16assd8e8r4s5d2sf15efa3s2d1e5f"
      },
      "server2": {
        "key": "ABCD1-EFGH2-IJKL3",
        "hash": "adw221e6fedsad2ef5sa6df2f1r5r6t2f1a6s5d1a"
      }
    }
}

```
### Basic Example:
```python
from src import AutoBoot

#default log method is to print result to console
VPSAB = AutoBoot(log=True)
VPSAB.runAll()
```

### Other Examples:
Only print to console if a server is offline
```python
VPSAB = AutoBoot(log=True,logLevel=1)
VPSAB.runAll()
```
Log to file if server offline
```python
VPSAB = AutoBoot(
   log=True,
   logLevel=1,
   type='file',
   filePath='./log.log'
)
VPSAB.runAll()
```
Log everything to file
```python
VPSAB = AutoBoot(
   log=True,
   logLevel=0,
   type='file',
   filePath='./log.log'
)
VPSAB.runAll()
```

## Auto-Run Scheduling (Windows/Task Scheduler)
Create a .bat file somewhere in the project directory. add the following contents:
```bash
cd "C:\absolute\path\to\the\project\src"
python main.py
```
feel free to add a "pause" at the end for testing.

>NOTE:  be sure to add the FULL path! relative path will not work from task scheduler

>NOTE2: ensure "python" is the correct identifier. May be "py", "python3", etc
double click the newly created .bat file.

You'll know it worked if a log file gets created at the path you specified in the ini file.

Assuming all is well at this point, open the start menu and type "task scheduler".

Click "Action" at the top, then "Create Task".

Here's some screenshots of my configuration (runs every 10 minutes)

> [General Tab](http://bit.ly/2nvvIe1)

> [Triggers > New](http://bit.ly/2nvyLTv)

> [Actions](http://bit.ly/2lXrcEE)

When finished, you can right click the newly created task & click "Run". Then, check the log file for a new entry.

## Auto-Run Scheduling (Linux/Cron)
Open terminal (assuming GUI)

type "crontab -e"
create a cron job at the desired frequency with the command "python /path/to/project/main.py"
>Note: If you dont know how to format a cron job, use this: https://crontab-generator.org/
