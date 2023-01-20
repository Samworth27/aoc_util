import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name='aoc_util',
    version='0.0.29',
    author='Sam Mitchell',
    author_email='sam@xxvii.dev',
    description='Common modules used during Advent of Code',
    long_description=long_description,
    long_description_content_type='test/markdown',
    url="https://github.com/Samworth27/aoc_util",
    project_urls={
        "Bug Tracker": "https://github.com/Samworth27/aoc_util/issues"
    },
    license='MIT',
    packages=['aoc_util', 'aoc_util.grid_modules', 'aoc_util.graph_modules','aoc_util.graph_modules.tsp_graph'],
    install_requires=['numpy', 'pygame', 'pillow']
)
