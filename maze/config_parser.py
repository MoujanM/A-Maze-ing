
from pydantic import BaseModel, Field, BeforeValidator, field_validator, ValidationError
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

class Configs(Enum):
    WIDTH="WIDTH"
    HEIGHT="HEIGHT"
    ENTRY="ENTRY"
    EXIT="EXIT"
    OUTPUT_FILE="OUTPUT_FILE"
    PERFECT="PERFECT"

class MazeSpecs(BaseModel, extra='allow'):
    width: int = Field(ge=2, validation_alias='WIDTH')
    height: int = Field(ge=2, validation_alias='HEIGHT')
    entry_point: tuple[int, int] = Field(validation_alias='ENTRY')
    exit_point: tuple[int, int] = Field(validation_alias='EXIT')
    output_name: str = Field(min_length=4, pattern=".*\.txt$", validation_alias='OUTPUT_FILE')
    perfect: bool = Field(default=False, validation_alias='PERFECT')

    @field_validator('entry_point', 'exit_point', mode='before')
    @classmethod
    def int_tuple(cls, data: str) -> tuple[int, int]:
        x, y = data.split(',', 1)
        if int(x) < 0 or int(y) < 0:
            raise ValueError("Coordinates must be positive")
        else:
            return (int(x), int(y))


class ConfigError(Exception):
    """for custom parser error messages"""
    pass


class ConfigParser(ABC):

    def read_txt(self, file_name: str) -> dict[str, Any]:
        """
        Function that reads a file from file_name (e.g. 'config.txt')
        looking for KEY=VALUE lines in the file, it creates & returns
        a dict of {KEY: VALUE} to be validated.
        """

        txt_config: dict[str, Any] = {}
        try:
            with open(file_name) as f:
                for line in f:
                    if not (line.startswith("#") or line.isspace()):
                        key, value = line.split("=", 1)
                        txt_config.update({key.strip(): value.strip()})
                return txt_config
        except FileNotFoundError:
            raise ConfigError(f"Error locating file '{file_name}'")
        except Exception as e:
            raise ConfigError(f"Unknown error reading the file - {e}")

    

    def validate_config(self, txt_config: dict[str, Any]) -> MazeSpecs:
        """
        Takes raw dict from read_text and validates the data
        against BaseModel. 
        If validation successful, maze specs are returned
        Else, informative error message.
        """

        required: set[str] = {e.value for e in Configs}
        provided: set[str] = set(txt_config.keys())

        if not required.issubset(provided):
            missing: set[str] = required - provided
            raise ConfigError(f"Mandatory keys missing - {", ".join(missing)}")
        else:
            try:
                valid_config = MazeSpecs(**txt_config)
                return valid_config
            except ValidationError as e:
                error_msgs = [err['msg'] for err in e.errors()]
                complete_err = "\n".join(error_msgs)
                raise ConfigError(f"Validation failed - {complete_err}")
        

# if __name__ == "__main__":
#     file_name = "sample_config.txt"
#     my_test = ConfigParser.read_txt(file_name)
#     print(my_test)
#     new_config = ConfigParser.validate_config(my_test)
#     print(type(new_config))
#     print(new_config)

