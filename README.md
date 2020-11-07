# SolusVMClient-AutoBoot
 Auto-boots any offline VPSes managed in SolusVM through their Client API


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
