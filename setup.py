import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcp-injections",  # Replace with your own username
    version="0.1",
    author="Tommy Strand",
    author_email="github-projects@ireality.no",
    description="Logging configuration for Python with contrib for Django and Flask simplifying logging clean logs to stackdriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/injectedreality/stackdriverlog",
    packages=['stackdriverlog'],
    keywords='stackdriver django gcp logging gke',
    install_requires=[
        'structlog',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)