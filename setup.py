import os
import subprocess
from pathlib import Path
from distutils.core import setup, Extension


def build_live555(source):
  # NOTICE: it depends on some Unix-like commands
  # use subprocess.call instead subprocess.run for prior to Python 3.5
  filename = source.split('/')[-1]
  file = Path('{}/{}'.format(ROOT_DIR, filename))
  if not file.is_file():
    subprocess.call(['curl', '-O', source])
  if not Path(LIVE555_DIR).is_dir():
    subprocess.call(['tar', 'xvf', filename])
  subprocess.call('cd live && ./genMakefiles linux && CFLAGS=-fPIC CXXFLAGS=-fPIC make -j', shell=True)

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
LIVE555_SOURCE = 'http://www.live555.com/liveMedia/public/live555-latest.tar.gz'
LIVE555_DIR = '{}/live'.format(ROOT_DIR)
LIVE555_LIBS = ['liveMedia', 'BasicUsageEnvironment', 'UsageEnvironment', 'groupsock']
LIVE555_INCLUDE = ['{}/{}/include'.format(LIVE555_DIR, x) for x in LIVE555_LIBS]
LIVE555_LIBS_DIR = ['{}/{}'.format(LIVE555_DIR, x) for x in LIVE555_LIBS]

build_live555(LIVE555_SOURCE)

module = Extension('live555._live555',
                   include_dirs=LIVE555_INCLUDE,
                   libraries=LIVE555_LIBS,
                   # use C++11, in case the old compiler doesn't support C++14 ...
                   extra_compile_args=['--std=c++11', '-O3'],
                   # LTO optimization, and strip the binary
                   extra_link_args=['-s', '-flto'],
                   library_dirs=LIVE555_LIBS_DIR,
                   sources=['live555/module.cpp'])


setup(name='live555',
      version='0.0.1',
      description='wrapper of live555',
      url='https://github.com/wdv4758h/pylive555',
      packages=['live555'],
      ext_modules=[module])
