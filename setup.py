from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='ANCE',
    version='0.1.0',
    description='Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval',
    url='https://github.com/microsoft/ANCE',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    packages=['ance', 'ance.data', 'ance.drivers', 'ance.model', 'ance.utils'],
    license="MIT",
    long_description=readme,
    install_requires=[
#        'transformers==2.3.0', 
        'transformers==3.0.2', 
        'pytrec-eval',
        #'faiss-cpu',
        'wget',
        'torch'
    ],
)
