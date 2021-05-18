import pickle
from pathlib import Path

from anytree import AbstractStyle, Node, RenderTree

def getRoot(mapId:str) -> Node:
    # if mapId not in mindMaps.keys():
    #     print(f'Mindmap with id = {mapId} does not exist!')
    #     raise KeyError

    # return mindMaps[id]
    return load(mapId)


def createMap(mapId:str, text:str = '') -> Node:
    # if mapId in mindMaps:
    #     print(f'Mindmap with id = {mapId} already exists!')
    #     raise KeyError

    # mindMaps[mapId] = Node(mapId, text=text)

    # return mindMaps[mapId]
    return save(mapId, Node('root', text=text))


def prettyPrintMap(mapId:str, renderText:bool = "False") -> None:
    root = getRoot(mapId)

    for pre, _, node in RenderTree(root, style=AbstractStyle(u'    ', u'   /', u'   /')):
        text = ''
        if renderText and len(node.text) > 0:
            text = ' \t\t--> ' + node.text

        print("%s%s%s" % (pre, node.name, text))


def addNodes(mapId:str, names:str, text:str = '') -> None:
    root = getRoot(mapId)
    names = names.split(sep='/')

    addLeaf(root, names, text)
    save(mapId, root)

def addLeaf(parent:Node, names:list, text:str = ''):
    for child in parent.children:
        if child.name == names[0]:
            if len(names) > 1:
                addLeaf(child, names[1:], text)
            return

    # The same node has been added a second time, the text will be updated
    if len(names) == 0:
        parent.text = text
        return

    # currentName is not a child of parent, create a new node
    nextNode = Node(names[0], parent, text='')
    if len(names) > 1:
        addLeaf(nextNode, names[1:], text=text)
    else:
        nextNode.text = text


def getLeaves(mapId:str, names:str):
    root = getRoot(mapId)
    names_split = names.split(sep='/')

    # return getLeaf(root, names_split)
    text = getLeaf(root, names_split)
    leaf = {}
    leaf['path'] = names
    leaf['text'] = text

    return leaf

def getLeaf(parent:Node, names:list):
    for child in parent.children:
        if child.name == names[0]:
            if len(names) == 1:
                return child.text
            else:
                return getLeaf(child, names[1:])

    # at least one name is not a node of the mindmap
    # TODO What to return when at least one name is not found
    return ''


###############################
# Data persistence
###############################
def getFileName(mapId:str) -> Path:
    path = Path('./data/')
    if not path.exists():
        path.mkdir()
    return path / (mapId + '.pickle')


def save(mapId:str, root:Node):
    with getFileName(mapId).open(mode='wb') as file:
        pickle.dump(root, file)


def load(mapId:str) -> Node:
    with getFileName(mapId).open(mode='rb') as file:
        return pickle.load(file)

#################
# TEST
#################

# rootId = 'root_id'
# myroot = createMap(rootId)
# # myroot = load(rootId)

# addNodes(rootId, "I/like/potatoes", text='Because reasons')
# addNodes(rootId, "I/like/pineapples", text="Don't you ?")
# addNodes(rootId, "I/eat/tomatoes", text='Because the test says so')
# addNodes(rootId, "I/eat/tomatoes/for/breakfast")
# addNodes(rootId, "I/eat/tomatoes/for/dinner", text='Everybody does!')

# print(getLeaves(rootId, "I/like/potatoes"))
# print(getLeaves(rootId, "I/like/patates"))

# # print('----------------')
# # print(RenderTree(myroot))
# print('----------------')
# prettyPrintMap('root_id', renderText=False)
# print('----------------')
# prettyPrintMap('root_id', renderText=True)
# print('----------------')
