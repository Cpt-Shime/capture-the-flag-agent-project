# First name Last name

""" 
Description of the agent (approach / strategy / implementation) in short points,
fictional example / ides:
- It uses the knowledge base to remember:
     - the position where the enemy was last seen,
     - enemy flag positions,
     - the way to its flag.
- I use a machine learning model that, based on what the agent sees around it, decides:
     - in which direction the agent should take a step (or stay in place),
     - whether and in which direction to shoot.
- One agent always stays close to the flag while the other agents are on the attack.
- Agents communicate with each other:
     - position of seen enemies and in which direction they are moving,
     - the position of the enemy flag,
     - agent's own position,
     - agent's own condition (is it still alive, has it taken the enemy's flag, etc.)
- Agents prefer to maintain a distance from each other (not too close and not too far).
- etc...
"""

import random
from config import *  # contains, amongst other variables, `ASCII_TILES` (which will probably be useful here)


class Agent:
    
    # called when this agent is instanced (at the beginning of the game)
    def __init__(self, color, index):
        self.color = color  # "blue" or "red"
        self.index = index # 0, 1, or 2
        self.list_of_moves = []
        self.brojac = 0
    
    # called every "agent frame"
    def __update__(self, visible_world, position, can_shoot, holding_flag):
        # display one agent's vision:
       
        ## TODO ---- ako vide zastavu ju uzmu DONE
        ## TODO ---- Popravit kako se krecu u podrucuju zastave DONE
        ## below is a very random and extremely simple implementation for testing purposes
        
        enemy_flag_x_axsis = 25
        friendly_flag_x_axsis = 7
        if self.color == "blue":
            if can_shoot:
                action= "shoot"
            else:
                action = "move"

            #donje krilo
            if self.index == 1:
                #print(position)

                
                if holding_flag:
                    #ako vidis vlastitu zastavu idi prema njoj samo okomito ili vodoravno
                    for i in range(len(visible_world)):
                        for j in range(len(visible_world)):
                            if visible_world[i][j] == "{":
                                if i == 4 and (j in range(5,9)):
                                    action = "move"
                                    direction = "right"

                                    return action, direction
                                if i == 4 and (j in range(0,4)):
                                    action = "move"
                                    direction = "left"


                                    return action, direction

                                if j == 4 and (i in range(0,4)):
                                    action = "move"
                                    direction = "up"
                                    print("idem prema zastavi")

                                    return action, direction
                                if j == 4 and (i in range(5,9)):
                                    action = "move"
                                    direction = "down"

                                    return action, direction   
                                
                    # Movement za sredinu prijatelske strane
                    if position[0] <= friendly_flag_x_axsis and position[1] <19 and position[1] >5:
                        r = random.random() 
                        if r < 0.25:
                            direction = "left"
                        elif r < 0.45:
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

                #Potez bez zastave 
                # ako vidis zastavu idi prema njoj , okomito ili vodoravno samo      
                for i in range(len(visible_world)):
                    for j in range(len(visible_world)):
                        if visible_world[i][j] == "}":

                            if i == 4 and (j in range(5,9)):
                                action = "move"
                                direction = "right"
                                return action, direction
                            
                            if i == 4 and (j in range(0,4)):
                                action = "move"
                                direction = "left"
                                return action, direction

                            if j == 4 and (i in range(0,4)):
                                action = "move"
                                direction = "up"
                                return action, direction
                            
                            if j == 4 and (i in range(5,9)):
                                action = "move"
                                direction = "down"
                                return action, direction 
                              

                if position[0] >= enemy_flag_x_axsis and position[1] <19 and position[1] >7:
                    
                    r = random.random() 
                    if r < 0.2:
                        direction = "left"
                    elif r < 0.4:
                        direction = "right"
                    elif r < 0.75:
                        direction = "up"
                    else:
                        direction = "down"
                    
                    return action, direction
                
                elif position[0] >= enemy_flag_x_axsis and position[1] <=22:
                    
                    preferred_direction = "up"
                    r = random.random() * 1.5
                    if r < 0.30:
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
            
                #gornje krilo
            if self.index == 0: 

                if holding_flag:
                    print("Ja imam zastavu, gornji")

                    for i in range(len(visible_world)):
                        for j in range(len(visible_world)):

                            if visible_world[i][j] == "{":
                                if i == 4 and (j in range(5,9)):
                                    action = "move"
                                    direction = "right"
                                    return action, direction
                                
                                if i == 4 and (j in range(0,4)):
                                    action = "move"
                                    direction = "left"
                                    return action, direction

                                if j == 4 and (i in range(0,4)):
                                    action = "move"
                                    direction = "up"
                                    return action, direction
                                
                                if j == 4 and (i in range(5,9)):
                                    action = "move"
                                    direction = "down"
                                    return action, direction
                                
                    # Prijateljska sredina baze pocni random vrtit se  
            
                    if position[0] <= friendly_flag_x_axsis and position[1] <19 and position[1] >7:
                        r = random.random() 
                        if r < 0.3:
                            direction = "left"
                        elif r < 0.5:
                            direction = "right"
                        elif r < 0.7:
                            direction = "up"
                        else:
                            direction = "down"
                        
                        return action, direction
                
                    elif position[0] >= enemy_flag_x_axsis and position[1] >1:
                        
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
                    
                    elif position[0] <= friendly_flag_x_axsis and position[1] >=1:
        
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
                              
                    elif position[1] == 1:
                        direction = "left"
                        return action, direction
              
                # Potezi bez zastave
                for i in range(len(visible_world)):
                    for j in range(len(visible_world)):
                        if visible_world[i][j] == "}":
                            if i == 4 and (j in range(5,9)):
                                action = "move"
                                direction = "right"
                                return action, direction
                            
                            if i == 4 and (j in range(0,4)):
                                action = "move"
                                direction = "left"
                                return action, direction

                            if j == 4 and (i in range(0,4)):
                                action = "move"
                                direction = "up"
                                return action, direction
                            
                            if j == 4 and (i in range(5,9)):
                                action = "move"
                                direction = "down"

                                return action, direction


                if position[0] >= enemy_flag_x_axsis and position[1] <16 and position[1] >7:
                    
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
    
                elif position[0] >= enemy_flag_x_axsis and position[1] >=1:

                    
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

                    self.list_of_moves.append(direction)
                    return action, direction
                
                elif position[1] == 1:
                    action = "move"
                    direction = "right"
                    
                    self.list_of_moves.append(direction)
                    return action, direction
                
                
                
                direction = "up"
                preferred_direction = "right"
                r = random.random() * 1.5
                if r < 0.50:
                    direction = "up"
                elif r < 0.75:
                    direction = "left"
                elif r < 1:
                    direction = "down"
                else:
                    direction = preferred_direction
                return action, direction
            
        if self.index == 2:
            if visible_world[3][4] != "#":
                action = "move"
                direction = "up"
            
            elif visible_world[3][4] == "#":
                action = "shoot"
                direction = "down"
                
            else:
                direction = "down"
                action = "shoot"
            
            return action, direction

    # called when this agent is deleted (either because this agent died, or because the game is over)
    # `reason` can be "died" or if the game is over "blue", "red", or "tied" depending on who won
    def __terminate__(self, reason):
        if reason == "died":
            print(self.color, self.index, "died")