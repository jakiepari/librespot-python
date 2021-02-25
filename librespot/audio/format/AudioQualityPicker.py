from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from librespot.proto import Metadata


class AudioQualityPicker:
    def get_file(self, files: list[Metadata.AudioFile]) -> Metadata.AudioFile:
        pass