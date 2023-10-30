# There are two whole numbers:
# 1 < a,b <100

# One scientist("Sum") get provided with sum of numbers,
# another  ("Prod") get provided with product of numbers. 
# Both scientists know that numbers 1 < a,b <100.

# Determine the numbers being based on the following dialog: 
#     Prod: I don't know the numbers;
#     Sum: I know it;
#     Prod: then I know the numbers; 
#     Sum: then I know the numbers too.

# Write a program that will determine the numbers a and b by the given conditions.

import numpy as np

def factor_pairs(number):
    '''
    Input: a number which has to be factorized
    Output: list of factor pairs of the product that is equal to the input number

    Example:
    Input: 20
    Output: [[10, 2], [4, 5]]
    '''
    factors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factors.append([i, number // i])
    return factors

def is_prime(number):
    '''
    Input: a number which has to be checked if it is prime
    Output: True if the number is prime, False otherwise

    Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...
    '''
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def split_into_sums(number):
    '''
    Input: a number which has to be split into sums
    Output: list of all possible combinations of two numbers that sum up to the input number

    Example:
    Input: 8
    Output: [[2,6],[3,5],[4,4]]
    '''
    # split combinations into sums
    sum_combinations = np.array([], dtype=np.int32).reshape(0, 2)
    for i in range(2, number // 2 + 1):
        sum_combinations = np.append(sum_combinations, [(i, number - i)], axis=0)
    return sum_combinations


def first_move(sum_results):
    '''
    Input: list of all possible sum combinations
    Output: list of all possible sum combinations after the first phrase
    (removing all sum combinations where both numbers are prime)
    '''
    for sum_result in sum_results:
        possible_numbers = split_into_sums(sum_result)
        for possible_number in possible_numbers:
            if is_prime(possible_number[0]) and is_prime(possible_number[1]):
                sum_results = np.delete(sum_results, np.where(sum_results == sum_result), axis=0)
                break
    return sum_results

def second_move(sum_results):
    '''
    Input: list of all possible sum combinations
    Output: list of all possible answers that deal with the second phrase(rules)
    Description:
    1. Loop over all possible sum combinations
    2. Split each sum combination into combinations of two numbers that sum up to the sum combination
    3. Get all factor pairs of the product of two numbers
    4. For each combination of factor pairs check if it's number are not prime(if yes, then skip this combination)
    5. If the sum of the factor pairs is in the list of all possible sum combinations, then it's not the answer
    6. Append the combination of two numbers to the list of possible answers

    '''
    possible_answers = []
    for i, sum_result in enumerate(sum_results):
        possible_numbers = split_into_sums(sum_result)
        possible_answers.append([])
        for possible_number in possible_numbers:
            factor_pairs_list = factor_pairs(possible_number[0] * possible_number[1])
            append = True
            for factor_pair in factor_pairs_list:
                if is_prime(factor_pair[0]) and is_prime(factor_pair[1]):
                    append = False
                    break
                if sum(factor_pair) in sum_results:
                    if factor_pair == possible_number.tolist():
                        continue
                    append = False
                    break
            if append:
                possible_answers[i].append(possible_number.tolist())
    return possible_answers

def third_move(possible_answers):
    '''
    Input: list of all possible answers that we got after getting the rules from a dialogue
    Output: the answer(chooses the answer where is only one possible choice)
    '''
    # select the answer where is only one possible choice
    for possible_answer in possible_answers:
        if len(possible_answer) == 1:
            return possible_answer[0]
        
if __name__ == "__main__":
    sum_results = np.arange(4, 199, dtype=np.int32)
    print(f'Init sum_combinations count: {len(sum_results)}')

    sum_results = first_move(sum_results)
    print(f'Sum_combinations count after first_move filtering: {len(sum_results)}')

    possible_answers = second_move(sum_results)
    print(f'Possible answers count: {len(possible_answers)}')

    answer = third_move(possible_answers)
    print(f'The answer is a combination: {answer}')