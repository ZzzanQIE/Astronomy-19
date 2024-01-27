import numpy as np
from tabulate import tabulate

def sin_table():
    x = np.linspace(0,2*np.pi,1000,dtype=float)
    y = np.sin(x)
    table_data = [(a,b) for a,b in zip(x,y)]
    table_headers = ['x','sin(x)']
    print(tabulate(table_data,tablefmt="grid",headers=table_headers,floatfmt=".3f"))

def main():
    sin_table()

if __name__ == "__main__":
    main()