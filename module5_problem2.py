book_rewards = {
    0:0,
    2:5,
    4:15,
    6:30,
    8:60,
}

num_books = int(input("Enter the number of books purchased this month: "))
applicable_books = max([key for key in book_rewards if key <= num_books])
print(f"Rewards: {book_rewards[applicable_books]}")