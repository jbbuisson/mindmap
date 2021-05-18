import pickle
from pathlib import Path

from anytree import Node

class Mindmap_dto:
    @staticmethod
    def _getFileName(mapId:str) -> Path:
        path = Path('./data/')
        if not path.exists():
            path.mkdir()
        return path / (mapId + '.pickle')


    @staticmethod
    def save(mapId:str, root:Node):
        with Mindmap_dto._getFileName(mapId).open(mode='wb') as file:
            pickle.dump(root, file)


    @staticmethod
    def load(mapId:str) -> Node:
        with Mindmap_dto._getFileName(mapId).open(mode='rb') as file:
            return pickle.load(file)
