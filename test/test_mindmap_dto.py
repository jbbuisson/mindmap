import shutil
from pathlib import Path

from anytree import Node
from mindmap_dto import Mindmap_dto


def mkDataDir():
    Path.mkdir(Path('./data/'), exist_ok=True)


def rmDataDir():
    folder = Path('./data/')
    if folder.exists():
        shutil.rmtree(folder, ignore_errors=True)


def test_getFileName_data_folder_exists():
    mkDataDir()
    fileName = Mindmap_dto._getFileName('myMapId')
    assert fileName == Path('data/myMapId.pickle')


def test_getFileName_data_folder_does_not_exists():
    rmDataDir()
    fileName = Mindmap_dto._getFileName('myMapId')
    assert fileName == Path('data/myMapId.pickle')


def test_save():
    root_id = 'root_id'
    root = Node(root_id)
    Mindmap_dto.save(root_id, root)
    
    expectedOutputFilePath = Mindmap_dto._getFileName(root_id)
    assert expectedOutputFilePath.exists()
