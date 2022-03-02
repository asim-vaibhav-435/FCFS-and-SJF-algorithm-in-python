class SJF:
    def __init__(self,burstTime,n):
        self.BT = burstTime
        self.n = n
    
    def waitTime(self):
        wt=[0]
        for i in range(self.n-1):
            wt.append(wt[i]+self.BT[i][1])
        for j in range(self.n):
            print(' '+self.BT[j][0]+' : '+str(wt[j]))
        return wt
    
    def turnAroundTime(self):
        tat=[self.BT[0][1]]
        for i in range(self.n-1):
            tat.append(tat[i]+self.BT[i+1][1])
        for j in range(self.n):
            print(' '+self.BT[j][0]+' : '+str(tat[j]))
        return tat

    def avgTime(self, array):
        avgtime = sum(array)/len(array)
        return avgtime


def run():
    print('\tCPU scheduling - Shortest Job First (SJF) ')
    n = int(input('Enter the number of processes: '))
    burstTime = []
    print('Enter burst time of process: ')
    for k in range(n):
        burstTime.append(['P'+str(k+1),int(input('  P'+str(k+1)+' : '))])
    burstTime.sort(key= lambda x:x[1])
    obj = SJF(burstTime,n)
    print('Wait time of the process: ')
    wt = obj.waitTime()
    print('Turn Around time of the process: ')
    tat = obj.turnAroundTime()
    print('Average time : \
        \n Wait time: '+str(obj.avgTime(wt))+\
        '\n Turnaround time: '+str(obj.avgTime(tat)))


if __name__ == '__main__':
    run() 