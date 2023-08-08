import unittest
from transpiler.others_module.import_package import Mod, Use


class test_import_package(unittest.TestCase):
    def test_mod(self):
        mod = Mod('test').get()
        print(mod)
        self.assertTrue(mod, "mod test;")

    def test_use_dep_std(self):
        use = Use().standard_library
        print(use)
        self.assertTrue(use, "use dep::std;")

    def test_use_dep_std_println(self):
        use = Use().standard_library_println
        print(use)
        self.assertTrue(use, "use dep::std::println;")

    def test_use_define_custom_use(self):
        use = Use()
        use.define_custom_use("std::hash")
        print(use.custom_use)
        self.assertTrue(use.custom_use, "use std::hash;")


if __name__ == '__main__':
    unittest.main()
