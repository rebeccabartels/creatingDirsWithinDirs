import os
# print(dir(os))
# path: /Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python

# os.chdir('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python')
# print(os.getcwd())
# print(os.listdir())


def main():
    count = 0
    # create CyberSecurity-Notes directory
    # os.mkdir('CyberSecurity-Notes')
    root_path = '/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'
    folders = ['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12',
               'Week13', 'Week14', 'Week15', 'Week16', 'Week17', 'Week18', 'Week19', 'Week20', 'Week21', 'Week22', 'Week23', 'Week24']
    for root, dirs, files in os.walk('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'):
        print("hello")
        for f in folders:
            if count < 23:
                os.mkdir('Day1')
                os.mkdir('Day2')
                os.mkdir('Day3')
                count += 1


main()
