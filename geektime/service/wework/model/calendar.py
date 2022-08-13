from dataclasses import dataclass


@dataclass
class Calendar:
    summary: str = None
    color: str = None
    shares: list[str] = None
    organizer: str = None

