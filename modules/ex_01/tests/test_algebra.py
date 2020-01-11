from mathematica.algebra import matrices

def test_add_matrices():
    m1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    m2 = [
        [6,5,0],
        [1,3,9],
        [0,2,1]
    ]

    assert matrices.add_matrices(m1,m2) == [[7, 7, 3], [5, 8, 15], [7, 10, 10]]