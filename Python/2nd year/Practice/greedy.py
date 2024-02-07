'''
You are given a set of n jobs, each with a deadline and a profit. 
You need to schedule the jobs to maximize the total profit, subject to the 
constraint that each job must be completed before its deadline. 
Design an algorithm using the Greedy approach that solves this problem in O(n log n) time complexity.  
'''

def scheduler(jobs):
    constraint = 1
    days_left_list = []
    prioritized_jobs = []
    organized_profit = []
    total_profit_earned = 0 # this should equal to 18,000
    for every_job in jobs:
        # jobs must be finished before the deadline
        values = jobs.get(every_job)
        days_to_finish = values[0]
        days_left = days_to_finish - constraint
        profit_from_job = values[1]

        # sort the job based on the number of days left
        days_left_list += [days_left]
        prioritized_jobs += [every_job]
        organized_profit += [profit_from_job]
        total_profit_earned += profit_from_job

        

        for i in range(len(days_left_list)):
            
            for j in range(len(days_left_list)- i - 1):
                if j + 1 < len(days_left_list):
                    if days_left_list[j] > days_left_list[j + 1]:
                        # organizes everything in order
                        days_left_list[j + 1], days_left_list[j] = days_left_list[j], days_left_list[j + 1]
                        prioritized_jobs[j + 1], prioritized_jobs[j] = prioritized_jobs[j], prioritized_jobs[j + 1]
                        organized_profit[j + 1], organized_profit[j] = organized_profit[j], organized_profit[j + 1]
                        
    return f'''
    =============================================
    =               TASK PRIORITY               =
    =============================================

    1: {prioritized_jobs[0]}
    DAY/S LEFT BEFORE THE DEADLINE: {days_left_list[0]} days
    Profit: P {organized_profit[0]}

    2: {prioritized_jobs[1]}
    DAY/S LEFT BEFORE THE DEADLINE: {days_left_list[1]} days
    Profit: P {organized_profit[1]}

    3: {prioritized_jobs[2]}
    DAY/S LEFT BEFORE THE DEADLINE: {days_left_list[2]} days
    Profit: P {organized_profit[2]}

    ---------------------------------------------
    Total profit earned: P {total_profit_earned}
    
    '''


# format{"job_name": [days_to_complete, profit]}
set_of_jobs = {"Job 1": [4, 12000], "Job 2": [2, 1000], "Job 3": [3, 5000]}
#print(set_of_jobs.get("Job1"))
print(scheduler(set_of_jobs))
# ----------------------- you have 3 set of jobs to do ----------------------- #
# job 1: Deadline is in 4 days, profit is 12,000
# job 2: Deadline is in 2 days, profit is 1,000
# job 3: Deadline is in 3 days, profit is 5,000
# jobs must be completed before deadline, then reduce 1 day to the jobs
# ----------------------- So the jobs supposed to have ----------------------- #
# job 1: Deadline is in 3 days to complete
# job 2: Deadline is in 1 day to complete
# job 3: Deadline is in 2 days to complete
# goal: maximize time and profit

# -------------------------------- how to do? -------------------------------- #
# prioritize deadlines that takes the least days to complete

