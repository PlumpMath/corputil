from setuptools import setup


setup(
    name='corputil',
    version='0.3.4',
    packages=['corputil'],
    package_data={'corputil': ['stopwords/*.txt']},
    install_requires=['nltk', 'textblob-de'],
    url='',
    license='MIT',
    author='Sascha Can',
    author_email='Sascha.Can@gmail.com',
    description=''
)
