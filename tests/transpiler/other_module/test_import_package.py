import unittest
from transpiler.others_module.import_package import Mod, Use


class test_import_package(unittest.TestCase):
    def test_mod(self):
        mod = Mod('test').get()
        print(mod)
        self.assertTrue(mod, "mod test;")

    def test_Use(self):
        use = Use().standard_library()
        print(use)
        self.assertTrue(use, "use dep::std;")


if __name__ == '__main__':
    unittest.main()
