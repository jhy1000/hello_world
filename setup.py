import re
import io

from setuptools import setup


with io.open('helloworld/__init__.py', encoding='utf-8') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)


with io.open('README.rst', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='helloworld-python',
    version=version,
    description='Say hello to the world or to a specific person.',
    long_description=readme,
    url='https://github.com/dwayne/helloworld-python',
    author='Dwayne Crooks',
    author_email='me@dwaynecrooks.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    keywords='hello helloworld',
    packages=['helloworld'],
    entry_points={
        'console_scripts': [
            'hello=helloworld.core:main'
        ]
    }
)
