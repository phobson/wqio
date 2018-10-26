from pkg_resources import resource_filename
import warnings

import wqio
from .helpers import requires

try:
    import pytest
except ImportError:
    pytest = None


@requires(pytest, 'pytest')
def test(*args):
    options = [resource_filename('wqio', '')]
    options.extend(list(args))
    return pytest.main(options)


@requires(pytest, 'pytest')
def teststrict(*args):
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        options = [
            '--pep8', '--mpl', '--doctest-modules',
            *list(args)
        ]
        return test(*list(set(options)))
