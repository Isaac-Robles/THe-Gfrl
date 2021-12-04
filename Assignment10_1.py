#Assignment 10.1: Your Own Class, Demo Program
#hey

#imports time module
import time

#Creates the class based off of the real world videogame console the Nintendo DSI Lite
class DSIlite():
    #creates 2 class variables, the battery life of the dsi, being 10 hours, and the block of memory storage on the console, being 200
    batterylife = 10
    stoargeblocks = 200
    #init method takes in 2 arguements, the color of the console and the game inserted into it, which is defaulted to None
    def __init__(self, color, gamein=None,):
        self.__gamein = gamein
        self.__color = color

    #set method for the gamein variable
    def set_gamein(self, gamein):
        #sets the gamein variable only if gamein is a string or None
        if type(gamein) == "str":
            self.__gamein = gamein
        elif type(gamein) == "NoneType":
            self.__gamein = gamein
        #if gamein arguement isnt either of these it prints an error message and raises a value error
        else:
            print("This is not a game title.")
            raise ValueError

    #get method for gamein variable
    def get_gamein(self):
        return self.__gamein

    #set method for color variable
    def set_color(self, color):
        #if the color is one of the 4 colors the DSI comes in, blue, pink, black, or white then it sets the color variable
        if color == "Blue":
            self.__color = color
        elif color == "Black":
            self.__color = color
        elif color == "White":
            self.__color = color
        elif color == "Pink":
            self.__color = color
        #if the color arguement is not one of these colors it prints an error message and returns a value error
        else:
            print("The DSIlite is not available in this color.")
            raise ValueError

    #get method for color variable
    def get_color(self):
        return self.__color

    #returns the battery life of the dsi
    def get_battery(self):
        return (f"You have {self.batterylife} of battery life left.")

    #simulates the battery life used when playing a game for a certain amount of hours
    def play_game(self):
        #asks how many hours the game inserted was played for
        play_time = input(f"Enter how many hours you played {self.__gamein} DSI for. ")
        #intializes a counter
        self.__count = 0
        #iterates through the range from 1 to the amount of hours played
        for i in range(1, int(play_time) + 1):
            #for every hour played it adds one to the count
            self.__count += 1
        #sets the new battery life equal to the battery life minus the count
        self.batterylife = self.batterylife - self.__count
        return self.batterylife

    #charges the battery life to full power
    def charge(self):
        #uses the time sleep function to simulate the time it would take to charge
        print("Charging...")
        time.sleep(5)
        #sets the battery life back to its original value
        self.batterylife = 10
        return("Fully charged!")


#main function
def main():
    childhoodDS = DSIlite("Blue", "Mario Kart DS")
    childhoodDS.play_game()
    print(childhoodDS.get_battery())
    print(childhoodDS.charge())
    print(childhoodDS.get_battery())

#runs code
if __name__ == "__main__":
    main()