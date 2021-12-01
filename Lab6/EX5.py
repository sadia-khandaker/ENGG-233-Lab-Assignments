import random

def main():
    counter = 0
    
    while counter < 10:
        x = random.random()
        y = random.uniform(1, 100)
        z = random.randint(1, 100)
        print("The three random numbers generated are: ",x,y,z)
        if (is_different(x,y,z)):
            print_result(min_of_three(x,y,z),max_of_three(x,y,z))
        else:
            print("The three numbers are the same")
        counter += 1

def is_different(x,y,z):
    different = True
    if ((x==y) and (y==z)):
        different = False
    return different

def max_of_three(x,y,z):
    first_max = greater_of_two(x,y)
    total_max = greater_of_two(first_max,z)
    return total_max

def greater_of_two(x,y):
    if (x>y):
        return x
    else:
        return y

def min_of_three(x,y,z):
    first_min = smaller_of_two(x,y)
    total_min = smaller_of_two(first_min,z)
    return total_min

def smaller_of_two(x,y):
    if (x<y):
        return x
    else:
        return y

def print_result(a,b):
    print('Max and Min are: {} {}'.format(b,a))
    
if __name__ == '__main__':
    main()