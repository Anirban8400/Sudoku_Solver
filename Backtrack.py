

import numpy as np
from copy import deepcopy


def solve_sudoku(digits_grid):
    """
    Solves a sudoku puzzle.
    
    :param digits_grid: 2D numpy array of shape (9,9). 0 means empty.
    :return: Solved grid or None if unsolvable / ambiguous.
    """
    if not is_solvable(digits_grid):
        return None

    digits_grid = deepcopy(digits_grid)
    human_notes = get_full_human_notes(digits_grid)

    while True:
        changed1 = remove_orphans_technique(digits_grid, human_notes)
        changed2 = single_appearances_technique(digits_grid, human_notes)
        if not changed1 and not changed2:
            break

    return digits_grid if is_solved_correctly(digits_grid) else None


def is_solvable(digits_grid):
    for y in range(9):
        for x in range(9):
            if digits_grid[y, x]:
                if not (check_row(x, y, digits_grid) and
                        check_col(x, y, digits_grid) and
                        check_square(x, y, digits_grid)):
                    return False
    return True


def check_row(x, y, digits_grid):
    return np.count_nonzero(digits_grid[y, :] == digits_grid[y, x]) == 1


def check_col(x, y, digits_grid):
    return np.count_nonzero(digits_grid[:, x] == digits_grid[y, x]) == 1


def check_square(x, y, digits_grid):
    x0, y0 = (x // 3) * 3, (y // 3) * 3
    square = digits_grid[y0:y0+3, x0:x0+3]
    return np.count_nonzero(square == digits_grid[y, x]) == 1


def get_full_human_notes(digits_grid):
    notes = np.empty((9, 9), dtype=object)
    for y in range(9):
        for x in range(9):
            if digits_grid[y, x] == 0:
                notes[y, x] = find_all_candidates(digits_grid, x, y)
            else:
                notes[y, x] = set()
    return notes


def find_all_candidates(digits_grid, x, y):
    candidates = set()
    for digit in range(1, 10):
        if (fits_in_row(digits_grid, y, digit) and
            fits_in_col(digits_grid, x, digit) and
            fits_in_square(digits_grid, x // 3, y // 3, digit)):
            candidates.add(digit)
    return candidates


def fits_in_row(digits_grid, y, digit):
    return digit not in digits_grid[y, :]


def fits_in_col(digits_grid, x, digit):
    return digit not in digits_grid[:, x]


def fits_in_square(digits_grid, x_square, y_square, digit):
    square = digits_grid[y_square * 3 : y_square * 3 + 3, x_square * 3 : x_square * 3 + 3]
    return digit not in square


def remove_orphans_technique(digits_grid, human_notes):
    changed = False
    for y in range(9):
        for x in range(9):
            if len(human_notes[y, x]) == 1:
                digit = next(iter(human_notes[y, x]))
                digits_grid[y, x] = digit
                human_notes[y, x] = set()
                implications_of_removing_an_orphan(human_notes, x, y, digit)
                changed = True
    return changed


def implications_of_removing_an_orphan(notes, x, y, digit):
    for i in range(9):
        notes[y, i].discard(digit)
        notes[i, x].discard(digit)

    x0, y0 = (x // 3) * 3, (y // 3) * 3
    for dy in range(3):
        for dx in range(3):
            notes[y0 + dy, x0 + dx].discard(digit)


def single_appearances_technique(digits_grid, human_notes):
    changed = False

    # rows
    for y in range(9):
        changed |= single_appearance_axis(digits_grid, human_notes, y, axis="row")

    # columns
    for x in range(9):
        changed |= single_appearance_axis(digits_grid, human_notes, x, axis="col")

    # 3x3 boxes
    for box_y in range(3):
        for box_x in range(3):
            changed |= single_appearance_box(digits_grid, human_notes, box_x, box_y)

    return changed


def single_appearance_axis(digits_grid, human_notes, index, axis="row"):
    changed = False
    for digit in range(1, 10):
        appearances = []
        for i in range(9):
            x, y = (i, index) if axis == "row" else (index, i)
            if digit in human_notes[y, x]:
                appearances.append((y, x))
                if len(appearances) > 1:
                    break
        if len(appearances) == 1:
            y, x = appearances[0]
            digits_grid[y, x] = digit
            human_notes[y, x] = set()
            implications_of_removing_an_orphan(human_notes, x, y, digit)
            changed = True
    return changed


def single_appearance_box(digits_grid, human_notes, box_x, box_y):
    changed = False
    for digit in range(1, 10):
        appearances = []
        for dy in range(3):
            for dx in range(3):
                y = box_y * 3 + dy
                x = box_x * 3 + dx
                if digit in human_notes[y, x]:
                    appearances.append((y, x))
                    if len(appearances) > 1:
                        break
        if len(appearances) == 1:
            y, x = appearances[0]
            digits_grid[y, x] = digit
            human_notes[y, x] = set()
            implications_of_removing_an_orphan(human_notes, x, y, digit)
            changed = True
    return changed


def is_solved_correctly(digits_grid):
    if np.any(digits_grid == 0):
        return False
    return is_solvable(digits_grid)
