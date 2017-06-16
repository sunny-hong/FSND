import time
import webbrowser

trackingTime = True

print("TakeABreak Program")

start = time.localtime()
print start
sec1 = [((start.tm_year-2000)*365+start.tm_yday)*3600+ start.tm_hour*3600+start.tm_min*60+start.tm_sec]
time.sleep(3)
end = time.localtime()

url = "https://youtu.be/y6Sxv-sUYtM?t=11s"

timelimit = 8

while (trackingTime):
    time.sleep(3)
    end = time.localtime()
    sec2 = [ ((end.tm_year-2000)*365+ end.tm_yday)*3600+ end.tm_hour*3600+end.tm_min*60+end.tm_sec]
    if (sec2[0]-sec1[0] > timelimit) : #in seconds.
        trackingTime=None
        print "%d seconds elapsed, stop working, start dancing." %timelimit
        # Open URL in a new tab, if a browser window is already open.
        webbrowser.open_new_tab(url)



# print(end - start)
