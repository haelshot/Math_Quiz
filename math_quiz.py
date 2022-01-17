import random


def display_intro():
    title = "** A Simple Math Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("_" * 24)


def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("correct")
        return count
    else:
        print("incorrect, the answer is {}".format(solution))
        return count


def menu_option(index, count):
    number_one = random.randrange(1, 100)
    number_two = random.randrange(1, 100)
    if index == 1:
        problem = str(number_one) + "+" + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        for num in range(2000):
            if number_one > number_two:
                problem = str(number_one) + "-" + str(number_two)
                solution = number_one - number_two
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                break
            elif number_two > number_one:
                problem = str(number_two) + "-" + str(number_one)
                solution = number_two - number_one
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                break
            else:
                number_one = random.randint(1, 100)
                number_two = random.randint(1, 100)
        return count
    elif index == 3:
        problem = str(number_one) + "*" + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        for num in range(2000):
            if number_one % number_two == 0:
                problem = str(number_one) + "/" + str(number_two)
                solution = number_one // number_two
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                break
            elif number_two % number_one == 0:
                problem = str(number_two) + "/" + str(number_one)
                solution = number_two // number_one
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                break
            else:
                number_one = random.randrange(1, 100)
                number_two = random.randrange(1, 100)
        return count


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("you answered", total, "questions with", correct, "correct.")
    print("your score is ", percentage, "%. Play again sometime.", sep="")


def main():
    display_intro()
    display_menu()
    display_separator()
    
    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
    
    print("Exit the quiz if you no play again.")
    display_separator()
    display_result(total, correct)


main()
