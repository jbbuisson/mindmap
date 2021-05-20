from anytree import AbstractStyle, Node, RenderTree

from mindmap_dto import Mindmap_dto


def createMap(map_id:str, text:str = '') -> Node:
    return Mindmap_dto.save(map_id, Node('root', text=text))


def pretty_print_map(map_id:str, render_text:bool = "False") -> None:
    root = Mindmap_dto.load(map_id)

    for pre, _, node in RenderTree(root, style=AbstractStyle(u'    ', u'    ', u'    ')):
        text = ''
        if render_text and len(node.text) > 0:
            text = ' \t\t--> ' + node.text

        print("%s%s/%s" % (pre, node.name, text))

        # JBB
        # FAIRE UN RETURN ET PAS UN PRINT !!!

def add_nodes(mapId:str, names:str, text:str = '') -> None:
    root = Mindmap_dto.load(mapId)
    names = names.split(sep='/')

    add_leaf(root, names, text)
    Mindmap_dto.save(mapId, root)


def add_leaf(parent:Node, names:list, text:str = ''):
    # The same node has been added a second time, the text will be updated
    if len(names) == 0:
        parent.text = text
        return

    for child in parent.children:
        if child.name == names[0]:
            add_leaf(child, names[1:], text)
            return

    # names[0] is not a child of parent, create a new node
    new_node = Node(names[0], parent, text='')

    if len(names) > 1:
        add_leaf(new_node, names[1:], text=text)
    else:
        new_node.text = text


def get_leaves(mapId:str, names:str):
    root = Mindmap_dto.load(mapId)
    names_split = names.split(sep='/')

    text = get_leaf(root, names_split)
    leaf = {}
    leaf['path'] = names
    leaf['text'] = text

    return leaf

def get_leaf(parent:Node, names:list):
    for child in parent.children:
        if child.name == names[0]:
            if len(names) == 1:
                return child.text
            else:
                return get_leaf(child, names[1:])

    # at least one name is not a node of the mindmap
    # empty string is returned
    return ''
