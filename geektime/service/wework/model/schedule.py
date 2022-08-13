from dataclasses import dataclass


@dataclass
class Schedule:
    summary: str = None
    color: str = None
    shares: list[str] = None
    organizer: str = None