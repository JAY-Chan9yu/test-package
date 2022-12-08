import setuptools

setuptools.setup(
    name="test jay",
    version="1.0.0",
    author="jay.ji",
    author_email="test@gmail.com",
    description="backend service common modules package",
    long_description_content_type="text/markdown",
    url="<https://github.com/JAY-Chan9yu/test-package",
    packages=setuptools.find_packages(where=".", exclude=("tests", "*.tests")),
    python_requires=">=3.6",
    install_requires=[],
)
