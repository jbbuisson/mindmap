from mindmap import *

# More an integration test than a unit test...
def test_prettyPrintMap(capsys):
    rootId = 'root_id'
    createMap(rootId)

    addNodes(rootId, "I/like/potatoes", text='Because reasons')
    addNodes(rootId, "I/like/pineapples", text="Don't you ?")
    addNodes(rootId, "I/eat/tomatoes", text='Because the test says so')
    addNodes(rootId, "I/eat/tomatoes/for/breakfast")
    addNodes(rootId, "I/eat/tomatoes/for/breakfast")
    addNodes(rootId, "I/eat/tomatoes/for/dinner", text='Everybody does!')

    prettyPrintMap('root_id', renderText=False)
    captured = capsys.readouterr()
    assert captured.out == "root/\n    I/\n        like/\n            potatoes/\n            pineapples/\n        eat/\n            tomatoes/\n                for/\n                    breakfast/\n                    dinner/\n"
