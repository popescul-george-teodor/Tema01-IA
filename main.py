from scipy import spatial

from utils.utils import manhattan_distance


def main():

    with open("points.csv", "r") as file:
        points = [list(map(int, line.strip().split(","))) for line in file]

    p1 = points[0]
    p2 = points[1]
    print("P1=", *p1)
    print("P2=", *p2)
    print("Distance (Manhattan SciPy)= ", spatial.distance.cityblock(p1, p2))
    print("Distance (Manhattan Reimplemented)= ", manhattan_distance(p1, p2))
    print("Distance (Euclidean SciPy)= ", round(spatial.distance.euclidean(p1, p2)))


if __name__ == "__main__":
    main()
