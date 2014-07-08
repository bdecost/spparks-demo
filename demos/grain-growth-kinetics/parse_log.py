#!/usr/bin/env python
""" Extract grain size and count vs time from log file for SPPARKS with diag_style cluster"""

import sys

logfile = ""
try:
  logfile = sys.argv[1]
except:
  sys.exit("Please supply a filename as an argument.")

# extract Time, Nclust, and <R> from logfile
# eschew checking logfile format
Time, Nclust, R_av = [], [], []
with open(logfile, "r") as f:
  for line in f:
    # skip ahead to simulations stats output
    if "Setting up run ..." not in line:
      pass
    else:
      # Extract all stats data
      next(f); line = next(f) # skip to the first line of stats output
      while "Loop time" not in line:
        T, Naccept, Nreject, Nsweeps, CPU, Num, N, R = line.split()
        Time.append(float(T))
        Nclust.append(int(Num))
        R_av.append(float(R))
        line = next(f)

# print output to console
print("time\tNclust\tR_av")
for time, N, R in zip(Time, Nclust, R_av):
  print("{0}\t{1}\t{2}".format(time, N, R))
      
# write output to tab-delimited csv
with open("cluster-stats.csv", "w") as f:
  f.write("time\tNclust\tR_av\n")
  for time, N, R in zip(Time, Nclust, R_av):
    f.write("{0}\t{1}\t{2}\n".format(time, N, R))

# try to plot with matplotlib
try:
  import matplotlib.pyplot as plt
except ImportError:
  print("Install matplotlib to plot data\n")
  sys.exit()

fig, (ax0, ax1) = plt.subplots(1,2,sharey=True)
ax0.plot(Time, R_av, 'o-')
ax0.set_xlabel('Time (MCS)')
ax0.set_ylabel(r'$\langle R \rangle$ (pixels)')

import math
sqrtTime = [math.sqrt(t) for t in Time]
ax1.plot(sqrtTime, R_av, 'o-')
ax1.set_xlabel(r'Time$^\frac{1}{2}$ (MCS$^\frac{1}{2}$)')

plt.show()
