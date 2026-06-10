"""
Snippet for reading boolean environment variable with simple methods and
environs module.

See also https://pypi.org/project/environs/

Needs: pip install environs
"""
import os
import sys

from src.general_utils.utility_functions import install_if_needed
install_if_needed("environs")
from environs import env


def _get_raw_env_var(var_name: str, default_value: str = "False") -> str:
    env_var: str = os.environ.get(var_name, default_value)
    return env_var


def _get_bool_env_var_simple(var_name: str) -> bool:
    env_var = _get_raw_env_var(var_name)
    return env_var.lower() == "true"


def _get_bool_env_var_multi_values(
    var_name: str,
    true_values: tuple[str, ...] = ("true", "yes", "y", "1")
) -> bool:
    env_var = _get_raw_env_var(var_name)
    return env_var.lower() in true_values


def _get_bool_env_var_environs(
    var_name: str,
    env_file_path: str = ".env"
) -> bool:
    env.read_env(env_file_path)  # if file exists, get variables from there
    env_var: bool = env.bool(var_name, False)
    return env_var


def main(var_name: str) -> None:
    env_var_raw = _get_raw_env_var(var_name)
    print(f"raw env_var: '{env_var_raw}', type: {type(env_var_raw)}")

    env_var_simple = _get_bool_env_var_simple(var_name)
    env_var_multi = _get_bool_env_var_multi_values(var_name)
    env_var_environs = _get_bool_env_var_environs(var_name)

    for env_var in [env_var_simple, env_var_multi, env_var_environs]:
        print(f"bool env_var: '{env_var}', type: {type(env_var)}")


if __name__ == "__main__":
    main(sys.argv[1])
