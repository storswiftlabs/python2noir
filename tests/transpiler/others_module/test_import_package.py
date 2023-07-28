import unittest
from transpiler.others_module.import_package import Mod, Use


class test_import_package(unittest.TestCase):
    def test_mod(self):
        mod = Mod('test').get()
        print(mod)
        self.assertTrue(mod, "mod test;")

    def test_Use(self):
        use = Use()
        print(use.standard_library)
        self.assertTrue(use.standard_library, "use dep::std;")


if __name__ == '__main__':
    unittest.main()
