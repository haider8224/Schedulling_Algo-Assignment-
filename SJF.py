


#Getting input of processes
process_queue = []
total_wtime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(input('Enter process_name: '))
    process_queue[i].append(int(input('Enter process_arrival: ')))
    total_wtime += process_queue[i][1]
    process_queue[i].append(int(input('Enter process_bust: ')))
    print ('')

process_queue.sort(key = lambda process_queue:process_queue[2])

print ('ProcessName\tArrivalTime\tBurstTime')
for i in range(n):
    print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
    
print ('Average waiting time: ',(total_wtime/n))

currentTime = process_queue[0][1]
total_tR=0
for x in range(n):
	currentTime += process_queue[x][2]	
	total_tR += currentTime-process_queue[x][1]
	print('Turnarount time for ',x,'process is :',(currentTime-process_queue[x][1]))
print('Average Turnaround time : ', total_tR /n)

