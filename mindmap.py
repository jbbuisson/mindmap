from anytree import Node, RenderTree, AbstractStyle

mindMaps = {}

def getRoot(id:str) -> Node:
    if id not in mindMaps.keys():
        print(f'minmap with id = {id} does not exist!')
        raise KeyError

    return mindMaps[id]


def createMap(mapId:str, text:str = '') -> Node:
    if mapId in mindMaps:
        print(f'minmap with id = {mapId} already exists!')
        raise KeyError

    mindMaps[mapId] = Node(mapId, text=text)
    return mindMaps[mapId]

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

def addLeaf(parent:Node, names:list, text:str = ''):
    for child in parent.children:
        if child.name == names[0]:
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
    names = names.split(sep='/')

    return getLeaf(root, names)

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

# myTree = Tree('root_id')
# print(RenderTree(myTree))

# rootId = 'root_id'
# myroot = createMap(rootId)
# node100 = Node('node_100', myroot)
# node110 = Node('node_110', node100)
# node111 = Node('node_111', node110)
# node200 = Node('node_200', myroot)
# node210 = Node('node_210', node200)
# node211 = Node('node_211', node210)
# node212 = Node('node_212', node210)
# node220 = Node('node_220', node200)
# node221 = Node('node_221', node220)
# node222 = Node('node_222', node220)
# node223 = Node('node_223', node220)
# addNodes(rootId, "i/like/potatoes", text='Because reasons')
# addNodes(rootId, "i/like/pineapples", text="Don't you ?")
# addNodes(rootId, "i/eat/tomatoes", text='Because the test says so')

# print(getLeaves(rootId, "i/like/potatoes"))
# print(getLeaves(rootId, "i/like/patates"))

# print('----------------')
# print(RenderTree(myroot))
# print('----------------')
# prettyPrintMap('root_id', renderText=False)
# print('----------------')
# prettyPrintMap('root_id', renderText=True)
# print('----------------')