# Python2Noir
Generate Noir code through python.

## Description

Easy to quickly convert python libraries to Noir contracts

## Directory structure

- tests: Testcase for transpiler
- transpiler: Python2Noir transpiler, include Noir language diffent module
  - context: Process the transformation context to build the complete Noir file
  - core_module: Include some core components such as struct and function
  - others_module: Include non-core statements
  - sub_module: Include some base components such as primitive type sign and key words
  - util: tools such as code format and logger 
  
## Build guide

- Python 3.7+
- Anaconda

## Import package

### linux
```shell
pip install setuptools
git clone https://github.com/storswiftlabs/python2noir.git
python setup.py sdist
pip install ./dist/python2noir-0.1.tar.gz
```
### windows
```shell
pip install setuptools
git clone https://github.com/storswiftlabs/python2noir.git
python setup.py bdist_wininst
# execute exe file
./python2noir-0.1.win-amd64.exe
```

## Example

```shell
# clone repository 
git clone https://github.com/storswiftlabs/python2noir.git
# execute testcase: python generated Noir code
python  -m unittest tests/transpiler/context/test_context.py
```
