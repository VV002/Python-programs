import random
#Function to simulate the gambler's game
def gambler(stake,goal,num_times):
    win_count = 0
    bets_count = 0
    for i in range(num_times):
        current_stake = stake
        while(current_stake > 0 and current_stake < goal):
            bets_count+=1
            if random.random() < 0.5: #Asuming the chance of winning is 50% to be fair
                current_stake+=1
            else:
                current_stake-=1
        if current_stake == goal:
            win_count+=1
    return win_count,bets_count

#Function to display the final results and Calculate the win and loss percentage
def final_results(stake,goal,num_times):
    win_count,bets_count = gambler(stake,goal,num_times)
    win_percentage = (win_count/num_times)*100
    loss_percentage = 100-win_percentage
    print(f"Number of wins: {win_count} and Total number of bets made: {bets_count}")
    print(f"Wins Percentage: {win_percentage}")
    print(f"Loss Percentage: {loss_percentage}")


#User input for stake,goal and number of times
stake,goal,num_times = map(int,input("Enter the stake,goal and number of times: ").split())
final_results(stake,goal,num_times)