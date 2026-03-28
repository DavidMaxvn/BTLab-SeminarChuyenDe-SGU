import unittest

from src.chapter13.rectangle import rect_intersection_area


class TestRectangleIntersectionArea(unittest.TestCase):
    def test_intersecting_rectangles(self):
        rect1 = (0, 0, 4, 4)
        rect2 = (2, 2, 6, 6)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_intersecting_rectangles_swapped(self):
        rect1 = (2, 2, 6, 6)
        rect2 = (0, 0, 4, 4)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_non_intersecting_rectangles(self):
        rect1 = (0, 0, 2, 2)
        rect2 = (3, 3, 5, 5)
        self.assertEqual(rect_intersection_area(rect1, rect2), 0)

    def test_touching_edges(self):
        rect1 = (0, 0, 2, 2)
        rect2 = (2, 0, 4, 2)
        self.assertEqual(rect_intersection_area(rect1, rect2), 0)

    def test_invalid_rect1(self):
        with self.assertRaises(ValueError):
            rect_intersection_area((2, 2, 1, 3), (0, 0, 1, 1))

    def test_invalid_rect2(self):
        with self.assertRaises(ValueError):
            rect_intersection_area((0, 0, 1, 1), (2, 2, 2, 5))


if __name__ == "__main__":
    unittest.main()
