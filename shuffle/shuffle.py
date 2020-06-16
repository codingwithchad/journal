import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # Shuffle the input in place
    new_list = [0] * len(the_list)
    mangled_list = the_list.copy()
    num = get_random(0, len(the_list) -1 )
    new_list[num] = mangled_list[num]
    mangled_list[num] = None

    for it in range(len(the_list) - 1):
        num = get_random(0, len(the_list) - 1)
        while mangled_list[num] is None:
            num = get_random(0, len(the_list) - 1)
        if num is not None:
            new_list[num] = mangled_list[num]
        mangled_list[num] = None
    the_list = new_list.copy()






sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)