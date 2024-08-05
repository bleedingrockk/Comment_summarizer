import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Comment_summarizer"
AUTHOR_USER_NAME = "bleedingrockk"
SRC_REPO = "comment_summarizer"
AUTHOR_EMAIL = "sureshsuthar438@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,  # Added this to include the author's email
    description="A comment analyzer tool",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected parameter name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
