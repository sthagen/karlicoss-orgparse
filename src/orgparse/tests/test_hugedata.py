import pickle

from .. import loadi


def generate_org_lines(num_top_nodes, depth=3, nodes_per_level=1, _level=1):
    if depth == 0:
        return
    for i in range(num_top_nodes):
        yield ("*" * _level) + f' {i}-th heading of level {_level}'
        yield from generate_org_lines(
                nodes_per_level, depth - 1, nodes_per_level, _level + 1)


def num_generate_org_lines(num_top_nodes, depth=3, nodes_per_level=1):
    if depth == 0:
        return 0
    return num_top_nodes * (
        1 + num_generate_org_lines(
            nodes_per_level, depth - 1, nodes_per_level))


def test_picklable() -> None:
    num = 1000
    depth = 3
    nodes_per_level = 1
    root = loadi(generate_org_lines(num, depth, nodes_per_level))
    assert sum(1 for _ in root) == num_generate_org_lines(num, depth, nodes_per_level) + 1
    pickle.dumps(root)  # should not fail
