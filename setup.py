from setuptools import setup
from setuptools.command.install import install


def _post_install():
    import site
    from importlib import reload
    reload(site)
    import nltk
    nltk.download('punkt')


class Install(install):
    def run(self):
        install.run(self)
        self.execute(_post_install, [], msg='Running post install...')


setup(
    name='corputil',
    version='0.3.0',
    packages=['corputil'],
    package_data={'corputil': ['stopwords/*.txt']},
    setup_requires=['nltk'],
    url='',
    license='MIT',
    author='Sascha Can',
    author_email='Sascha.Can@gmail.com',
    description='',
    cmdclass={'install': Install}
)
