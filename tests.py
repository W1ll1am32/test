import unittest
import random
from tic_tac_toe import Game


def generate(n):
    moves = []
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            moves.append((r, c))
    random.shuffle(moves)
    return moves


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(0)

    def test_3x3_1(self):
        try:
            self.game.set_size(3)
            move_list = generate(3)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1)
        except Exception:
            self.fail("Caught exception")

    def test_3x3_2(self):
        try:
            self.game.set_size(3)
            move_list = generate(3)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1)
        except Exception:
            self.fail("Caught exception")

    def test_3x3_3(self):
        try:
            self.game.set_size(3)
            move_list = generate(3)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1)
        except Exception:
            self.fail("Caught exception")

    def test_3x3_4(self):
        try:
            self.game.set_size(3)
            move_list = generate(3)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1)
        except Exception:
            self.fail("Caught exception")

    def test_3x3_5(self):
        try:
            self.game.set_size(3)
            move_list = generate(3)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1)
        except Exception:
            self.fail("Caught exception")

    def test_4x4(self):
        try:
            self.game.set_size(4)
            move_list = generate(4)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1 or ret == -1)
        except Exception:
            self.fail("Caught exception")

    def test_5x5(self):
        try:
            self.game.set_size(5)
            move_list = generate(5)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1 or ret == -1)
        except Exception:
            self.fail("Caught exception")

    def test_nxn(self):
        try:
            n = random.randint(3, 10)
            self.game.set_size(n)
            move_list = generate(n)
            self.game.set_input(move_list)
            ret = self.game.start()
            self.assertTrue(ret == 0 or ret == 1 or ret == -1)
        except Exception:
            self.fail("Caught exception")


if __name__ == '__main__':
    unittest.main()
