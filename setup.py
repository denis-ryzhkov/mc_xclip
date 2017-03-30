from distutils.core import setup

setup(
    name='mc_xclip',
    version='0.3.0',
    description='Syncs clipboards of Midnight Commander and X Window System.',
    long_description='''
**NEW:**

Don't use ``mc_xclip``! Instead:

* ``sudo apt-get install xclip``
* Make sure ``mc`` is NOT running, or it will overwrite the next changes.
* Find ``clipboard_store`` in ``~/.config/mc/ini``
* Set ``clipboard_store=xclip -i -selection clipboard``
* Set ``clipboard_paste=xclip -o -selection clipboard``
* Thanks to https://github.com/IvanAli

**OLD:**

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
