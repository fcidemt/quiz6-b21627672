import matplotlib.pyplot as plt

occupancy_data = open('occupancy.data', 'r')
occupancy = []   #datanın liste hali
for line in occupancy_data:
    if line[-1] == "\n":
        line = line[:-1]
    line = line.split(";")
    line[1:2] = line[1].split(" ")
    occupancy.append(line)

dates = {date[1][-2:] for date in occupancy}
x = list(sorted(dates))
y1 = []                 #occup
y2 = []                 #noccup
for i in x:
    occup = 0
    noccup = 0
    for j in occupancy:
        if i == j[1][-2:]:
            if j[8] == "1":
                occup += 1
            elif j[8] == "0":
                noccup += 1
    y1.append(occup)
    y2.append(noccup)

plt.plot(x,y1, color='b', label='Occupied')
plt.plot(x,y2, color='r', label='Not-occupied')
plt.legend(loc='upper left')
plt.ylabel('# of samples')
plt.xlabel('Days')
plt.savefig("Fig1.pdf")
# first plot finished

temperature = [float(i[3]) for i in occupancy if i[8] == "1"]
n_temperature = [float(i[3]) for i in occupancy if i[8] == "0"]
humidity = [float(i[4]) for i in occupancy if i[8] == "1"]
n_humidity = [float(i[4]) for i in occupancy if i[8] == "0"]
light = [float(i[5]) for i in occupancy if i[8] == "1"]
n_light = [float(i[5]) for i in occupancy if i[8] == "0"]
co2 = [float(i[6]) for i in occupancy if i[8] == "1"]
n_co2 = [float(i[6]) for i in occupancy if i[8] == "0"]

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.hist(temperature, bins=47, color="b")
ax1.set_title("Temperature")
ax2 = fig.add_subplot(222)
ax2.hist(humidity, bins=47, color="r")
ax2.set_title("Humidity (%)")
ax3 = fig.add_subplot(223)
ax3.hist(light, bins=47, color="g")
ax3.set_title("Light")
ax4 = fig.add_subplot(224)
ax4.hist(co2, bins=47, color="purple")
ax4.set_title("Co2")
fig.suptitle('Occupied')
plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.savefig("Fig2.pdf")

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.hist(n_temperature, bins=15, color="b")
ax1.set_title("Temperature")
ax2 = fig.add_subplot(222)
ax2.hist(n_humidity, bins=15, color="r")
ax2.set_title("Humidity (%)")
ax3 = fig.add_subplot(223)
ax3.hist(n_light, bins=15, color="g")
ax3.set_title("Light")
ax4 = fig.add_subplot(224)
ax4.hist(n_co2, bins=15, color="purple")
ax4.set_title("Co2")
fig.suptitle('Not occupied')
plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.savefig("Fig3.pdf")

occupancy_data.close()
