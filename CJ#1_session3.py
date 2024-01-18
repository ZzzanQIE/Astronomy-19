def special_function(x):
    return x**3+8

def main():
    i = special_function(9)
    print("the result is:",i)
    if i > 27:
        print('YAY!')

if __name__ == "__main__":
    main()