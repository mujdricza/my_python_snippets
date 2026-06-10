"""
Snippet for dotenv usage.

Needs dotenv
"""
import os
from dotenv import load_dotenv


_CURR_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(_CURR_DIR, ".my_exp_env")
ENV_VARIABLE = "OPENAI_API_KEY"

is_successful: bool = load_dotenv(
    dotenv_path=ENV_PATH,
    verbose=False,
    override=False,
)
print(f"Loading dotenv file {ENV_PATH} is succesful: {is_successful}")
# --> value of the ENV_VARIABLE is loaded to os.environ

env_var_value = os.getenv(ENV_VARIABLE)
print(f"Value of {ENV_VARIABLE} is '{env_var_value}'")
