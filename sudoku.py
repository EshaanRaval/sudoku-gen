from ortools.sat.python import cp_model
import numpy as np
import pandas as pd

def sudoku(size):
    model = cp_model.CpModel()
    sudoku = {}
    for i in range(size):
        for j in range(size):
            sudoku[(i,j)] = model.new_int_var(1, size, f"({i},{j})")
    
    
    for i in range(size):
        model.AddAllDifferent([sudoku[(i,j)] for j in range(size)])
        model.AddAllDifferent([sudoku[(j,i)] for j in range(size)])  # for columns


    # Create a solver and solve the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    print(sudoku)

    # Display the solution.
    if status == cp_model.OPTIMAL: # or status == cp_model.FEASIBLE:
        
        print(f"Solution found: {status}")
        smatrix = np.zeros((size, size), dtype = np.int8)
    
        for entries, value in sudoku.items():
            smatrix[entries] = solver.Value(value)
        data = pd.DataFrame(smatrix)
        data.to_excel("matrix.xlsx")
        print(smatrix)        

    else:
        print("No solution found.")

def randomizer(sudoku):
    # can switch around rows 
    print("WIP")
    # can switch around columns

    # can rotate

    # 


sudoku(120)
