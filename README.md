# Shortest-path-finder-in-a-maze-using-BFS

Controls(mouse only):
Right Click: Sets start and end position alternatively
Left Click: Block or open passage
Middle Click: Start path finding process

Time and space complexity of Algorithm
O(width x height). For square maze of size n, O(n^2)



Algorithm
Step 1: Start
Step 2: Take a 'maze' which is an array, 'start' & 'end' position
Step 3: Initialize 'rows', 'cols', 'moves', 'queue' & 'visited' for starting position and 	empty 'path' 
Step 4: While queue isn't empty{
		Dequeue current position and path (i.e. front element)
		if current position is 'end' then return 'path' 
		Iterate over all possible moves{
			Get new position (nr,nc)
			Check if the new move is valid (move should be within bounds, path should be free & not visited)
			For valid move{
				Add the position and path to queue
			}
		}
	}
Step 5: If no path is found, return 0
Step 6: Stop
