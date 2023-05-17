"""
def __update__(self, visible_world, position, can_shoot, holding_flag):
        # display one agent's vision:
        if self.index == 0:
            print("\n===========================\n")
            for row in visible_world:
                print(" " + " ".join(row))
                
        
        ## below is a very random and extremely simple implementation for testing purposes
        
        if self.color == "blue":

            if self.index == 0:
                action = "move"
                direction = "up"
                #jedna iznad

                if visible_world[3][4] == "#":
                     print("theres a fucking wall")
                     action = "move"
                     direction = "right"
                     #jedna desno i jedna iznad
                elif visible_world[4][5] == "#" and visible_world[3][4] == "#":
                        
                        action = "move"
                        direction = "left"
                     #jedna desno jedna lijevo i jedna iznad
                elif visible_world[4][5] == "#" and visible_world[4][3]  == "#" and visible_world[3][4]  == "#":
                        action = "move"
                        direction = "down"
                            
                if can_shoot:
                     action = "shoot"

                self.list_of_moves.append(direction)
                print(self.list_of_moves)
                return action, direction 
            
            if self.index == 1:
                
                action = "move"
                direction = "down"
                #jedna ispod
                if visible_world[5][4] == "#":
                    action = "move"
                    direction = "right"
                #jedna ispod i jedna desno
                elif visible_world[4][5] == "#" and visible_world[5][4] == "#":
                        action = "move"
                        direction = "left"
                        
                elif visible_world[4][5] == "#" and visible_world[5][4]  == "#" and visible_world[3][4]  == "#":
                        action = "move"
                        direction = "down"
                            
                if can_shoot:
                     action = "shoot"
                return action, direction 

            if self.index == 1:
                action = "shoot"
                direction = "down"
                return action, direction
            
            

            if can_shoot and random.random() > 0.5:
                action = "shoot"
            else:
                action = "move"
            
            direction = "right"

            return action, direction 
        


    
def __update__(self, visible_world, position, can_shoot, holding_flag):
        # display one agent's vision:
        if self.index == 0:
            print("\n===========================\n")
            for row in visible_world:
                print(" " + " ".join(row
        
        ## below is a very random and extremely simple implementation for testing purposes
        
        if can_shoot and random.random() > 0.5:
            action = "shoot"
        else:
            action = "move"
            
        if self.color == "blue":
            preferred_direction = "right"
            if holding_flag:
                preferred_direction = "left"
        elif self.color == "red":
            preferred_direction = "left"
            if holding_flag:
                preferred_direction = "right"
        
        r = random.random() * 1.5
        if r < 0.25:
            direction = "left"
        elif r < 0.5:
            direction = "right"
        elif r < 0.75:
            direction = "up"
        elif r < 1.0:
            direction = "down"
        else:
            direction = preferred_direction
            
        return action, direction
        """

for i in range(9):
    for j in range(9):
        print(i, j , end = "|")
    print(' ')

#Donje krilo radi tip top
"""
if self.index == 1:
                print(position)

                
                if holding_flag:
                    print("Ja imam zastavu, donji")

                    for i in range(len(visible_world)):
                        for j in range(len(visible_world)):
                            if visible_world[i][j] == "{":
                                if i == 4 and (j in range(5,9)):
                                    action = "move"
                                    direction = "right"
                                    print("idem prema zastavi")

                                    return action, direction
                                
                                if i == 4 and (j in range(0,4)):
                                    action = "move"
                                    direction = "left"

                                    print("idem prema zastavi")

                                    return action, direction

                                if j == 4 and (i in range(0,4)):
                                    action = "move"
                                    direction = "up"
                                    print("idem prema zastavi")

                                    return action, direction
                                if j == 4 and (i in range(4,9)):
                                    action = "move"
                                    direction = "up"

                                    return action, direction   
                                
                    # Enemy sredina baze 
                    if position[0] <= friendly_flag_x_axsis and position[1] <19 and position[1] >5:
                        r = random.random() 
                        if r < 0.25:
                            direction = "left"
                        elif r < 0.5:
                            direction = "right"
                        elif r < 0.75:
                            direction = "up"
                        else:
                            direction = "down"
                        
                        return action, direction
                
                    elif position[0] >= enemy_flag_x_axsis and position[1] <22:
                    
                        preferred_direction = "down"
                        r = random.random() * 1.5
                        if r < 0.25:
                            direction = "left"
                        elif r < 0.5:
                            direction = "right"
                        elif r < 0.75:
                            direction = "up"
                        elif r < 1.0:
                            direction = "down"
                        else:
                            direction = preferred_direction

                        return action, direction
                    
                    elif position[0] <= friendly_flag_x_axsis and position[1] <=22:
    
                        preferred_direction = "up"
                        r = random.random() * 1.5
                        if r < 0.25:
                            direction = "left"
                        elif r < 0.5:
                            direction = "right"
                        elif r < 0.75:
                            direction = "up"
                        elif r < 1.0:
                            direction = "down"
                        else:
                            direction = preferred_direction

                        return action, direction
                
                    elif position[1] == 22:
                        
                        direction = "left"

                        
                        return action, direction
                        
                for i in range(len(visible_world)):
                    for j in range(len(visible_world)):
                        if visible_world[i][j] == "}":
                            if i == 4 and (j in range(5,9)):
                                action = "move"
                                direction = "right"
                                print("idem prema zastavi")

                                return action, direction
                            
                            if i == 4 and (j in range(0,4)):
                                action = "move"
                                direction = "left"

                                print("idem prema zastavi")

                                return action, direction

                            if j == 4 and (i in range(0,4)):
                                action = "move"
                                direction = "up"
                                print("idem prema zastavi")

                                return action, direction
                            if j == 4 and (i in range(4,9)):
                                action = "move"
                                direction = "up"

                                return action, direction   

                if position[0] >= enemy_flag_x_axsis and position[1] <19 and position[1] >5:
                    
                    r = random.random() 
                    if r < 0.25:
                        direction = "left"
                    elif r < 0.5:
                        direction = "right"
                    elif r < 0.75:
                        direction = "up"
                    else:
                        direction = "down"
                    
                    return action, direction
                
                elif position[0] >= enemy_flag_x_axsis and position[1] <=22:
                    
                    preferred_direction = "up"
                    r = random.random() * 1.5
                    if r < 0.25:
                        direction = "left"
                    elif r < 0.5:
                        direction = "right"
                    elif r < 0.75:
                        direction = "up"
                    elif r < 1.0:
                        direction = "down"
                    else:
                        direction = preferred_direction

                    return action, direction
                
                elif position[1] == 22:
                    
                    direction = "right"

                    return action, direction

                
                direction = "up"
                preferred_direction = "right"
                r = random.random() * 1.5
                if r < 0.50:
                    direction = "down"
                elif r < 0.75:
                    direction = "left"
                elif r < 1:
                    direction = "up"
                else:
                    direction = preferred_direction
                
                return action, direction
            
"""
         

"""
                if holding_flag:
                    if self.brojac == 0: 
                        self.list_of_moves.reverse()
                    action = "move"
                    direction = self.list_of_moves[self.brojac]
                    if direction == "up":
                        direction = "down"
                    if direction == "down":
                        direction = "up"
                    if direction == "left":
                        direction = "right"
                    if direction == "right":
                        direction = "left"
                    self.brojac = self.brojac+1
                    print(direction)
                    return action, direction
                """