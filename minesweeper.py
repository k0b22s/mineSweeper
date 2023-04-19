#create mine-grid
minesweeper = [
     ["#","-","#","-","-"],
     ["-","#","#","-","-"],
     ["-","-","-","-","#"],
     ["-","#","#","-","-"],
     ["-","-","#","-","#"],
 ]


#get user input on coordinates and provide descriptive print statement
print("Please enter your coordinates below: ")
lat = int(input("Latitude here (max 3): "))  # fix typo, change max to 3
long = int(input("Longitude here (max 3): "))  # change max to 3

#Check if input is on grid
if lat >= 5 or long >= 5 or lat < 0 or long < 0:  # check if input is out of bounds
    print("Out of bounds")
else:
    #define count function
    def find_mine(minesweeper):
        for lat in range(len(minesweeper)):
            for long in range(len(minesweeper[lat])):
                #define positions adjacent to the open spaces
                adjacent_positions = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
                count = 0

                #if position is open count for mines around it using adjacent positions
                if minesweeper[lat][long] == "-":
                    for adjacent in adjacent_positions:
                        adjacent_row = lat + adjacent[0]
                        adjacent_col = long + adjacent[1]

                        #prevent loop from going off of the grid
                        if ((adjacent_row >= 0 and adjacent_row < len(minesweeper)) and (adjacent_col >= 0 and adjacent_col < len(minesweeper[0]))):
                            if minesweeper[adjacent_row][adjacent_col] == "#":
                                count +=1  #count variable increment according to bombs around it
                    minesweeper[lat][long] = str(count)

    #recall function to find mines
    find_mine(minesweeper)  

    #print specified coordinates
    #if coordinates land on a mine, print boom for dramatic effect
    if minesweeper[lat][long] == "#":
        print("BOOOMM")
    
    print(minesweeper[lat][long])
    
    #print mine
    for row in minesweeper:
        print(row)
