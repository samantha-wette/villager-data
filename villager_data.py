"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    all_species = set()

    my_file = open(filename)
    for line in my_file:
        line = line.split('|')
        all_species.add(line[1])

    print(all_species)
    return all_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    my_file = open(filename)
    villagers = []
    for line in my_file:
        line = line.split('|')

        if search_string == "All":
            villagers.append(line[0]) 
        
        elif line[1] == search_string:
            villagers.append(line[0])

        
    return sorted(villagers)



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness_list = []
    nature_list = []
    education_list = []
    music_list = []
    fashion_list = []
    play_list = []

    my_file = open(filename)
    for line in my_file:
        line = line.split('|')
        villager_name = line[0]
        villager_hobby = line[3]
        if villager_hobby == "Fitness":
            fitness_list.append(villager_name)
        elif villager_hobby == "Nature":
            nature_list.append(villager_name)
        elif villager_hobby == "Education":
            education_list.append(villager_name)
        elif villager_hobby == "Music":
            music_list.append(villager_name)
        elif villager_hobby == "Fashion":
            fashion_list.append(villager_name)
        elif villager_hobby == "Play":
            play_list.append(villager_name)
            
    hobby_list = [sorted(fitness_list), sorted(nature_list), sorted(education_list), sorted(music_list), sorted(fashion_list), sorted(play_list)]
    return hobby_list

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    my_file = open(filename)
    
    all_data = []
    for line in my_file:
        line = line.split('|')
        line_data = tuple(line)
        all_data.append(line_data)
    
    return all_data


def find_motto(filename, villager_name='Default'):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    my_file = open(filename)
    
    if villager_name == 'Default':
        return None

    for line in my_file:
        line = line.split('|')
        name = line[0]
        motto = line[4]
        if name == villager_name:
            return motto

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    likeminded_villagers = set()

    my_file = open(filename)

    for line in my_file:
        line = line.split('|')
        
        if line[0] == villager_name:
            personality = line[2]
            break

    for line in my_file:
        line = line.split('|')

        if line[2] == personality:
            likeminded_villagers.add(line[0])
    
    return likeminded_villagers