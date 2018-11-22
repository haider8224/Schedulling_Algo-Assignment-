


#Making a queue
prcs_list = []
t_waitTime = 0

#Getting input from users
n = int(input('Enter the total no of processes: '))


for i in range(n):
    prcs_list.append([])#append a list object to the list
    prcs_list[i].append(input('Enter process_name: '))
    prcs_list[i].append(int(input('Enter process_arrival: ')))
    t_waitTime += prcs_list[i][1]
    prcs_list[i].append(int(input('Enter process_bust: ')))
    print ('')

prcs_list.sort(key = lambda prcs_list:prcs_list[1])

#Displaying Data
print ('ProcessName\tArrivalTime\tBurstTime')
for i in range(n):
    print (prcs_list[i][0],'\t\t',prcs_list[i][1],'\t\t',prcs_list[i][2])
    
print ('Average waiting time: ',(t_waitTime/n))

currentTime = prcs_list[0][1]
total_tR=0
for x in range(n):
	currentTime += prcs_list[x][2]	
	total_tR += currentTime-prcs_list[x][1]
	print('Turnarount time for ',x,'process is :',(currentTime-prcs_list[x][1]))
print('Average Turnaround time : ', total_tR /n)

