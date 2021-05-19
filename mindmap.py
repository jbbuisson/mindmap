from anytree import AbstractStyle, Node, RenderTree
from mindmap_dto import Mindmap_dto

def getRoot(mapId:str) -> Node:
    return Mindmap_dto.load(mapId)


def createMap(mapId:str, text:str = '') -> Node:
    return Mindmap_dto.save(mapId, Node('root', text=text))


def prettyPrintMap(mapId:str, renderText:bool = "False") -> None:
    root = getRoot(mapId)

    for pre, _, node in RenderTree(root, style=AbstractStyle(u'    ', u'    ', u'    ')):
        text = ''
        if renderText and len(node.text) > 0:
            text = ' \t\t--> ' + node.text

        print("%s%s/%s" % (pre, node.name, text))


def addNodes(mapId:str, names:str, text:str = '') -> None:
    root = getRoot(mapId)
    names = names.split(sep='/')

    addLeaf(root, names, text)
    Mindmap_dto.save(mapId, root)

def addLeaf(parent:Node, names:list, text:str = ''):
    # The same node has been added a second time, the text will be updated
    if len(names) == 0:
        parent.text = text
        return

    for child in parent.children:
        if child.name == names[0]:
            if len(names) > 1:
                addLeaf(child, names[1:], text)
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
