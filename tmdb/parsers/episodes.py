"""Parsers of episode objects."""
from datetime import datetime, date

from tmdb.parsers.mixins import ImageParserMixin, ImageSize
from ..datatypes import Episode
from .base import Parser
from typing import Optional


class EpisodeParser(ImageParserMixin, Parser[Episode]):
    """Parser of Episode objects."""

    object_class = Episode

    @staticmethod
    def _get_air_date(data: dict) -> Optional[date]:
        if data['air_date'] is not None:
            return datetime.strptime(data['air_date'], '%Y-%m-%d').date()
        else:
            return None

    def get_kwargs(self, data: dict) -> dict:
        return {
            'number': data['episode_number'],
            'name': data['name'],
            'synopsis': data['overview'],
            'still_path': self.get_image_or_placeholder_url(
                data['still_path'],
                family='stills',
            ),
            'air_date': self._get_air_date(data),
        }
