
# Day Trip Genertor

import random



print ('Hello and Welcome to Day Trip Tours! Let us help you find your perfect vacation. Would you like to go to the following destination? :' )


destination_cities = ['Eugene, OR','Los Angeles, CA','Sacramento, CA', 'Los Angeles, CA']
restaurant= ['The Vintage', 'Lion and Owl', 'Cornucopia Restaurant']
transportaton_mode= ['Rental Car','Uber/Lyft','Taxi']
entertainment= ['Attend football game', 'Take a bike tour on the river','Take Brewary Tour']

def get_destination():
    # randomly generate destination for user
    result= random.choice (destination_cities)
    # print result
    print(result)
    # ask user if they like it
    answer = input(' Type y/n:  ')
    # if they do like it, this function is done and needs to to transportation
    if answer == 'y':
        print( 'Great! We have your destination chosen. What would you like your mode of transportation to be?')     
    # if not, generate choice again 

    elif answer == 'n':
            result= random.choice (destination_cities)
            print(result) 
            answer =input(" I am sorry that wasn't the destination you were hoping to visit. Do you like this destination choice better? Type y/n ")
    answer='n'
    while answer=='n':
        result= random.choice (destination_cities)
        print(result) 
        answer =input(" I am sorry that wasn't the destination you were hoping to visit. Do you like this destination choice better? Type y/n ")
    else:
        print( 'Great! We have your destination chosen. What would you like your mode of transportation to be?') 

get_destination()  



# have user choose ofrm of transportion      
def get_transprotation ():
# randomly generate restaurant for user
    result= random.choice (transportaton_mode)
    # print result
    print(result)
    # ask user if they like it
    answer = input('Do you like this mode of transportation? Type y/n:  ')
    # if they do like it, this function is done and needs user needs to chice of entertainment
    if answer == 'y':
       print('Wonderful! Glad we could find you and your party a mode of transportation. Would you like to eat at the following restaurant choice?' )
       
           # if not, generate choice again

    elif answer == 'n':
        result= random.choice (transportaton_mode)
        print(result) 
        answer = input("I am so sorry you didn't like the last transportation choice? Do you prefer this mode of trasportation?  Type y/n: ")
    answer='n'
    while answer=='n':
        result= random.choice (transportaton_mode)
        print(result) 
        answer =input("I am so sorry you didn't like the last transportation choice? Do you prefer this mode of trasportation?  Type y/n: ")
    else:
         print ('Wonderful! Glad we could find you and your party a mode of transportation. Would you like to eat at the following restaurant choice?' )

    
get_transprotation()

#have the user choose a restaurant
def get_restaurant ():
    # randomly generate restaurant for user
    result= random.choice (restaurant)
    # print result
    print(result)
    # ask user if they like it
    answer = input('Do you like this restaurant choice? Type y/n:  ')
    # if they do like it, this function is done and needs user needs to choice entertainment
    if answer == 'y':
        print ('Fabulous, one of my favorites.  What type of entertainment activity would you like do?' )
    # if not, generate choice again

    elif answer == 'n':
        result= random.choice (restaurant)
        print(result) 
        answer = input("I am so sorry you didn't like the last restaurant choice? Do you prefer this establishment?  Type y/n: ")
    while answer=='n':
        result= random.choice (restaurant)
        print(result) 
        answer =input("I am so sorry you didn't like the last restaurant choice? Do you prefer this establishment?  Type y/n: ")
    else:
         print ('Fabulous, one of my favorites.  What type of entertainment activity would you like do?' )


get_restaurant()



# have user choose entertainment     
def get_entertainment ():
# randomly generate restaurant for user
    result= random.choice (entertainment)
    # print result
    print(result)
    # ask user if they like it
    answer = input(' choice? Type y/n:  ')
    # if they do like it, this function is done and needs user needs to chice of entertainment
    if answer == 'y':
        print ("Congrats! We have completed generating your day trip.  Now, let's confirm this is the trip you wanted." )
    # if not, generate choice again

    elif answer == 'n':
        result= random.choice (entertainment)
        print(result) 
        answer = input("Do you perfer this activity better?   Type y/n: ")
    while answer=='n':
        result= random.choice (entertainment)
        print(result) 
        answer =input("Do you perfer this activity better?   Type y/n: ")
    else:
         print ("Congratualtions! We have your day trip scheduled. Let's confirm this is the trip you expect" )


get_entertainment()        

# confirmation of the trip choices with the user
print('The trip we have generated for you is as follows:')
 

def trip_itenery():
    
    print(' destination is: ')
    result= destination_cities
    


