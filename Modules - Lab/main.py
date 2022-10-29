"""Calculate Logarithm"""
# from calculate_logarithm import logarithm
#
#
# number = int(input())
# base = input()
# print(logarithm(number, base))

"""ASCII Art"""
# from ascii_art import print_ascii_art
#
#
# word = input()
# print(print_ascii_art(word))

"""Triangle"""
# from triangle import print_triangle
#
# size = int(input())
# print_triangle(size)

"""Mathematical operations"""
# from mathematical_operations import operations
#
# first_number, sign, second_number = input().split()
# print(operations(float(first_number), sign, int(second_number)))

"""Fibonacci sequence"""
# from fibonacci_sequence import create_fibonacci_sequance, locate
#
# sequence = []
# while True:
#     command = input()
#
#     if command == 'Stop':
#         break
#
#     command = command.split()
#
#     if command[0] == 'Create':
#         number = int(command[2])
#         sequence = create_fibonacci_sequance(number)
#         print(' '.join(str(x) for x in sequence))
#     else:
#         number = int(command[1])
#         print(locate(sequence, number))