# import the random module
import random


class Lottery:

    def __init__(self):
        self._lottery_numbers = lotto_nums

    def generate_lottery_numbers():
        # create empty set to store values in
        lotto_nums = set([])

        # while loop to run 6 times
        while len(lotto_nums) < 6:
            # random.randint() to generate the random numbers
            num = random.randint(1, 50)
            # append the randomly generated numbers to the lotto_nums set
            lotto_nums.add(num)
        print(lotto_nums)

    # generate_lottery_numbers()

# use a set instead of a list
# for loop with a nested while loop with 'continue'


def main():
    Lottery.generate_lottery_numbers()


if __name__ == "__main__":
    main()