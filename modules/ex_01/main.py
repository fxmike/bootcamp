from mathematica.algebra import matrices
from mathematica.geometry import figures


def main():
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
    print(matrices.add_matrices(m1,m2))
    print(matrices.sub_matrices(m1,m2))
    print(figures.square_area(2))
    print(figures.triangle_area(6,3))



if __name__ == "__main__":
    main()