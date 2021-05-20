from mindmap import *

# More an integration test than a unit test...
def test_prettyPrintMap(capsys):
    rootId = 'root_id'
    createMap(rootId)

    add_nodes(rootId, "I/like/potatoes", text='Because reasons')
    add_nodes(rootId, "I/like/pineapples", text="Don't you ?")
    add_nodes(rootId, "I/eat/tomatoes", text='Because the test says so')
    add_nodes(rootId, "I/eat/tomatoes/for/breakfast")
    add_nodes(rootId, "I/eat/tomatoes/for/breakfast")
    add_nodes(rootId, "I/eat/tomatoes/for/dinner", text='Everybody does!')

    pretty_print_map('root_id', render_text=False)
    captured = capsys.readouterr()
    assert captured.out == "root/\n    I/\n        like/\n            potatoes/\n            pineapples/\n        eat/\n            tomatoes/\n                for/\n                    breakfast/\n                    dinner/\n"
