import unittest

from transpiler.others_module import Annotation
from transpiler.others_module.import_package import Mod, Use


class test_annotation(unittest.TestCase):
    def test_get_content(self):
        annotation = Annotation(0, 'my test annotation')
        print(annotation.get_content())
        self.assertTrue(annotation.get_content(), "// my test annotation")


if __name__ == '__main__':
    unittest.main()
