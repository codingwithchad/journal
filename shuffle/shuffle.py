import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # Shuffle the input in place

    for it in range(len(the_list)):
        temp = the_list[it]
        rando = get_random(0, len(the_list))
        the_list[it] = the_list[rando]
        the_list[rando] = temp





sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)