from distutils.core import setup
import py2exe
setup(
    windows = [
        {
            "script": "wx-randorator.py",
            "icon_resources": [(1, "randorator.ico")]
        }
    ],
)
