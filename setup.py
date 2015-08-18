from distutils.core import setup

setup(
    name='mc_xclip',
    version='0.2.1',
    description='Syncs clipboards of Midnight Commander and X Window System.',
    long_description='''
Install::

    sudo apt-get install xclip
    sudo pip install mc_xclip

    # If you use Display Manager:
    echo 'mc_xclip &' >> ~/.xprofile

    # Else:
    echo 'mc_xclip &' >> ~/.xinitrc

    # Reboot.

''',
    url='https://github.com/denis-ryzhkov/mc_xclip',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    scripts=[
        'scripts/mc_xclip',
    ],
)
