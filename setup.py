from setuptools import setup
from setuptools import find_packages

package_dir = "src"

setup(name='fourierseries',
      version="1.0.0",
      description="Fourier series expansion",
      package_dir={
            "": package_dir
      },
      packages=find_packages(package_dir),
      package_data={
      },
      install_requires=[
        "numpy",
        "scipy"
      ],
      entry_points={
            "console_scripts": [
            ]
      },
      author="Taishi Hashimoto",
      author_email="hashimoto.taishi@outlook.com")
