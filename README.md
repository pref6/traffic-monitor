# traffic-monitor
A simple python script that tracks the amount of traffic and notifies you when it has been exceeded. You can set your own traffic volume.

**Setup:**

Install ```vnstat``` if you don't have it:
```
$ sudo apt-get install vnstat
```

**Usage:**

To run, enter this command. Instead of xxx, specify the amount of traffic and select MiB or GiB. The & sign is needed for background operation.
```
$ python traffic-monitor.py xxx MiB/GiB &
```
If you want to stop the process at any time use:
```
$ ps -ef
```
To get a process sheet and kill an unwanted one, use:
```
$ sudo kill pid
```
