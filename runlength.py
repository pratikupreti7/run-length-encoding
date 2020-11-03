def encoding():
    with open('input', 'r') as file:
        string = file.read().strip('\n')
    ans = []
    count = 1
    if len(string) == 0:
        print('Please enter Something')

    else:
        for i in range(len(string)):

            if i == len(string) - 1:
                ans.append([string[i], count])
            elif string[i] == string[i + 1]:
                count += 1

            else:
                ans.append([string[i], count])
                count = 1
        for i in ans:
            output = open("output", 'a')
            print(i[0] + str(i[1]), file=output, end='')


def decoding():
    newstring=''
    with open('output', 'r') as file:
        output = file.read()
    print("Entered string in output file is:")
    print(output)
    if len(output)==0:
        print("Please Enter Something")
    else:
        for i in range(0,len(output),2):
            ch=output[i]
            num=int(output[i+1])
            newstring=newstring+ch*num
    print("After Decoding String is :")
    print(newstring)



print(
    """
    Choose from the following:
    1.Encoding
    2.Decoding 
    
    """
)
choice=int(input("Enter your choice:"))
options=[encoding,decoding]
options[choice-1]()






