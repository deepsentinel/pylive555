========================================
PyLIVE555 - Wrapper of LIVE555
========================================


.. contents:: Table of Contents


Installation
========================================

By pip:

.. code-block:: sh

  pip3 install git+ssh://git@github.com/wdv4758h/pylive555.git@develop


From Source:

.. code-block:: sh

  $ git clone git@github.com:wdv4758h/pylive555.git
  $ cd pylive555
  $ python setup.py build
  $ python setup.py install



Run Examples
========================================

.. code-block:: sh

  # record 10 seconds H264 video from source 10.17.4.118 with channel 1,
  # and save to file out.264
  $ python3 examples/example.py  10.17.4.118 1 10 out.264
