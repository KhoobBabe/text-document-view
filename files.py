#only shows the file in reading mode
def read_file():
    file = open("text.txt", mode = "r")
    data = file.read()
    print()
    print(data)
    print()

    file.close()

#shows statistics
def show_stats():
    file = open("text.txt", mode = "r")
    data = file.read()
    words = data.split()
    print()
    #shows the number of words
    print("The number of words are: ", len(words))

    sentences = data.split('. ')
    #shows the number of sentences
    print("The number of senteces are: ", len(sentences))

    file.close()

#shows the frequency of the words which the user enters in the text file 
def show_ex():
    #input
    string=input("Enter a sentence: ")

    freq_dict={}

    temp_str=string.split()
    
    for i in temp_str:
        file=open("text.txt")
        data=file.read()
        file_data=data.split()
        freq=0

        for words in file_data:
            if i.upper()==words.upper():
                freq += 1
        file.close()

        freq_dict[i]=freq
        
   #sorts in ascending order
    sorted_dict=sorted(freq_dict.items(),key=lambda x:x[1])
    print("Word\t\tFrequency")
    file=open("new_file","w")
    file.write("Word\t\tFrequency\n")

    
    for key,value in sorted_dict:
        file.write(f"{key}\t\t{value}\n")
        print(f"{key}\t\t{value}")

    file.close()

opt = ''
while opt != 0:
    #options are given
    print("current file is text")
    print()
    print("select from the following optons:-\n")
    print("a. read file")
    print("b. show statistics")
    print("c. show and export")
    print("d. exit")
    opt = input("Enter your option: ")
    if opt == "a":
        read_file()
    elif opt == "b":
        show_stats()
    elif opt == "c":
        show_ex()
    elif opt == "d":
        print("program closed")
        break
