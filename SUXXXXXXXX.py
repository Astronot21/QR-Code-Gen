"""
Skeleton code for CS114 project 2025: A QR code generator.

This skeleton code for the project is intended as a starting point for students
to get an idea of how they can begin to code the project. You are not required
to use any of the functions in this skeleton code, however you may find some of
the ideas useful. Your code, however, is required to have the line:

if __name__ == "__main__":

but you are free to and should modify the lines following this.

None of the functions are implemented yet, so if you would like to
use a particular function, you need to implement it yourself. If you decide not
to use any of the functions, you are free to leave them empty or remove them
from this file. You are also free to alter the function signatures (the name of
the function and its arguments), so if you need to pass more arguments to the
function, or do not need a particular argument, you are also free to add and
remove arguments as you see fit. We provide the function signatures only as a
guide for how we think you can start to approach the project.
"""

# imports
import os
import sys
import stdio
# Your imports go here
import stdarray
import stddraw

# global variables
# Your global variables go here

def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # =========================================================================================================
    # Canvas variables:

    row_counter:int = 0

    CANVAS_SIDE_LENGTH = 600
    square_size:float = CANVAS_SIDE_LENGTH / (len(qr_grid) + 8)

    # =========================================================================================================

    # =========================================================================================================
    # Canvas setup:

    stddraw.setCanvasSize(CANVAS_SIDE_LENGTH, CANVAS_SIDE_LENGTH)
    stddraw.setXscale(0, CANVAS_SIDE_LENGTH)
    stddraw.setYscale(0, CANVAS_SIDE_LENGTH)
    stddraw.setPenRadius(0.002)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledSquare(CANVAS_SIDE_LENGTH/2, CANVAS_SIDE_LENGTH/2, CANVAS_SIDE_LENGTH/2)


    # Margin (4 squares)
    margin = 4 * square_size

    # Important: Start from top (highest y value), and move downward
    start_y = CANVAS_SIDE_LENGTH - margin - (square_size / 2)

    # =========================================================================================================

    # =========================================================================================================
    # Drawing squares:

    # Colours set according to Doc 3: QR Code specifications
    for row in qr_grid:
        column_counter = 0
        x = margin + (square_size / 2)

        for value in row:
            if value == 0:
                stddraw.setPenColor(stddraw.WHITE)
            elif value == 1:
                stddraw.setPenColor(stddraw.BLACK)
            else:
                stddraw.setPenColor(stddraw.GRAY) # dashes
                
            stddraw.filledSquare(
                x,
                start_y - (row_counter * square_size),
                square_size/2
            )

            stddraw.show(5) # delay for animation (make 0 if none)
            x += square_size
            column_counter += 1
        row_counter += 1

    stddraw.show() # This will be removed in final submission
    # stddraw.save("QR-output.png") # This will be uncommented in final submission
    # =========================================================================================================


def add_dark_cell(qr_grid):
    """
    Changes value for dark cell to be at the hardcoded position. This position is always the same; the function is only applicable when in "real" mode.
    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # Values are hardcoded from specifications since only applicable with real QR code dimensions
    qr_grid[17][8] = 1
    

def add_timing_strips(qr_grid):
    """
    Adds two timing strips based on locations provided by Doc 3: QR Code specifications
    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    for i in range(8, 17):
        if i % 2 == 0:
            qr_grid[6][i] = 1
            qr_grid[i][6] = 1
        else:
            qr_grid[6][i] = 0
            qr_grid[i][6] = 0


def get_format_information_bits(qr_type, mask_pattern):
    '''Gets the 15-bit information vector specifying which graphical output,
    the QR type (snake or real), and the masking pattern will be used for the
    QR code generation.

    Parameters:
    ----------
    qr_type : str
        A string of length 2 comprising 0s or 1s specifying which of the
        following encoding rules will be used:
        | qr_type |  Type  |  Output  |
        |  '00'   |  Snake | Command-line |
        |  '01'   |  Real  | Command-line |
        |  '10'   |  Snake | Graphical|
        |  '11'   |  Real  | Graphical|
    masking_patter : str
        A string of length 3 comprising 0s or 1s encoding the masking pattern.
        For example, '000' specifies that 0 == 1 masking pattern will be used.

    Returns:
    -------
    list
        A list of length 15 containing the bits used for the format information
        regions of the real QR code.
        '''


def add_format_information_region(qr_grid, mask_pattern: int):
    """
    Adds the two format information regions based on the 15-bit vector generated by the project library function 
    Args:
        qr_grid (2D array of int): The data of the QR grid.
        mask_pattern (int): The mask pattern specified by the encoding parameter
    """
    pass


def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """


    stdio.write("\n")
    # print out values
    for row in qr_grid:
        for value in row:
            stdio.write(str(value) + " ")
        stdio.write("\n")  # Move to the next line after each row 


def make_position_pattern(pos_square_size):
    """
    Creates the position pattern of size pos_square_size and returning it as a
    2-dimensional array of int.

    Args:
        pos_square_size (int): The size of the position pattern to generate

    Returns:
        2D array of int: The position pattern
    """
   
   # Generate a p x p matrix containing all 1's
    pattern = stdarray.create2D(pos_square_size, pos_square_size, 1)

    if pos_square_size % 4 == 0:  # if p is a multiple of 4
        # Set rightmost and bottom values to 0
        for i in range(pos_square_size - 1):
            pattern[i][pos_square_size - 1] = 0
        for j in range(pos_square_size):
            pattern[pos_square_size - 1][j] = 0

        # Set inner values
        for i in range(pos_square_size - 1):
            for j in range(pos_square_size - 1):
                distance = min(i, j, pos_square_size - 2 - i, pos_square_size - 2 - j)
                if distance % 2 != 0:
                       pattern[i][j] = 0

        # Explicitly set the center of the constant 1 region to be 1
        middle = pos_square_size // 2  # integer division
        pattern[middle - 1][middle - 1] = 1
        
    else:  # if p is not a multiple of 4
        for i in range(pos_square_size - 1):
            for j in range(pos_square_size - 1):
                distance = min(i, j, pos_square_size - 2 - i, pos_square_size - 2 - j)
                if distance % 2 == 0:
                    pattern[i][j] = 0
            
        # Explicitly set the center of the constant 1 region to be 1
        middle = (pos_square_size // 2) - 1
        pattern[middle][middle] = 1
    
    return pattern
    

def make_alignment_pattern(align_square_size):
    """
    Creates the alignment pattern of size align_square_size and returning it as
    a 2-dimensional array of int.

    Args:
        align_square_size (int): The size of the alignment pattern to generate

    Returns:
        2D array of int: The alignment pattern
    """

    # Create an array of size a x a containing all 0's
    pattern = stdarray.create2D(align_square_size, align_square_size, 0)

    # Fill the pattern by determining the minimum distance from the edges
    for i in range(align_square_size):
        for j in range(align_square_size):
            layer = min(i, j, align_square_size - 1 - i, align_square_size - 1 - j)
            pattern[i][j] = 1 if layer % 2 == 0 else 0  # Alternating 1s and 0s
    
    return pattern


def rotate_pattern_clockwise(data):
    """
    Rotates the values in data clock-wise by 90 degrees

    Args:
        data (2D array of int): The array that should be rotated
    """
    p = len(data)
    for i in range(p):
        for j in range(i + 1, p):  # Avoid redundant swaps
            data[i][j], data[j][i] = data[j][i], data[i][j]  # Swap elements

    # Flip the transposed matrix about the vertical axis in place
    n = p - 1
    for row in range(p):
        for column in range(p // 2):
            data[row][column], data[row][n - column] = data[row][n - column], data[row][column]  # Swap elements
    

def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    """
    Places values contained in data to the qr_grid starting as positions given
    by achnor_x and anchor_y.

    Args:
        qr_grid (2D array of int): The QR grid
        anchor_x (int): the x position from where the data should be added
        anchor_y (int): the y position from where the data should be added
        data (2D array of int): The data that should be added to the QR grid
    """
    for y in range(anchor_y, anchor_y + len(data)): # rows
        for x in range(anchor_x, anchor_x + len(data)): # columns
            qr_grid[x][y] = data[x - anchor_x][y - anchor_y] 


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """

    MAX_ROWS = len(qr_grid)
    MAX_COLUMNS = MAX_ROWS
    payload_index = 0

    row = 0
    while row < MAX_ROWS:
        if row % 2 == 0:
            # Left to right
            col = 0
            while col < MAX_COLUMNS and payload_index < len(data):
                if (qr_grid[row][col] == "-"):
                    qr_grid[row][col] = int(data[payload_index])
                    payload_index += 1
                col += 1
        else:
            # Right to left
            col = MAX_COLUMNS - 1
            while col >= 0 and payload_index < len(data):
                if (qr_grid[row][col] == "-"):
                    qr_grid[row][col] = int(data[payload_index])
                    payload_index += 1
                col -= 1
        row += 1


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):
    """
    Applies the masking pattern specified by mask_id to the QR grid following
    the masking rules as specified by the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        reserved_positions (2D array of int): the reserved positions
        mask_id (str): The mask id to apply to the QR grid
    """

    # Define a dictionary with the corresponding conditions. The condition is selected via the base-10 value of the masking pattern
    mask_conditions = {
    0: lambda r, c: 1 == 0,
    1: lambda r, c: r % 2 == 0,
    2: lambda r, c: c % 3 == 0,
    3: lambda r, c: (r + c) % 3 == 0,
    4: lambda r, c: ((c // 3) + (r // 3)) % 2 == 0,
    5: lambda r, c: (r * c) % 2 + (r * c) % 3 == 0,
    6: lambda r, c: ((r * c) % 2 + (r * c) % 3) % 2 == 0,
    7: lambda r, c: ((r + c) % 2 + (r * c) % 3) % 2 == 0
}

    condition = mask_conditions.get(int(mask_id))
    if condition:
        for row in range(len(qr_grid)):
            for col in range(len(qr_grid)):
                if reserved_positions[row][col] != 'X' and condition(row, col):
                    # print("Changed row " + str(row) + " and column" + str(col))
                    temp = int(qr_grid[row][col])
                    temp ^= 1 # using XOR to flip the bit
                    qr_grid[row][col] = str(temp) 


def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    snake layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def get_error_codewords(message, num_err_words=16):
    '''Encode a list of integers using Reed - Solomon codes, a type of error correction code.

    Parameters:
    ----------
    message : list
        A list of integer representations of ASCII encodable decimal values.
    num_err_words : int
        The number of error correction codewords to generate.

    Returns:
    -------
    list
        A list of length 'num_err_words' containing the integer representations
        of the generated codewords generated for the 'message'.
'''


def build_payload(message, total_length):
    """
    Builds up the payload using the encoding info, message length, message codewords, termination pattern and padding bits
    
    Args:
        message:str: The message to be converted into the payload
        total_length:int: The number of bits to fill, based on available grid slots
    Returns:
        payload:list[int] The full payload to be added to the grid
    """
    # Fixed parts
    encoding = [0, 1, 0, 0] # Fixed
    message_length = len(message)
    message_length_bits = [int(b) for b in f"{message_length:08b}"]  # Convert length to 8-bit binary

    # Convert message to 8-bit ASCII
    codewords = []
    for char in message:
        codewords.extend([int(b) for b in f"{ord(char):08b}"])

    termination = [0, 0, 0, 0] # Fixed

    # Combine parts
    core_payload = encoding + message_length_bits + codewords + termination

    # Padding logic
    padding_bits = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    payload = core_payload[:] # Copies all items in core_payload into payload variable

    # Adds onto end of payload the required padding
    i = 0
    while len(payload) < total_length:
        payload.append(padding_bits[i % len(padding_bits)])
        i += 1

    return payload


def populate_aux_grid(aux_grid, original_grid):
    """
    Marks the positions on the auxiliary grid where there are reserved spots on the original grid

    Args:
        aux_grid: The blank auxliary grid
        original_grid: The grid containing the position and alignment squares
    Returns
        aux_grid:list[int] A new grid marking reserved spots with an X
        num_open_squares:int The number of non-reserved squaress
    """

    for row in range(len(aux_grid)):
        for col in range(len(aux_grid)):
            if (original_grid[row][col] != '-'):
                aux_grid[row][col] = 'X'
                
    return aux_grid


def main(args):
    # =========================================================================================================
    # Handling arguments
    # From here onwards, 'return' will terminate the program, since 'main' is the root function 

    for arg in args[1:]:
        if not(all('0' <= ch <= '9' for ch in arg)):
            return
        
    argument_size = len(args)

    if (argument_size < 5):
        print("ERROR: Too few arguments")
        return
    elif (argument_size > 5):
        print("ERROR: Too many arguments")
        return

    # TODO: Manually implement the strip function since it is not allowed in submission
    message_received = sys.stdin.read().strip() # strip() removes whitespace and newline characters, read() reads entire line


    encoding_param = int(args[1])
    if (not encoding_param in range(0, 32)):
        print("ERROR: Invalid encoding argument:", encoding_param)
        return
    

    gui_mode = (encoding_param >> 4) & 0b1 
    # ALTERNATE METHOD FOR DOING THIS - gives same result :) 
    # gui_mode = (encoding_param & 0b10000) >= 16
    real_mode = (encoding_param >> 3) & 0b1  # returns '0' if snake mode and '1' if real mode

    if (real_mode == 1 or gui_mode == 1):
        grid_size_param : int = 25
        position_pattern_size_param : int = 8
        alignment_pattern_size_param : int = 5
    else:
        grid_size_param = int(args[2])
        position_pattern_size_param = int(args[3])
        alignment_pattern_size_param = int(args[4])
    
    mask_pattern = encoding_param & 0b111  # ANDing with 1 copies that bit 
    

    # Checks if inputs is a number within the correct range and also not a letter
    if (not(all('0' <= ch <= '9' for ch in args[2]))) or (not grid_size_param in range(10, 49)):
        print("ERROR: Invalid size argument:", args[2])
        return
    if (not(all('0' <= ch <= '9' for ch in args[3]))) and not (position_pattern_size_param > 3 and position_pattern_size_param % 2 == 0):
        print("ERROR: Invalid position pattern size argument:", position_pattern_size_param)
        return
    if (not(all('0' <= ch <= '9' for ch in args[4]))) and not ((alignment_pattern_size_param > 0) and (alignment_pattern_size_param-1) % 4 == 0):
        print("ERROR: Invalid alignment pattern size argument:", alignment_pattern_size_param)
        return
    
    
    # TODO: Find and apply fixes based on feedback given
    alignment_anchor = (grid_size_param - position_pattern_size_param - 1) # n-p-1
    condition_a = position_pattern_size_param + alignment_pattern_size_param > grid_size_param
    condition_b = (alignment_pattern_size_param) > abs(grid_size_param - alignment_anchor)
    # print(condition_a)
    # print(condition_b)     
    if (condition_a or condition_b):
        print("ERROR: Alignment/position pattern out of bounds")
        return

    # Checking payload error condition
    # n^2 - (3p^2 + a^2), assuming here only position patterns and alignment patterns are placed
    available_spots = pow(grid_size_param, 2) - (3*pow(position_pattern_size_param, 2) + pow(alignment_pattern_size_param, 2))
    payload = build_payload(message_received, available_spots)

    if (len(payload) > available_spots):
        print("ERROR: Payload too large")
        return

    # =========================================================================================================


    
    # =========================================================================================================
    # Calling the respective functions

    # Create clean grid(s) initialised with '-' characters
    grid = stdarray.create2D(grid_size_param, grid_size_param, '-')
    aux_grid = stdarray.create2D(grid_size_param, grid_size_param, '-')
    # print_qr_grid(grid)
    
    # Create top-left position pattern and add to corner
    position_pattern_nw = make_position_pattern(position_pattern_size_param) # North-West corner - original
    add_data_at_anchor(grid, 0, 0, position_pattern_nw)
    # print_qr_grid(grid)

    # Create top-right position pattern by rotating and place it on grid
    rotate_pattern_clockwise(position_pattern_nw) 
    pos = (grid_size_param - position_pattern_size_param) 
    add_data_at_anchor(grid, 0, pos, position_pattern_nw)
    # print_qr_grid(grid)


    # Create the bottom-left position pattern by rotating and placing on grid
    rotate_pattern_clockwise(position_pattern_nw)
    rotate_pattern_clockwise(position_pattern_nw)
    add_data_at_anchor(grid, pos, 0, position_pattern_nw)
    # print_qr_grid(grid)
    
    # Create alignment pattern and place on grid
    alignment_pattern = make_alignment_pattern(alignment_pattern_size_param)
    add_data_at_anchor(grid, alignment_anchor, alignment_anchor, alignment_pattern)
    # print_qr_grid(grid)

    # Create auxliary grid: Provides reserved positions
    aux_grid = populate_aux_grid(aux_grid, grid)
    
    if (real_mode == 0):
        add_data_snake(grid, payload)
        apply_mask(grid, aux_grid, mask_pattern)
        print_qr_grid(grid)
    else: 
        add_dark_cell(grid) 
        add_timing_strips(grid)
        add_format_information_region(grid, mask_pattern)
        apply_mask(grid, aux_grid, mask_pattern)
        print_qr_grid(grid)
        draw_qr_grid(grid)

    # =========================================================================================================



if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)

