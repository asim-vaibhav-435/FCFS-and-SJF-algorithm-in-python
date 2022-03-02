from array import *

print('Asim Vaibhav\n COMP C 42\n')
def FCFS():
    try:
        n=int(input('Enter the number of processes: '))
        print('Enter the busrt time of process:')
        bursttime=[]
        for i in range(n):
            bursttime.append(int(input('  P'+str(i+1)+' : ')))
        print('Entered details: '+'\n\tProcess\t\tBurst time')
        for i in range(n):
          print('\t   P'+str(i+1)+'\t\t   '+str(bursttime[i]))

        wt = waittime(bursttime,n)
        tt = turnarndtime(bursttime,n)
        avgtime(wt,tt,n)

    except ValueError as err:
        print(err)
    except ZeroDivisionError as err:
        print('Enter proper value !')

def waittime(bursttime,n):
    print('Waiting time of the process:')
    wt = [0]
    for i in range(1,n):
        wt.append(wt[i-1] + bursttime[i-1])
    for i in range(n):
        print('  P'+str(i+1)+' : '+str(wt[i]))
    return wt
    
def turnarndtime(bursttime,n):
    print('Turnaround time of the processes')
    tt = [bursttime[0]]
    for i in range(n-1):
        tt.append(tt[i] + bursttime[i+1])
    for i in range(n):
        print('  P'+str(i+1)+' : '+str(tt[i]))
    return tt

def avgtime(wt,tt,n):
    print('Average waiting time: '+str(sum(wt)/n))
    print('Average turnaround time: '+str(sum(tt)/n))

FCFS()