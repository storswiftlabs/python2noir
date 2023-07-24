import unittest
from transpiler.others_module.import_package import Mod, Use


class test_import_package(unittest.TestCase):
    def test_mod(self):
        mod = Mod('test').get()
        print(mod)

    def test_Use(self):
        use = Use('println').get()
        print(use)


if __name__ == '__main__':
    unittest.main()
