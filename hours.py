time = float(input("Input time in secs: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hr = time // 3600
time %= 3600
mins = time // 60
time %= 60
secs = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hr, mins, secs))
