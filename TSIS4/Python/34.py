def result(N):


    for num in range(N):


            if num % 3 == 0 and num % 4 == 0:

                print(str(num) + " ", end = "")


            else:

                pass

if __name__ == "__main__":

    N = 100

    result(N)
