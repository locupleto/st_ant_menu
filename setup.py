import setuptools

with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name="st_ant_menu",
    version="0.0.20",
    author="Urban Ottosson",
    author_email="urban@ottosson.org",
    description="Streamlit Component for ANT Menu with Bootstrap icon support",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/locupleto/st_ant_menu",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)