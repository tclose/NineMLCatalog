import sys
import os.path
from unittest import TestCase
import traceback
import ninemlcatalog


class TestLoadCatalog(TestCase):

    repo_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    xml_root = os.path.join(repo_root, 'xml')

    def setUp(self):
        with open(os.path.join(self.repo_root, '.gitignore')) as f:
            self.gitignore = list(f)

    def iterate_paths(self, dirname):
        """
        Descencds into the file directory tree and yields every path
        ending with 'xml'
        """
        for f in os.listdir(dirname):
            if not f.startswith('.') and f not in self.gitignore:
                pth = os.path.abspath(os.path.join(dirname, f))
                if os.path.isdir(pth):
                        for p in self.iterate_paths(pth):
                            yield p
                elif f.endswith('.xml'):
                    yield pth[len(self.xml_root):-4]

    def test_load_all(self):
        errors = []
        for pth in self.iterate_paths(self.xml_root):
            # Just check to see whether all elements of the document load
            # without error
            try:
                _ = list(ninemlcatalog.load(pth).elements)
            except Exception:
                errors.append(
                    (pth, traceback.format_exception(*sys.exc_info())))
        self.assert_(
            not errors,
            "The following failures occured while attempting to load all "
            "models from the catalog:\n\n{}"
            .format('\n\n'.join("{}\n---\n{}".format(pth, '\n'.join(trace))
                                for pth, trace in errors)))
