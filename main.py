# This is a sample Python script.
import dir
import undir
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adju = [ [1,2,3],
        [3,0,2],
        [1,0,3],
        [1,0,2] ]
    adj1 = [[1, 2],
           [3, 3],
           [1, 0],
           [0, 2]]
    adj2 = [ [], [0], [3], [1] ]
    print(undir.euler(adju))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
