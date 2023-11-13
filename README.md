# flaskchat 

This is flaskchat, which uses multiple LLM models to write stories, or have philosophical discussions, or anything else you want to set the prompts for. 

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

Two parts, flaskapi_gpt.py and main.py (or the variations that use different backend storage.)

Uses [openai](https://openai.com) and [cohere](https://cohere.com) as these are some good models with reasonable api prices.

## Getting Started
1. 
```python 
python main.py # for list storage
python main-mongoback.py # for mongodb or ferretdb backend
python main-redisback.py # for redis backend
```
In seperate window:

```python
python flaskapi_gpt.py # for main application 
```
### Prerequisites

- python >= 3.9
- cohere and openai api keys
- cohere (python client)
- openai (python client) 
- redis server as available
- mongodb server as available

### Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/jtatman/flaskchat.git
  ```
2. Create a virtual environment

  Use micromamba, why not?
  ```bash
  "${SHELL}" <(curl -L micro.mamba.pm/install.sh)
  micromamba create -n flaskchat python=3.9 
  ```
  or venv
  ```bash
  python -m venv .venv
  ```

3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Assumes mongo and redis run in servers at localhost or docker. If not, adjust in respective files. 

5. Docker or podman

  TODO
