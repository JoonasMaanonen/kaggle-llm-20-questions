import os
import sys

# **IMPORTANT:** Set up your system path like this to make your code work
# both in notebooks and in the simulations environment.
KAGGLE_AGENT_PATH = "/kaggle_simulations/agent/"
print("Try do some logging...")
if os.path.exists(KAGGLE_AGENT_PATH):
    sys.path.insert(0, os.path.join(KAGGLE_AGENT_PATH, "lib"))
    MODEL_DIR = f"{KAGGLE_AGENT_PATH}/models/Meta-Llama-3-8B-Instruct"
    print("Lib folder added to sys path")
else:
    sys.path.insert(0, "lib")
    MODEL_DIR = "../models/Meta-Llama-3-8B-Instruct"

from bots.llama_3_bot import Llama3CombinedBot
from data_models.observation import Observation

# Use one combined model to handle all roles with the same base model.
# This reduces the loading times making the submission run in the time limit.
agent = Llama3CombinedBot(model_dir=MODEL_DIR)


def agent_fn(obs, cfg):
    observation = Observation(**obs)
    response = agent(
        observation,
    )
    return response
