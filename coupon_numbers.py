import random
#Class with Static methods to find Total random numbers required to get distinc coupon number
class coupon_colletor():
    @staticmethod
    def RNG(num): #Method to generate random numbers between 1 and num
        return random.randint(1,num)
    
    @staticmethod
    def collect_coupons(num):#Static method that calculates the total random numbers required to get distinct coupon numbers
        collected_coupons = set()
        total_random_numbers = 0
        while len(collected_coupons) < num:
            total_random_numbers+=1
            coupon = coupon_colletor.RNG(num)
            collected_coupons.add(coupon)
        print(f"Distinct coupons collected are: {collected_coupons}")
        print(f"Total random numbers required to form the distinc coupons are: {total_random_numbers}")

#user input to generate coupon
num = int(input("Enter the number of distinct coupons required: "))
coupon_colletor.collect_coupons(num)
