from setuptools import setup
#import py2exe

with open('downstream_farmer/version.py','r') as f:
    exec(f.read())
    
setup(
    name='downstream-farmer',
    version=__version__,
    packages=['downstream_farmer'],
    url='https://github.com/mstg/downstream-farmer',
    license='MIT',
    author='Storj Labs',
    author_email='info@storj.io',
    description='Client software for a Storj farmer',
    install_requires=[
        'six',
        'requests',
        'base58',
        'RandomIO',
        'storj-heartbeat',
        'siggy'
    ],
    entry_points={
        'console_scripts': [
            'downstream = downstream_farmer.shell:main'
        ]
    }
)
