from setuptools import setup


setup(
    name='corputil',
    version='0.7.0',
    packages=['corputil'],
    package_data={'corputil': ['stopwords/*.txt']},
    install_requires=['nltk'],
    url='',
    license='',
    author='Sascha Can',
    author_email='Sascha.Can@gmail.com',
    description=''
)
