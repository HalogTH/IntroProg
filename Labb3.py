<<<<<<< HEAD
def menuPromt():
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit programy")
    return input("Choose alternative: ")

def ordLista1():
    words = []
    desc  = []
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")
            if(word in words):
                print("word already in dictionary!")
            else:
                words.append( word )
                desc.append ( input("Description of word: ") )
                
            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            if(word in words):
                print( desc[words.index(word)] )
            else:
                print("Word not found")

                
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()



def ordLista2():
    words = []
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")

            #finns inga ord, bara å lägga till
            if len(words) == 0:
                    desc = input("Description of word: ")
                    words.append( (word, desc) )
            else:
                #kollar om ordet finns
                for i in words:
                    if i[0] == word:
                        print("word already in dictionary!")
                        break
                    elif words.index(i) == len(words) - 1: #kollar om loopen är slut. 
                        desc = input("Description of word: ")
                        words.append( (word, desc) )
                        break #annars kör loopen igen för att words blir en större

            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            for i in words:
                if(i[0] == word):
                    print(i[1])
                    break
                elif(words.index(i) == len(words) - 1): #i = tupeln. index(i) = positionen
                    print("Word not found")

            
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()


def ordLista3():
    dic = {}
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")
            if(word in dic):
                print("word already in dictionary!")
            else:
                dic[word] = input("Description of word: ")

            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            if(word in dic):
                print( dic[word] )
            else:
                print("Word not found")

                
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()
    
=======
def menuPromt():
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit programy")
    return input("Choose alternative: ")

def ordLista1():
    words = []
    desc  = []
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")
            if(word in words):
                print("word already in dictionary!")
            else:
                words.append( word )
                desc.append ( input("Description of word: ") )
            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            if(word in words):
                print( desc[words.index(word)] )
            else:
                print("Word not found")
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()



def ordLista2():
    words = []
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")
            desc = input("Description of word: ")
            if((word, desc) in words):
                print("word already in dictionary!")
            else:
                words.append( (word, desc) )
            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            for i in words:
                if(i[0] == word):
                    print(i[1])
                elif(words.index(i) == len(words) - 1): #kollar om loopen är slut
                    print("Word not found")
            
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()


def ordLista3():
    dic = {}
    i = menuPromt()

    while(i != "3"):
        print("")

        if(i == "1"): #insert
            word = input("Word to insert: ")
            if(word in dic):
                print("word already in dictionary!")
            else:
                dic[word] = input("Description of word: ")
            
        elif(i == "2"): #lookup
            word = input("Word to lookup: ")
            if(word in dic):
                print( dic[word] )
            else:
                print("Word not found")
        else:
            print("Unknown command, please try again.","")
            ordLista1()

        print("","")
        i = menuPromt()
    
>>>>>>> db010d28339c9f5467a16f41c9e81c79d7bf28f6