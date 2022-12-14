import os
import functions
from callback import input_callback

def main():
    login = input_callback('login')

    functions.auth(int(login))

if __name__ == "__main__":
    main()