# # Function to print numbers in snake and ladder pattern
# def print_snake_ladder(n=10):
#     num = 1
#     board = []

#     # Build the board
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(num)
#             num += 1
#         # Reverse every alternate row to create snake pattern
#         if i % 2 != 0:
#             row.reverse()
#         board.append(row)

#     # Print the board
#     for row in reversed(board):  # Start printing from top row
#         print('\t'.join(map(str, row)))


# # Call the function
# print_snake_ladder()

num = 1
board = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(num)
        num += 1
    print(row)
if i % 2 != 0:
    print(row.reverse())
    # print(board.append(row))
    print('')
