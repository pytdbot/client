from re import findall
from setuptools import setup, find_packages


with open("pytdbot/__init__.py", "r") as f:
    version = findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = [x.strip() for x in f.readlines()]


setup(
    name="Pytdbot",
    version=version,
    description="Easy-to-use asynchronous TDLib wrapper for Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="AYMEN Mohammed",
    author_email="let.me.code.safe@gmail.com",
    url="https://github.com/pytdbot/client",
    license="MIT",
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "tdjson": ["tdjson"],
    },
    project_urls={
        "Source": "https://github.com/pytdbot/client",
        "Tracker": "https://github.com/pytdbot/client/issues",
    },
    packages=find_packages(exclude=["examples"]),
    package_data={
        "pytdbot": ["td_api.*"],
    },
    keywords=[
        "telegram",
        "tdlib",
        "bot",
        "telegram-client",
        "telegram-bot",
        "bot-api",
        "telegram-bot",
        "tdlib-python",
        "tdlib-bot",
    ],
)
