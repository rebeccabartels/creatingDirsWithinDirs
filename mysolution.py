import os
# print(dir(os))
# path: /Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python

# os.chdir('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python')
# print(os.getcwd())
# print(os.listdir())


def main():
    count = range(1, 25)
    # create CyberSecurity-Notes directory
    # os.mkdir('CyberSecurity-Notes')
    root_path = '/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'
    for root, dirs, files in os.walk('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'):
        x = len(count)
        print("You have " + str(x) + " directories here.")
        break
        if x == 24:
            isTrue = True
            print("Your files have been created.")
            # if isTrue == True:
            # for root, dirs, files in os.walk(root_path):
            # print(dirs)
            # print(files)

        else:
            print("Let's get started...")
            for i in range(24):
                os.makedirs("Week %d\r\n" % (i+1))


main()
