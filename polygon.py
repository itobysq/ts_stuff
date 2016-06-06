class PolyTest(object):
    """
    A class of different tests for _is_point_in_poly (which needed some work to be
    brought up to PEP-8!
    """
    def __init__(self):
        pass

    def test_square(self):
        """
        Tests a very basic case where the polygon is a square with side length = 2
        and the point is at the origin. This test case is important because
        the xints statement is called only once.
        :return: True (the point is indeed inside of the polygon)
        """
        return self._is_point_in_poly(0, 0, [(1, 1), (1, -1), (-1, -1), (-1, 1)])

    def test_outside(self):
        """
        Tests when the point is outside the polygon. This case is designed to run the path
        where the xints is called an even number of times.
        :return: False
        """
        return self._is_point_in_poly(-2, 0, [(1, 1), (1, -1), (-1, -1), (-1, 1)])

    def test_outside_y(self):
        """
        Tests the path where xints is called 0 times (a ray never passes through the polygon).
        :return: False
        """
        return self._is_point_in_poly(0, 2, [(1, 1), (1, -1), (-1, -1), (-1, 1)])

    def test_online(self):
        """
        Tests the case where the point is on the line. This is important because
        we need to have a boundary test.
        :return: True
        """
        return self._is_point_in_poly(0, 1, [(1, 1), (1, -1), (-1, -1), (-1, 1)])

    def test_no_points(self):
        """
        Tests the case where the for loop is not entered - important for path completion.
        :return: IndexError (but really this should give a more informative error)
        """
        return self._is_point_in_poly(0, 1, [])

    def _is_point_in_poly(self, x, y, poly):
        """
        Method to see if a point is inside of a polygon. This method uses the ray casting method.
        :param x: The x coordinate of the point in consideration.
        :param y: The y coordinate of the point in consideration.
        :param poly: A list of (x, y) coordinates.
        :return: A boolean representing whether or not the point is inside of the polygon.
        """
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n+1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (y - p1y) * (p2x - p1x)/(p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

if __name__ == '__main__':
    my_test = PolyTest()
    print(my_test.test_outside_y())
