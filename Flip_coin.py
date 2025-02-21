import random

#Function to identify the probability of getting heads or tails in 'n' coin flips
def flip_coin(n):
    heads = 0
    tails = 0
    for i in range(n):
        if random.uniform(0,1) < 0.5:
            tails+=1
        else:
            heads+=1
    return heads/n, tails/n

times=int(input("Enter the number of times you want to flip the coin: ")) #Input the number of times you want to flip the coin
prob_head, prob_tail = flip_coin(times)
print(f"Probability of getting heads: {prob_head*100}%")
print(f"Probability of getting tails: {prob_tail*100}% ")
