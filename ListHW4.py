#Function test whether values have been added to the list.


myUniqueList = []
hobby1 = "reading"
hobby2 = "writing"
hobby3 = "hiking"
hobby4 = "music"
def MyHobbies(hobby):

    if hobby1 not in myUniqueList:
        myUniqueList.append(hobby1)

    if hobby2 not in myUniqueList:
        myUniqueList.append(hobby2)

    if hobby3 not in myUniqueList:
        myUniqueList.append(hobby3)

    if hobby4 not in myUniqueList:
        myUniqueList.append(hobby4)
        print("This is a short list of my hobbies:", hobby)
        return True

    else:
        return False


MyHobbies(myUniqueList)
