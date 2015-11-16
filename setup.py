from setuptools import setup
from setuptools.command.install import  install as _install


def _post_install():
    import nltk
    nltk.download('punkt')


class Install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, msg='Running post install...')


setup(
    name='corputil',
    version='0.3.0',
    packages=['corputil'],
    package_data={'corputil': ['stopwords/*.txt']},
    install_requires=['nltk'],
    url='',
    license='MIT',
    author='Sascha Can',
    author_email='Sascha.Can@gmail.com',
    description='',
    cmdclass={'install': Install}
)
