class Node:
    def __init__(self, question, guess: str, yes_branch=None, no_branch=None):
        self.question = question
        self.yes_branch = yes_branch  # Reference to the next node if the answer is "yes"
        self.no_branch = no_branch  # Reference to the next node if the answer is "no"
        self.guess = guess

    def is_leaf(self):
        return self.yes_branch is None and self.no_branch is None

    def __repr__(self) -> str:
        return f"Node(question={self.question})"


def traverse_tree(node, answers):
    if not node:
        return None, None
    if not answers:
        return node.question, node.guess
    for answer in answers:
        # Move to the next node based on the answer
        if answer == "yes":
            return traverse_tree(node.yes_branch, answers[1:])
        else:
            return traverse_tree(node.no_branch, answers[1:])


edible_things = Node(
    "Is it a type of drink?",
    yes_branch=Node(
        "Is it an alcoholic beverage?",
        no_branch=Node(
            "Is it a type of tea or coffee?",
            no_branch=Node(
                "Is it a type of soft drink?",
                no_branch=Node(
                    "Is it a type of juice?",
                    no_branch=Node("Is it a type of milk?", guess="soy milk"),
                    guess="orange juice",
                ),
                yes_branch=Node(
                    "Is it a type of soda?",
                    no_branch=Node("Is it a type of energy drink?", guess="red bull"),
                    guess="coca cola",
                ),
                guess="apple juice",
            ),
            yes_branch=Node("Is it a type of coffee?", guess="espresso"),
            guess="chai tea",
        ),
        yes_branch=Node(
            "Is it a type of beer?",
            guess="wine",
            no_branch=Node(
                "Is it a type of spirit?",
                guess="whiskey",
                no_branch=Node(
                    "Is it a type of cocktail?",
                    guess="margarita",
                    no_branch=Node("Is it a type of wine?", guess="chardonnay"),
                ),
            ),
        ),
        guess="milk",
    ),
    no_branch=Node(
        "Is it a type of fruit or vegetable?",
        yes_branch=Node(
            "Is it a type of fruit?",
            guess="carrot",
            yes_branch=Node(
                "Is it a type of berry?",
                guess="blood orange",
                no_branch=Node(
                    "Is it a type of citrus fruit?",
                    guess="banana",
                    no_branch=Node(
                        "Is it a type of melon?",
                        guess="watermelon",
                        no_branch=Node(
                            "Is it a type of stone fruit?",
                            guess="peach",
                            no_branch=Node(
                                "Is it a type of tropical fruit?",
                                guess="mango",
                                no_branch=Node("Is it a type of apple?", guess="granny smith"),
                            ),
                        ),
                    ),
                ),
            ),
            no_branch=Node(
                "Is it a type of leafy green?",
                guess="broccoli",
                no_branch=Node(
                    "Is it a type of root vegetable?",
                    guess="potato",
                    no_branch=Node(
                        "Is it a type of squash?",
                        guess="zucchini",
                        no_branch=Node(
                            "Is it a type of onion?",
                            guess="red onion",
                            no_branch=Node(
                                "Is it a type of pepper?",
                                guess="bell pepper",
                                no_branch=Node("Is it a type of tomato?", guess="roma tomato"),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        no_branch=Node(
            "Is it a sweet dish or dessert?",
            yes_branch=Node(
                "Is it a type of candy or chocolate?",
                no_branch=Node(
                    "Is it a type of cake?",
                    no_branch=Node(
                        "Is it a type of ice cream?",
                        no_branch=Node(
                            "Is it a type of cookie?",
                            guess="oreos cookies",
                            no_branch=Node(
                                "Is it a type of pie?",
                                guess="mud pie",
                            ),
                        ),
                        guess="ice cream",
                    ),
                    yes_branch=Node("Is it a type of cheesecake?", guess="cheesecake"),
                    guess="carrot cake",
                ),
                yes_branch=Node("Is it a type of chocolate?", guess="dark chocolate"),
                guess="chocolate chip cookie",
            ),
            no_branch=Node(
                "Is it a type of bread or pastry?",
                no_branch=Node(
                    "Is it a type of noodle or pasta?",
                    no_branch=Node(
                        "Is it a type of meat or fish?",
                        no_branch=Node(
                            "Is it a type of soup?",
                            guess="chicken noodle soup",
                            no_branch=Node(
                                "Is it a type of cheese?",
                                guess="parmesan cheese",
                                no_branch=Node(
                                    "Is it a type of sauce?",
                                    guess="ketchup",
                                    no_branch=Node(
                                        "Is it a type of spice?",
                                        guess="cinnamon",
                                        yes_branch=Node("Is it a type of herb?", guess="basil"),
                                    ),
                                ),
                            ),
                        ),
                        yes_branch=Node("Is it a type of fish?", guess="salmon"),
                        guess="beef stew",
                    ),
                    yes_branch=Node(
                        "Is it a type of noodle?",
                        guess="soba noodles",
                        no_branch=Node("Is it a type of ravioli?", guess="orzo pasta"),
                    ),
                    guess="spaghetti bolognese",
                ),
                guess="sourdough bread",
                yes_branch=Node("Is it a type of bread?", guess="baguette"),
            ),
            guess="apple pie",
        ),
        guess="apricot",
    ),
    guess="ramen noodles",
)

basic_man_made_object = Node(
    "Is it a man-made object?",
    yes_branch=Node(
        "Is it electronic?",
        yes_branch=Node(
            "Is it used for entertainment?",
            yes_branch=Node(
                "Is it a type of gaming device?",
                yes_branch=Node(
                    "Is it a console?",
                    no_branch=Node("Is it a handheld device?", guess="gameboy"),
                    guess="playstation",
                ),
                guess="nintendo switch",
                no_branch=Node(
                    "Is it a type of accessory?",
                    guess="headphone",
                    no_branch=Node(
                        "Is it a handheld device?",
                        guess="phone",
                        yes_branch=Node(
                            "Is it a type of phone?",
                            guess="iphone",
                            no_branch=Node(
                                "Is it a type of tablet?",
                                guess="tablet",
                                no_branch=Node(
                                    "Is it a type of watch?",
                                    guess="apple watch",
                                    no_branch=Node(
                                        "Is it a type of camera?",
                                        guess="digital camera",
                                        no_branch=Node("Is it a type of computer?", guess="laptop"),
                                    ),
                                ),
                            ),
                        ),
                        no_branch=Node("Is it a type of computer?", guess="computer"),
                    ),
                ),
            ),
            no_branch=Node(
                "Is it a household appliance?",
                yes_branch=Node(
                    "Is it used in the kitchen?",
                    guess="wall oven",
                    yes_branch=Node(
                        "Can it be held in hand?",
                        guess="fridge",
                        yes_branch=Node("Is it used for cooking?", guess="spatula"),
                    ),
                ),
                no_branch=Node(
                    "Is it a tool or industrial equipment?",
                    yes_branch=Node(
                        "Is it a hand-held tool?",
                        guess="power tool",
                        yes_branch=Node(
                            "Is it powered by batteries?",
                            guess="cordless drill",
                            yes_branch=Node("Does it have a display?", guess="fish finder"),
                        ),
                        no_branch=Node("Is it used for manufacturing?", guess="lathe"),
                    ),
                    no_branch=Node(
                        "Is it related to transportation?",
                        no_branch=Node(
                            "Is it related to entertainment or hobbies?",
                            no_branch=Node(
                                "Is it related to health and safety?",
                                guess="fire alarm",
                            ),
                            guess="car",
                            yes_branch=Node("Is it a type of vehicle?", guess="electric car"),
                        ),
                        guess="electric bike",
                    ),
                    guess="drill",
                ),
                guess="microwave",
            ),
            guess="printer",
        ),
        no_branch=Node(
            "Is it a tool or industrial equipment?",
            no_branch=Node(
                "Is it a vehicle?",
                no_branch=Node(
                    "Is it a type of building or structure?",
                    no_branch=Node(
                        "Is it a piece of furniture?",
                        no_branch=Node(
                            "Is it a toy or game?",
                            no_branch=Node(
                                "Is it a piece of art or decoration?",
                                guess="painting",
                                no_branch=Node(
                                    "Is it a type of container?",
                                    guess="thrash can",
                                    no_branch=Node(
                                        "Is it a type of clothing?",
                                        guess="t-shirt",
                                        no_branch=Node(
                                            "Is it related to pets or hobbies?",
                                            guess="leash",
                                            no_branch=Node(
                                                "Is it related personal hygiene or grooming?",
                                                guess="lotion",
                                                no_branch=Node(
                                                    "Is it a type of medicine?", guess="aspirin"
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            guess="lego",
                        ),
                        guess="bed",
                        yes_branch=Node(
                            "Is it typically found in the living room?",
                            guess="armchair",
                            no_branch=Node(
                                "Is it typically found in the bed room?",
                                guess="nightstand",
                                no_branch=Node(
                                    "Is it typically found in the kitchen?",
                                    guess="stool",
                                    no_branch=Node(
                                        "Is it typically found in the bathroom?", guess="toilet"
                                    ),
                                ),
                            ),
                        ),
                    ),
                    guess="bridge",
                ),
                guess="truck",
            ),
            yes_branch=Node(
                "Is it a type of tool?",
                guess="hammer",
                no_branch=Node("Is it a type of machine?", guess="drill press"),
                yes_branch=Node("Is it a tool used for cleaning?", guess="duster"),
            ),
            guess="screwdriver",
        ),
        guess="computer",
    ),
    no_branch=Node(
        "Is it a type of sport?",
        no_branch=Node(
            "Is it a type of game?",
            guess="chess",
            yes_branch=Node(
                "Is it a board game?",
                guess="scrabble",
                no_branch=Node(
                    "Is it a card game?",
                    guess="poker",
                    no_branch=Node("Is it a type of puzzle game?", guess="crossword"),
                ),
            ),
            no_branch=Node(
                "Is it a natural phenomenon?",
                guess="earthquake",
                no_branch=Node(
                    "Is it an abstract concept?",
                    guess="philosophy",
                    yes_branch=Node("Is it a scientific discipline?", guess="mathematics"),
                    no_branch=Node(
                        "Is it a human body part?",
                        guess="kidney",
                        no_branch=Node("Is it a type of music?", guess="jazz"),
                        yes_branch=Node(
                            "Is it an internal organ?",
                            guess="heart",
                            no_branch=Node(
                                "Is it a type of bone?",
                                guess="femur",
                                no_branch=Node("Is it a type of muscle?", guess="bicep"),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        guess="ice hockey",
    ),
    guess="hammer",
)


question_tree_root = Node(
    "Is it a living thing?",
    yes_branch=Node(
        "Is it an animal?",
        yes_branch=Node(
            "Is it a pet or domesticated animal?",
            yes_branch=Node(
                "Is it a mammal?",
                no_branch=Node(
                    "Is it a bird?",
                    no_branch=Node(
                        "Is it a reptile?",
                        no_branch=Node(
                            "Is it a fish?",
                            no_branch=Node("Is it an amphibian?", guess="frog"),
                            guess="goldfish",
                        ),
                        guess="lizard",
                    ),
                    guess="parrot",
                ),
                guess="cat",
            ),
            no_branch=Node(
                "Is it a mammal?",
                no_branch=Node(
                    "Is it a bird?",
                    no_branch=Node(
                        "Is it a reptile?",
                        no_branch=Node(
                            "Is it a fish?",
                            no_branch=Node("Is it an amphibian?", guess="salamander"),
                            guess="shark",
                        ),
                        guess="alligator",
                    ),
                    yes_branch=Node("Is it a type of waterbird?", guess="sea gull"),
                    guess="eagle",
                ),
                guess="crocodile",
            ),
            guess="moose",
        ),
        no_branch=Node(
            "Is it a type of plant?",
            yes_branch=Node(
                "Is it a type of tree?",
                no_branch=Node(
                    "Is it a type of flower?",
                    guess="african violet",
                    no_branch=Node("Is it a type of moss?", guess="sphagnum moss"),
                ),
                yes_branch=Node("Is it a type of fruit tree?", guess="apple tree"),
                guess="rose",
            ),
            guess="cactus",
            no_branch=Node(
                "Is it a type of fungus?",
                guess="mushroom",
                no_branch=Node(
                    "Is it a type of algae?",
                    guess="seaweed",
                ),
            ),
        ),
        guess="human",
    ),
    no_branch=Node(
        "Is it a type of food or drink?",
        yes_branch=edible_things,
        no_branch=basic_man_made_object,
        guess="chisel",
    ),
    guess="chainsaw",
)
