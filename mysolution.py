import os
# print(dir(os))
# path: /Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python

# os.chdir('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python')
# print(os.getcwd())
# print(os.listdir())


def main():
    # create CyberSecurity-Notes directory
    # os.mkdir('CyberSecurity-Notes')
    root_path = '/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'
    for root, dirs, files in os.walk('/Users/rebeccabartels/cyber-homework/Unit 4 Advanced Python/HW04-Python'):
        #    print("****************")
        #    print("You have " + str(x) + " directories here.")
        #    break
        # if x == 24:
        #    isTrue = True
        #    print("Your files have been created.")
        #    print("****************")
        #    if len(os.listdir(root_path)) == 0:
        #        print("Directory is empty")
        #    else:
        #        print("Directory is complete")

        # else:
        #    print("Let's get started...")
        for i in range(1, 25):
            #os.makedirs("Week %d\r\n" % (i+1))
            for dir in dirs:
                for j in range(3):
                    os.makedirs("Week " + str(i) + "/Day- %d\r\n" % (j+1))


main()
