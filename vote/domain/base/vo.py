from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class ValueObject:
    ...
