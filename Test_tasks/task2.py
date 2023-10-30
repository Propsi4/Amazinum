import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# SETTINGS
SIZE = 7
A = np.zeros((SIZE, SIZE))
history = np.empty((0, SIZE, SIZE))

# FUNCTIONS
def count_neighbours(A, col, row):
    ''' Calculates neighbours of cell
    Args:
        A (numpy.array): matrix
        col (int): column of cell
        row (int): row of cell
    Returns:
        int: number of neighbours
    '''
    neighbours = 0
    if col > 0 and row > 0 and A[col-1][row-1] == 1:
        neighbours += 1
    if col > 0 and A[col-1][row] == 1:
        neighbours += 1
    if col > 0 and row < SIZE-1 and A[col-1][row+1] == 1:
        neighbours += 1
    if row > 0 and A[col][row-1] == 1:
        neighbours += 1
    if row < SIZE-1 and A[col][row+1] == 1:
        neighbours += 1
    if col < SIZE-1 and row > 0 and A[col+1][row-1] == 1:
        neighbours += 1
    if col < SIZE-1 and A[col+1][row] == 1:
        neighbours += 1
    if col < SIZE-1 and row < SIZE-1 and A[col+1][row+1] == 1:
        neighbours += 1
    return neighbours

def change_cell(A, col, row):
    ''' Changes cell
    Args:
        A (numpy.array): matrix
        col (int): column of cell
        row (int): row of cell
    Returns:
        None
    '''
    #count neighbours
    neighbours = count_neighbours(A, col, row)

    #count new value
    if A[col][row] == 1:
        if neighbours < 2 or neighbours > 3:
            A[col][row] = 0
    else:
        if neighbours == 3:
            A[col][row] = 1

    #save iteration
    global history
    history = np.append(history, [A], axis=0)

def change_cells(A):
    '''якщо в живої клітини два чи три живих сусіди, то вона лишається жити;
    якщо в живої клітини один чи немає живих сусідів, то вона помирає від «самотності»;
    якщо в живої клітини чотири та більше живих сусідів, то вона помирає від «перенаселення»;
    якщо в мертвої клітини рівно три живих сусіди, то вона оживає.'''

    ''' Applies rules to matrix A
    Args:
        A (numpy.array): matrix
    Returns:
        None
    '''
    for col in range(SIZE):
        for row in range(SIZE):
            change_cell(A, col, row)

# VIZUALISATION
def change_iteration(step): 
    ''' Changes iteration of vizualisation
    Args:
        history (numpy.array): history of iterations
        step (int): current iteration
    Returns:
        None
    '''
    global history
    # Col and row of the cell at 'step' value
    if step == 0:
        col = -1
        row = 0
    else: 
        col = (step - 1) % SIZE
        row = ((step - 1) // SIZE) % SIZE
    
    if (step > len(history) - 1):
        change_cell(history[step-1].copy(), row, col)

    ax.set_title(f"Ітерація {step}/{len(history)-1}")
    ax.imshow(history[step], cmap="binary")

    # Unhighlight the previous cell
    if hasattr(change_iteration, 'highlighted_cell'):
        change_iteration.highlighted_cell.remove()

    # Highlight the cell at 'step' value
    # Add a red border to highlight the cell
    highlighted_cell = plt.Rectangle((col - 0.5, row - 0.5), 1, 1, fill=False, color='red', linewidth=2)
    change_iteration.highlighted_cell = ax.add_patch(highlighted_cell)

    # Redraw the figure
    fig.canvas.draw_idle()

def forward(event):
    ''' Changes iteration to next
    Args:
        event (event): event
    Returns:
        None
    '''
    global step, history
    step += 1
    if(step > len(history) - 1 and loop_history):
        step = 0
    change_iteration(step)

def backward(event):
    ''' Changes iteration to previous
    Args:
        event (event): event
    Returns:
        None
        '''
    global step, history
    step -= 1
    if(step < 0):
        step = len(history) - 1
    change_iteration(step)
# END FUNCTIONS

# MAIN
# input matrix A
choice = input("Заповнити матрицю вручну? (y/n): ")

if choice == "y":
    print("Введіть матрицю (Допустимі значення 0 або 1): ")

for col in range(SIZE):
    for row in range(SIZE):
        if choice == "y":
            print(f"A[{col}][{row}] = ", end="")
            A[col][row] = int(input())
        else:
            A[col][row] = np.random.randint(2)

# Save raw matrix
history = np.append(history, [A.copy()], axis=0)

# Print raw matrix and apply rules
print("Матриця A: ")
print(A)
change_cells(A)
print("Матриця A після застосування правил: ")
print(A)

print("Історія ітерацій: ")
print("1-Повторювати історію; 0-Безкінечно продовжувати її")
loop_history = int(input("Ваш вибір: "))
# Vizualise iteration simulation
fig = plt.figure()
ax = fig.add_subplot()
ax.imshow(A, cmap="binary")

# Add buttons
ax_backward = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_forward = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_forward = Button(ax_forward, 'Вперед')
btn_backward = Button(ax_backward, 'Назад')

# Current iteration number
step = 0
# Visualize the first iteration
change_iteration(step)

# Bind the buttons click events
btn_forward.on_clicked(forward)
btn_backward.on_clicked(backward)

# Show the plot
plt.show()