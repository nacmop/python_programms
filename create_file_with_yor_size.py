# nacmop

# open or create file:
my_file = open('your_file_is_really_cool.txt', 'w')
# how much MB:
count_of_mb = int(input('How many megabytes are necessary for you: '))
my_file.write('01001110'*count_of_mb*131072)
