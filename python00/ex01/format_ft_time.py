import time as time

stime = time.time()
now = time.localtime()
date = time.strftime("%b %d %Y", now)

print("Seconds since January 1, 1970:", f"{stime:,.3f}", "or", f"{stime:,.3e}", "in scientific notation")
print(date)
