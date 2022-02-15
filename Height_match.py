import requests
import json

"""This project searches through NBA player heights
based on user input. The raw data is taken from (https://www.openintro.org/data/index.php?data=nba_heights).  The data is
served in json format by the endpoint (https://mach-eight.uc.r.appspot.com/).

Takes a single integer input. The application will download the raw data from the website above
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players
whose height in inches adds up to the integer input to the application. If no
matches are found, the application will print "No matches found" """

def Faulhaber(list_len:int,num:int = 0)->int: #This function returns the number of iterations for compare all the heigths. Is based on the Faulhaber funtion

    if num == list_len-1: #It doesn't take the last number in account
        return num

    return num + Faulhaber(list_len,num + 1)

def SumHeight(number:int, list_players:list, limit:int): #This function compares the height of the player n with the players n+1 to the last one

    count, i, y, couples= 0, 0, 1, 0 
    
    #The count is the variable that grous until the last iteration number
    #i is the index in the list for player n
    #y is the index of the other players n+1 ... to the last one
    #couples is the number of heights that match with user input

    while count <limit:

        count+=1

        if int(list_players[i]["h_in"]) + int(list_players[y]["h_in"]) == number:

            couples +=1
            print(list_players[i]["first_name"]+" "+list_players[i]["last_name"]+"          "+list_players[y]["first_name"]+" "+list_players[y]["last_name"]) #primt the heigth match
        
        if y >= len(list_players)-1 : #When all players height are compared to the n player. It continues with the n+1

            i+=1
            y=i+1
            
        else:

            y+=1
    
    if couples == 0: #if no couples were find, then appears the message "No matches found" 

        print("No matches found")
 
if __name__=="__main__":

    try:
        answer=int(input("Enter the sum of the heights: "))

        if answer < 0: #Check if the input is a positive integer
            raise ValueError()

        request=requests.get("https://mach-eight.uc.r.appspot.com/") #get the json from the url
        list_players = json.loads(request.content) 
        limit = Faulhaber(len(list_players["values"])) #get the limit of iterations
        SumHeight(answer, list_players["values"],limit)

    except ValueError:
        print("Only positive integers are allowed")



