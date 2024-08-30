import random


class RandomGuesser:
    def __init__(self) -> None:
        """Init."""
        pass

    def __call__(self, obs: dict) -> str:
        """Call the model."""
        if obs.turnType == "ask":
            return random.choice(["Is it a person?", "Is it a place?", "Is it a thing?"])
        elif obs.turnType == "guess":
            return random.choice(["Paris", "Chuck Norris", "Carbonara"])
        else:
            raise ValueError("Guesser can only ask or guess.")


class RandomAnswerer:
    def __init__(self) -> None:
        """Init."""
        pass

    def __call__(self, obs: dict) -> str:
        if obs.turnType == "answer":
            return random.choice(["yes", "no"])
        else:
            raise ValueError("Answerer can only answer.")
