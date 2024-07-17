
def chewbacca():

    n = input()

    final = ""

    for i in range(len(n)):
        if i == 0 and n[0] == "9":
            final += "9"

        elif (9-int(n[i]) < int(n[i])):
            x = 9 - int(n[i])
            final += str(x)

        else:
            final += n[i]        
            
    return final


print(chewbacca())