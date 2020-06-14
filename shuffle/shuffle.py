import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place


    pass


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)