#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program tells the user a month by number


def main():
    # This function determines month from its number value

    # Input
    month_number = int(input("Enter the number of a month: "))

    # Process and Output
    if month_number == 1:
        print("\nJanuary")
    elif month_number == 2:
        print("\nFebruary")
    elif month_number == 3:
        print("\nMarch")
    elif month_number == 4:
        print("\nApril")
    elif month_number == 5:
        print("\nMay")
    elif month_number == 6:
        print("\nJune")
    elif month_number == 7:
        print("\nJuly")
    elif month_number == 8:
        print("\nAugust")
    elif month_number == 9:
        print("\nSeptember")
    elif month_number == 10:
        print("\nOctober")
    elif month_number == 11:
        print("\nNovember")
    elif month_number == 12:
        print("\nDecember")
    print("\nDone.")


if __name__ == "__main__":
    main()
