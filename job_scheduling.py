#Design and implement an application that considers the problem of scheduling n jobs of known durations t1, t2,..., tn for execution by a single processor.
#The jobs can be executed in any order, one job at a time.
#Find and display the schedule that minimizes the total time spent by all the jobs in the system by maximizing the profit.

class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit
   
def scheduleJobs(jobs, T):
    profit = 0
    slot = [-1] * T
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.taskId
                profit += job.profit
                break
    print('The scheduled jobs are:', list(filter(lambda x: x != -1, slot)))
    print('The total profit earned is:', profit)
   
if __name__ == '__main__':
    jobs = []
    print("***********Please enter the pfofit in decreasing order*********")
    n = int(input('Enter the number of jobs: '))
    for i in range(n):
        taskId = int(input(f"Enter the task ID for job {i+1}: "))
        deadline = int(input(f"Enter the deadline for job {i+1}: "))
        profit = int(input(f"Enter the profit for job {i+1}: "))
        jobs.append(Job(taskId, deadline, profit))
    print("***********************")
    T = int(input("Enter the deadline limit: "))
    scheduleJobs(jobs, T)

