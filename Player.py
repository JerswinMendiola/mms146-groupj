class Player:
    def __init__(self, player_name: str):
        ''' 
        initialization of a new Player object
        '''
        self._player_name = player_name

    def get_name(self):
        '''
        Returns the name of the player
        '''
        return self._player_name 
    
    def set_name(self, new_name: str):
        '''
        Updates the name of the player

        Parameters:
        new_name (str): The new name to assign to the player
        '''
        self.__player_name = new_name