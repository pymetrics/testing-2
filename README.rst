Tools for Testing
================

Tools for effectively testing Django applications.


To Run the Slides (Virtualenv)
------------------------------

1. If you don't already have python 3, run

   .. code:

       $ brew install python3

    (also, shame!)

2. Create a Virtualenv

   .. code:

       $ mkvirtualenv --python python3 testing

3. Install the requirements

   .. code:

       $ pip install -r requirements.txt

4. Start the Hovercraft! server:

   .. code:

       $ hovercraft presentation/slides.rst

5. Open http://localhost:8000 and enjoy.



To Run the Slides (Docker)
--------------------------

There's no real reason to use Docker, except the build chain on my PC is
FUBAR and I didn't have time to fix it.

::

    $ make image
    $ make

Open your browser to http://localhost:8000

To run individual tests when using docker, you have to get a shell in the container.
While it's running, run:

::

    $ docker exec -ti testing_hovercraft_1 bash

Then, ``cd`` to ``presentations/src/``.


Built with Hovercraft_ .

.. _Hovercraft: http://regebro.github.io/hovercraft/#/step-1
