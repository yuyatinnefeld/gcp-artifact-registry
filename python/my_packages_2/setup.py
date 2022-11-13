import setuptools


def version():
    """
    retrieves the version number of the current project
    
    Returns:
        version number
    """
    with open('VERSION') as f:
        return f.read()


setuptools.setup(
    version=version(),
    packages=['frontend_lib'],
    python_requires=">=3.7",
)