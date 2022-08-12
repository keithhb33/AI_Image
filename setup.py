from setuptools import setup, find_packages


setup(
    name='ai_images',
    version='0.6',
    author="Keith Burroughs",
    author_email='keithburroughs33@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/keithhb33/AI-Image-Bot/',
    keywords='AI Images',
    install_requires=[
          'scikit-learn',
      ],

)
