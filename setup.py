from setuptools import setup

from os import path

here = path.abspath(path.dirname(__file__))

setup(
  name='tensorrec',
  packages=['tensorrec'],
  version='0.26.2',
  description='A TensorFlow recommendation algorithm and framework in Python.',
  author='James Kirk',
  author_email='james.f.kirk@gmail.com',
  url='https://github.com/jfkirk/tensorrec',
  keywords=['machine-learning', 'tensorflow', 'recommendation-system', 'python', 'recommender-system'],
  classifiers=[],
  dependency_links = [
    'https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.14.0-cp36-cp36m-linux_x86_64.whl'
  ],
  install_requires=[
      "numpy>=1.14.1",
      "scipy>=0.19.1",
      "six==1.11.0",
      "tensorflow_gpu>=1.14.0",
  ],
)
