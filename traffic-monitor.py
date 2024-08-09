import os
import sys
import time
import threading
import subprocess
import tkinter
import tkinter.messagebox

def monitor(limit, unit):
    check = "vnstat"
    proc = subprocess.Popen(check, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()
    output = str(output)
    l = []
    for t in output.split():
        try:
            if t == "MiB" or t == "GiB":
                l.append(t)
            else:
                l.append(float(t))
        except ValueError:
            pass

    if unit == l[5] and limit < l[4]:
        print("\nNetwork usage limit exceeded!\n")
        top = tkinter.Tk()

        def hello():
            tkinter.messagebox.showinfo("Warning!",
                                        "Network usage limit exceeded!!!!")

        B1 = tkinter.Button(top, text="Warning", command=hello)
        B1.pack()
        top.mainloop()
    arg = [limit, unit]
    threading.Timer(60.0, monitor, arg).start()


def main():
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        print('Command usage: python3 traffic-monitor.py <data usage in MiB or GiB>')
        print('example: python3 traffic-monitor.py 500 MiB')
        print('or python3 traffic-monitor.py 2 GiB')
        exit(1)
    else:
        limit = float(sys.argv[1])
        unit = str(sys.argv[2])
        monitor(limit, unit)


if __name__ == "__main__":
    main()