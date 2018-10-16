from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class Show:
    """Class to represent the details of a show."""

    id: int
    title: str
    small_logo_path: str
    big_logo_path: str = None
    synopsis: str = None
    creation_date: datetime = None
    directors: List[str] = None
    genres: List[str] = None
    next_episode_date: datetime = None
    last_episode_date: datetime = None


