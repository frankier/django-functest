from .funcselenium import FuncSeleniumMixin
from .funcwebtest import FuncWebTestMixin
from .utils import AdminLoginMixin, ShortcutLoginMixin
from .files import Upload

__version__ = '0.1.5-dev'

__all__ = ['FuncWebTestMixin', 'FuncSeleniumMixin', 'ShortcutLoginMixin', 'AdminLoginMixin', 'Upload']
