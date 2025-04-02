# web-crawler
A simple web crawler in Python

## Version Management
You are encouraged to use pyenv for version management. his allows each developer to install and switch between multiple Python versions and ensures the project always runs on the intended version.

### Install pyenv
```shell
curl https://pyenv.run | bash
```

### Alternatively, use the package manager:
```shell
brew install pyenv
```

### Python 13.x is recommended:
```shell
pyenv install 3.13.2
pyenv local 3.13.2
```

Add a .python-version file to your repository (automatically created by pyenv) so that anyone who clones the repository will use the right version.
```shell
% cat .python-version
3.13.2
```

Create a setup.py file and specify the python version:
```shell
# setup.py snippet
setup(
    ...
    python_requires='>=3.13, <3.14',
    ...
)
```

## Dependency Management
### Install Poetry
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

### Or with brew:
```shell
brew install poetry
```

### Initialize the project:
```shell
poetry init
```

### Make sure you have the latest SSL:
```shell
brew install openssl@3
```

### Make sure you have 3.10+
```shell
export LDFLAGS="-L$(brew --prefix openssl@3)/lib"
export CPPFLAGS="-I$(brew --prefix openssl@3)/include"
pyenv install 3.13.2
pyenv global 3.13.2
```
