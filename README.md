# web-crawler
A simple web crawler in Python

## Version Management
You are encouraged to use pyenv for version management. his allows each developer to install and switch between multiple Python versions and ensures the project always runs on the intended version.

Add a .python-version file to your repository (automatically created by pyenv) so that anyone who clones the repository will use the right version.
```shell
% cat .python-version
3.13.2
```

## Dependency Management
It is recommended to use ```pyproject.toml``` as the single source of truth for the project. Always create and manage self-contained virtual environments for your python projects.

### Install PDM
```shell
brew install pdm
pdm --version
```

### Initialize a new project
```shell
pdm init
```

### Make sure you have the latest SSL:
```shell
brew install openssl@3
```

### Adding dependencies
```shell
pdm add requests  # Example dependency
pdm add BeautifulSoup # Example dependency
```

### Running a Script
```shell
pdm run python simple-webcrawler.py
```