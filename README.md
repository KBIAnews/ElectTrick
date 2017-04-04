# ElectTrick
Embeddable election dashboards and visualizations, powered by Django.

## Requirements and Assumptions
This project's documentation and automated build tools assume a few things about your system:
- You have [GNU-Make](https://www.gnu.org/software/make/), GCC, Git, Python 2, [NodeJS and NPM](https://nodejs.org/en/) installed. On Ubuntu, running `sudo apt-get install build-essential` as a first step is _highly_ recommended.
- You have VirtualEnv and VirtualEnvWrapper set up (for Python 2).
- You're using bash for your system shell and your shell sources `~/.bashrc` on startup.

## Setup and Installation
1. Clone this repository.
2. Make a virtual environment for ElectTrick, ideally called electtrick: `mkvirtualenv electtrick`
3. Install all the Python requirements: `pip install -r requirements.txt`
4. Set up your environment variables. The easiest way to do this is use the assistant that comes in the project makefile: `make init`
5. Source your .bashrc again to grab those environment variables: `source ~/.bashrc`
