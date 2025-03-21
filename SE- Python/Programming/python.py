import webbrowser
import time 



total_breaks=3
break_counts=0
print("The program started at ",time.ctime())
while(break_counts<total_breaks):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=V1RPi2MYptM')
    break_counts=break_counts+1

