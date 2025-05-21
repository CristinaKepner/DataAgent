from setuptools import setup, find_packages

setup(
    name="dataagent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'numpy',
        'opencv-python',
        'segment-anything'
    ]
)