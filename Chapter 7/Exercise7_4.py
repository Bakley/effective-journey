"""
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.
"""


def eval_loop():

    while True:
        user = input('Enter something: ')
        if user == "done":
            break
        print(eval(user))

eval_loop()
