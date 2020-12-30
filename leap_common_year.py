# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a leap/common year


def main():
    # this function tells the user if the yaer is a leao or common

    # input
    year = input("Enter a year: ")

    # process
    try:
        year = int(year)
        if (year % 4) != 0:
            print("This is not a leap year")
        elif (year % 100) != 0:
            print("This is a leap year")
        elif (year % 400) != 0:
            print("This is not a leap year")
        else:
            print("This is a leap year")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
