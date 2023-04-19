#create mine-grid
minesweeper = [
     ["#","-","#","-","-"],
     ["-","#","#","-","-"],
     ["-","-","-","-","#"],
     ["-","#","#","-","-"],
     ["-","-","#","-","#"],
 ]

#print mine-grid
for row in minesweeper:
    print(row) 

#new-line spaces
print("\n")

#define count function
def find_mine(minesweeper):
    for i in range(len(minesweeper)):
        for j in range(len(minesweeper[i])):
            #define positions adjacent to the open spaces
            adjacent_positions = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
            count = 0
            #if position is open count for mines around it using adjacent positions
            if minesweeper[i][j] == "-":
                for adjacent in adjacent_positions:
                    adjacent_row = i + adjacent[0]
                    adjacent_col = j + adjacent[1]

                #prevent loop from going off of the grid
                    if ((adjacent_row >= 0 and adjacent_row < len(minesweeper)) and (adjacent_col >= 0 and adjacent_col < len(minesweeper))):
                        if minesweeper[adjacent_row][adjacent_col] == "#":
                            count +=1  #count variable increment according to bombs around it
                    minesweeper[i][j] = str(count)


#recall function to find mines
find_mine(minesweeper)  

#print mine
for row in minesweeper:
    print(row)  