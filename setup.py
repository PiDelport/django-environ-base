from setuptools import find_packages, setup


def README():
    with open('README.md') as f:
        return f.read()


setup(
    name='django-environ-base',
    description='A simple base settings file for projects using django-environ',
    url='https://github.com/pjdelport/django-environ-base',
    long_description=README(),
    long_description_content_type='text/markdown',

    author='Pi Delport',
    author_email='pjdelport@gmail.com',

    package_dir={'': 'src'},
    packages=find_packages('src'),

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    install_requires=[
        'django-environ',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
