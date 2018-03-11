book_list = ['The Hunger Games',
             'Harry Potter and the Order of the Phoenix',
             'To Kill a Mockingbird',
             'Pride and Prejudice',
             'Animal Farm',
             '1984'
             ]

book_no_space = [b.replace(' ', '') for b in book_list]

print('Book_no_space: \n{}'.format(book_no_space))

# Makes a NEW list
book_sorted = sorted(book_no_space, key=len)

print('\nBook_sorted:\n{}'.format(book_sorted))
print('\nBook_no_space:\n{}'.format(book_no_space))  # Not changed yet

# Operates on the same list
book_no_space.sort(key=len)
print('\nBook_no_space:\n{}'.format(book_no_space))

# One liner
book_one_liner = sorted([b.replace(' ', '') for b in book_list], key=len)
print('\nBook_one_liner:\n{}'.format(book_one_liner))
