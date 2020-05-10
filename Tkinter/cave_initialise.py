import shelve


settings = shelve.open("setting")

settings["0"] = {"desc": "You are sitting in front of a computer learning Python",
                    "exits": {},
                    "namedExits": {}},
settings["1"] = {"desc": "You are standing at the end of a road before a small brick building",
                   "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q":'0'},
                   "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}}
settings["2"] = {"desc": "You are at the top of a hill",
                   "exits": {"N": '5', "Q": '0'},
                   "namedExits": {"5": '5'}}
settings["3"] = {"desc": "You are inside a building, a well house for a small stream",
                     "exits": {"W": '1', "Q": '0'},
                     "namedExits": {"1": '1'}}
settings["4"] = {"desc": "You are in a valley beside a stream",
                    "exits": {"N": '1', "W": '2', "Q": '0'},
                    "namedExits": {"1": '1', "2": '2'}}
settings["5"] = {"desc": "You are in the forest",
                    "exits": {"W": '2', "S": '1', "Q": '0'},
                    "namedExits": {"2": '2', "1": '1'}}

settings.close()
# print(settings["five"])

vocabulary = shelve.open("vocabulary")

vocabulary["QUIT"] = "Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "R"
vocabulary["HILL"] = "H"
vocabulary["BUILDING"] = "B"
vocabulary["VALLEY"] = "V"
vocabulary["FOREST"] = "F"

vocabulary.close()
