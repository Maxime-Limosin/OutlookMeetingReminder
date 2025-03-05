# Project Title
[![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://en.cppreference.com/w/cpp/language)
[![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)](https://doc.qt.io/qt-5/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)](https://www.debian.org/)

One Paragraph of the project description.

**If you need help for the markdown syntax**, you can click [here](https://www.markdownguide.org/cheat-sheet/).

## Purpose of the application
My super app is capable of:
* blabla
* blablabla

<br/>

Here's some cool data about the app: 
| id | name    | favoriteDish | favoriteLanguage |   |
|----|---------|--------------|------------------|---|
| 0  | Maxime  | Burgers      | C#               |   |
| 1  | Bastian | Bananas      | Python           |   |
| 2  | Fanny   | Pastas       | C++              |   |
| 3  | Batman  | Pizzas       | Violence         |   |

## Download the project
From your terminal or from git bash:
```bash
git clone <repository-url>
cd <repository-folder>
```

## Set up the environment
Add the following variables to your environment:
* Set QT_PATH to /home/[your username]/Qt
* Set QT_VERSION to 5.15.0

## Install the depencies

### Boost
    sudo apt install libboost-all-dev

### ffmpeg
    sudo apt install ffmpeg

    sudo usermod -a -G dialout $USER


### Python project - Ubuntu
```bash
# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the required packages
pip3 install -r requirements.txt

# Run the main.py file
python main.py
```

### Python project - Windows
```bash
:: Create a virtual environment
python3 -m venv myenv

:: Activate the virtual environment
myenv\Scripts\activate

:: Install the required packages
pip3 install -r requirements.txt

:: Run the main.py file
python3 main.py
```

## Run the application

### Ubuntu
```bash
# Run the main file
python3 main.py

# Create the build folder
mkdir build
cd build

# Configure and build the project
cmake ..
make

# Run the application
./applicationName
```

### Windows
```bash
# Run the main file
python3 main.py

# Create the build folder
mkdir build
cd build

# Configure and build the project
cmake .. -G "MinGW Makefiles"
mingw32-make

# Run the application
./applicatioName
```
## Usage
You can run the application with the following flags:
* --debug: to use a debug data base
* --headless: to start the app without a GUI

To analyse the logs, drop them in the following folder:

    applicationName/myFolder/logs
