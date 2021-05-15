import shutil
from filecmp import cmp
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
    fileName = Mindmap_dto._get_filename('myMapId')
    assert fileName == Path('data/myMapId.pickle')
    rmDataDir()


def test_getFileName_data_folder_does_not_exists():
    rmDataDir()
    fileName = Mindmap_dto._get_filename('myMapId')
    assert fileName == Path('data/myMapId.pickle')
    rmDataDir()


def test_save():
    root_id = 'root_id'
    root = Node(root_id)
    Mindmap_dto.save(root_id, root)
    
    expectedOutputFilePath = Path('data/root_id.pickle')
    assert expectedOutputFilePath.exists()
    assert cmp(expectedOutputFilePath, Path('test/resource/root_id.pickle'), shallow=False)


def test_load():
    root_id = 'root_id'
    expected_root = Node(root_id)

    root = Mindmap_dto.load(root_id)

    assert str(root) == str(expected_root)
