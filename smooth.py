import numpy as np
import matplotlib.pyplot as plt

from csaps import csaps

n = 10000
time = np.zeros(n)
hcnha = np.zeros(n)
time1 = np.zeros(n)
hncaha = np.zeros(n)

f1 = open('data1.dat','r')
f2 = open('data1-modified.dat','w')
f3 = open('data2.dat','r')
f4 = open('data2-modified.dat','w')

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
for i in range (n):
	s = f1.readline()
	token = s.split()
	time[i] = token[0]
	hcnha[i] = token[1]
	
	q = f3.readline()
	token = q.split()
	time1[i] = token[0]
	hncaha[i] = token[1]
	
times = np.linspace(time[0], time[-1], 10000)

hcnhas = csaps(time, hcnha, times, smooth=0.3)
hncahas = csaps(time1, hncaha, times, smooth=0.3)
for i in range (n):
	print(round(times[i],4),'	',round(hcnhas[i],4),file=f2)
	print(round(times[i],4),'	',round(hncahas[i],4),file=f4)
	
plt.figure(1)
plt.figure(figsize=(8,6))
plt.xlabel('Delta t',fontdict=font)
plt.ylabel('TDCF (Correlation)',fontdict=font)
plt.title('HN-N/CAHA TDCF',fontdict=font)
plt.ylim(-0.1,0.1)
#plt.xlim(0,100)
plt.plot(time, hncaha, times, hncahas, '-')
plt.savefig('data1.png')

plt.figure(2)
plt.figure(figsize=(8,6))
plt.xlabel('Delta t',fontdict=font)
plt.ylabel('TDCF (Correlation)',fontdict=font)
plt.title('HCA/NHA TDCF',fontdict=font)
plt.ylim(-0.1,0.1)
#plt.xlim(0,100)
plt.plot(time1, hcnha, times, hcnhas, '-')
plt.savefig('data2.png')
