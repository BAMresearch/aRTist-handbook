# aRTist Handbook

User guide for the radiographic simulator aRTist. Find the readable version here:

https://bamresearch.github.io/aRTist-handbook/

This is the source code of the documentation for aRTist. You need the Python package [Sphinx](https://www.sphinx-doc.org) to compile it.

The [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io) is required. To install it, use:

    pip install sphinx_rtd_theme


## Compile and deploy

The source files are all located in the `source` folder. To create the HTML documentation and store it in the `build` folder, run

    make html

Github Pages expects the HTML documentation in a folder called `docs`. You can run the compile script to automatically copy the content from `build/html` to `docs` and create the necessary `.nojekyll` file.

    deploy.bat (Windows)
    ./deploy.sh (Linux)