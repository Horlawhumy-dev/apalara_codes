import random

class Box():
    """ Box object """
    def __init__(self, object_name):
        
        self.object_name = object_name

    #
    def __repr__(self):
        
        return str(self.object_name)


class ApalaraContainer():
    """
        An Apalara container contains four boxes in a table
    """
       

    def __init__(self, first_obj, second_obj, third_obj, fourth_obj):
        self.first_obj = first_obj
        self.second_obj = second_obj
        self.third_obj = third_obj
        self.fourth_obj = fourth_obj

        print("Setting up initial state....")
        # The state of the Apalara container
        self.state = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [first_obj, second_obj, third_obj, fourth_obj]
        ]
        
    def get_obj_position(self, target):
        """"
            A method in the Apalara class that gets the position of the objects with respect to the state.
            @params: target is an object in [row, column] format.
            @returns: No return but printing a string
        """
        for row in range(len(self.state)):
            for column in range(len(self.state[row])):
                if self.state[row][column] == target:
                    return([row, column])
                
        print(f"{target} not found")
    
    def reset_state(self):
        """
            Resets the current state to default Apalara container.
            @params: None
            @returns: None
        """
        print("Resetting to initial state...")
        self.state = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [self.first_obj, self.second_obj, self.third_obj, self.fourth_obj]
        ]
        
        
    def swap_objects_postion(self, first_obj, second_obj):
        """
            Swap postion of two objects
            It does this by:
                1. Placing the first object on any random remaining position on ground
                2. Put the second object in the intial position of the first object
                3. Put the first object(now on any random remaining position on ground) in the initial position of the second object

        """
        #Ensure all objects are of same type Box
        self.check_objs_type()
    
        #pick random object between third and fourth
        random_obj = self.get_random_obj(first_obj, second_obj)
        
        #get the positions of the three objects
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)
        row3, col3 = self.get_obj_position(random_obj)

        #make the random object position to position of object above it
        row3, col3 = [row3 - 1, col3]

        #swap the first object with the random object
        self.state[row3][col3], self.state[row1][col1] = self.state[row1][col1], self.state[row3][col3]
        
        #assign the initial position of the first object to empty one 
        row3, col3 = [row1, col1]

        #get the new position of the first and second objects
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)

        #swap the second object with the new first object position
        self.state[row3][col3], self.state[row2][col2] = self.state[row2][col2], self.state[row3][col3]
      
        #assign the initial position of second box to empty position
        row3, col3 = [row2, col2]

        #get the new position of the second and first objects
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)   
        
        #swap the two objects
        self.state[row1][col1], self.state[row3][col3] = self.state[row3][col3], self.state[row1][col1]

    def get_random_obj(self, first_obj, second_obj):
        remaining_objs = [obj for obj in self.state[3] if obj != first_obj and obj != second_obj]
        random_obj = random.choice(remaining_objs)
    
        return random_obj
    
    def check_objs_type(self):
        for index, obj in enumerate(self.state[3]):
            if type(obj) is not type(Box("A")):
                return f"object at {index} is not a Box type."
            
    def swap_two_objects(self, first_obj, second_obj, random_obj):

        #Get the position of the three boxes, two boxes you want to swap_objects_postion and the random remaining box picked 
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)
        row3, col3 = self.get_obj_position(random_obj)
        
        #Get the position above the random box picked
        row3, col3 = [row3 - 1, col3]
        
        #place the second box on the random box picked
        #in fact what this line does is to swap_objects_postion the position above the random boxed picked with the second box
        self.state[row3][col3], self.state[row2][col2] = self.state[row2][col2], self.state[row3][col3]
        
        #Assign the initial position of the second box to be empty 
        row3, col3 = [row2, col2]

        #Get the new position of the second box
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)

        #swap_objects_postion the first box to the initial first box position assigned empty earlier
        self.state[row3][col3], self.state[row1][col1] = self.state[row1][col1], self.state[row3][col3]
      

        row3, col3 = [row2, col2]
        #Get the new position of the first box
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj)  

        #swap_objects_postion the second box to the a row above the new first box position
        self.state[row1 - 1][col1], self.state[row3][col3] = self.state[row3][col3], self.state[row1 - 1][col1]

    def place_obj_under(self, first_obj, second_obj):
        """
            Place first object under second object
        """

        #Ensure all objects are of same type Box
        self.check_objs_type() 
        

        #pick random object between third and fourth
        random_obj = self.get_random_obj(first_obj, second_obj)
        
        self.swap_two_objects(first_obj, second_obj, random_obj)

    def place_obj_over(self, first_obj, second_obj):
        """
        Place first_obj on top of second_obj
        """
        
        #Get position of the two boxes
        row1, col1 = self.get_obj_position(first_obj)
        row2, col2 = self.get_obj_position(second_obj) 

        #swap_objects_postion the first box to the a row above the second box position
        self.state[row2 - 1][col2], self.state[row1][col1] = self.state[row1][col1], self.state[row2 - 1][col2]

    def arrange_first_to_fourth(self):
        """
            Arrange the objects on top of each other from first to fourth object with fourth object at the buttom
        """

        #Ensure all objects are of same type Box
        self.check_objs_type()

        #Place box C on D
        self.place_obj_over(self.third_obj, self.fourth_obj)

        #Place box B on C
        self.place_obj_over(self.second_obj, self.third_obj)

        #Place box A on B
        self.place_obj_over(self.first_obj, self.second_obj)

    def arrange_last_to_first(self):
        """
            Arrange the objects on top of each other from fourth to first object with first object at the buttom
        """
        #Ensure all objects are of same type Box
        self.check_objs_type()

        #Place box B on A
        self.place_obj_over(self.second_obj, self.first_obj)

        #Place box C on B
        self.place_obj_over(self.third_obj, self.second_obj)

        #Place box D on C
        self.place_obj_over(self.fourth_obj, self.third_obj)


if "__name__" == "__main__":
    A = Box("A")
    B = Box("B")
    C = Box("C")
    D = Box("D")


    container = ApalaraContainer(A, B, C, D)

    print(container.state)
    print("\n")

    print("Swapping object A and B...")
    container.swap_objects_postion(A, B)
    print(container.state)

    print("\n")
    container.reset_state()

    print("\n")
    print(container.state)

    print("\n")
    print("Placing object B under A...")
    container.place_obj_under(A, B)
    print(container.state)

    print("\n")
    container.reset_state()

    print("\n")
    print(container.state)

    print("\n")
    print("Placing object A over B...")
    container.place_obj_over(A, B)
    print(container.state)

    print("\n")
    container.reset_state()
    print(container.state)

    print("\n")
    print("Arranging object A, B, C, D...")
    container.arrange_first_to_fourth()
    print(container.state)

    print("\n")
    container.reset_state()
    print(container.state)

    print("\n")
    print("Arranging object D, c, B, A...")
    container.arrange_last_to_first()
    print(container.state)
    print("\n")