import harfang as hg

def test_pos_vs_nodes_table(node_pos, nodes_table, max_dist):
    return next(
        (
            idx
            for idx, nd in enumerate(nodes_table)
            if hg.Dist(node_pos, nd["pos"]) < max_dist
            and nd["node"].IsEnabled()
        ),
        -1,
    )

