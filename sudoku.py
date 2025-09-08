from ortools.sat.python import cp_model
import numpy as np
import pandas as pd
links = """https://www.sudokuwiki.org/sudoku.htm
https://www.thonky.com/sudoku/
https://sudoku.com/
https://en.wikipedia.org/wiki/Sudoku_..."""
def issqrt(value):
    root = np.sqrt(value)
    if int(root) == root:
        print(value)
        return True
    else:
        return False
def getsubgrid(size):
    root = int(np.sqrt(size))
    #3rd try just try to get the topmost points for all individual subgrid
    grid_points = []
    for i in range(root):
        for j in range(root):
            grid_points.append((i*root,j*root))
    
    sub_grids = {}
    for points in grid_points:
        a = points[0]
        b = points[1]
        coords = []
        for i in range(root):
            for j in range(root):
                coords.append((a+i,b+j)) # had to draw a physical grid to figure this out

        sub_grids[points] = coords
    return sub_grids


def sudoku(size):
    sub_squares = issqrt(size)
    model = cp_model.CpModel()
    sudoku = {}
    for i in range(size):
        for j in range(size):
            sudoku[(i,j)] = model.new_int_var(1, size, f"({i},{j})")
    
    
    for i in range(size):
        model.AddAllDifferent([sudoku[(i,j)] for j in range(size)])
        model.AddAllDifferent([sudoku[(j,i)] for j in range(size)])  # for columns
    
    if sub_squares:
        # we add an additional requirement that all numbers be used within this square once # for proper sudoku thingy
        grids = getsubgrid(size)
        for grid in grids.values():
            model.AddAllDifferent(list(sudoku[points] for points in grid))
    # Create a solver and solve the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    #print(sudoku, "this")

    # Display the solution.
    if status == cp_model.OPTIMAL: # or status == cp_model.FEASIBLE:
        
        print("Solution found:")
        smatrix = np.zeros((size, size), dtype = np.int8)
    
        for entries, value in sudoku.items():
            smatrix[entries] = solver.Value(value)
        #data = pd.DataFrame(smatrix)
        #data.to_excel("matrix.xlsx")
        print(smatrix)        

    else:
        print("No solution found.")

def randomizer(sudoku):
    # can switch around rows 
    print("WIP")
    # can switch around columns

    # can rotate

    # 


sudoku(9)
