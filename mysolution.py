import os
# print(dir(os))
# path: /Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python

# os.chdir('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python')
# print(os.getcwd())
# print(os.listdir())


import os
# create the CyberSecurity Notes folder and also set it to a variable called notes_folder


def main():
    notes_folder = os.mkdir('CyberSecurity-Notes')
    # create a for loop to create the weekly folders in a range
    # remember that a range will start at the first argument in the function but will stop right before the second argument, so you must set the range from 1 to 25 in order for it to make folders with the numbers 1 through 24
    for x in range(1, 25):
        # use the mkdir() function to create a folder for each week
        # mkdir() will only work if the notes_folder 'CyberSecurity-Notes' already exists
        # use concatenation (+) to add the variable x which will increase by 1 each time in the for loop
        # use the str() function to turn the integer into a string
        os.mkdir('CyberSecurity-Notes/Week-' + str(x))
        # remember that a range will start at the first argument in the function but will stop right before the second argument, so you must set the range from 1 to 4 in order to have a folder create for days 1 through 4
        for y in range(1, 4):
            # use concatenation (+) to add the variable y which will increase by 1 each time in the for loop
            # use the str() function to turn the integer into a string
            os.mkdir('CyberSecurity-Notes/Week-' + str(x) + '/Day-' + str(y))


main()
