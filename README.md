# Blockchain Casino: Learning to SCORE

In this fun workshop, students can learn how to build a Slot Machine application where user's bet ICX to play the game, and will either gain or lose ICX based on the outcome. This is a great workshop that aligns well with the content you all already have so it will give students a great jumping off point. The workshop will walk users through on how to set up a wallet on the Blockchain, display their current balance, bet ICX (Send Transactions) and receive transactions (Wins) all via a front-end. Participants will set up and work with T-Bears to generate a project template for SCORE. They will then code and test the smart contract locally in an emulated environment, and when ready, deploy SCORE onto the ICON network (Testnet) via the command-line interface.

## Requirements and dependencies

- [Python3](https://www.python.org/) - We recommend using virtual environments. They will help on the creation of isolated environments so different python versions can run on the same machine. Check more about virtual environments [here](https://docs.python.org/3/library/venv.html). (Needs to be installed manually)
- [Pip](https://pip.pypa.io/en/latest/installing/) - The python package manager. (Needs to be installed manually)
- [Flask](http://flask.pocoo.org/) - A simple and flexible Python Web Framework that provides with tools, libraries and technologies to build a web application. (Installed by pip)
- [iconsdk](https://github.com/icon-project/icon-sdk-python) - Official ICON SDK for Python based on ICON JSON RPC API V3. (Installed by pip)
- [tbears](https://www.icondev.io/docs/tbears-overview) - T-Bears is a suite of development tools for SCORE. [Installation](https://www.icondev.io/docs/tbears-installation)

## Clone the project

Use the command below:

```sh
git clone https://github.com/MLH/localhost-score.git
```

## Setup python and pyenv

### pyenv

Follow [this guide](https://github.com/pyenv/pyenv) to install pyenv and install python 3

```sh
pyenv install 3.7.1
```

### create and activate virtual environment

```sh
# setup the python pyenv virtual development environment
pyenv virtualenv localhost-icon
pyenv activate localhost-icon
source bin/activate
```

## WebApp

### Install dependencies

The next step is to install the dependencies used by the project. Run the following command:

```sh
cd webapp
pip install -r requirements.txt
```

### Executing the web application

After having all the dependencies installed, you only need to execute the main application file. In this case it will be the file "main.py"

```sh
cd webapp
python main.py
```

Then open [http://localhost:5000/](http://localhost:5000/) to see the application.

## SCORE's Smart Contract

### Install dependencies

#### T-bears (Install T-Bears with PIP)

Follow [this guide](https://www.icondev.io/docs/tbears-installation#section-install-t-bears-with-pip).

##### Known issue

When trying to install t-bears on MacOS, you may need to follow this workaround.

```sh
brew install leveldb
mv /Applications/Xcode.app /Applications/Xcode_cp.app
ls -la /Applications/ | grep Xcode*

leveldb_version=$(ls /usr/local/Cellar/leveldb/ | tail -1)
CFLAGS="-mmacosx-version-min=10.7 -stdlib=libc++" \
pip install tbears \
--no-cache-dir \
--global-option=build_ext \
--global-option="-I/usr/local/Cellar/leveldb/${leveldb_version}/include/" \
--global-option="-L/usr/local/lib"

mv /Applications/XCode_cp.app /Applications/Xcode.app
ls -la /Applications/ | grep Xcode*
```

[Source](https://github.com/wbolster/plyvel/issues/66)

### Deployment to local tbears instance

note: use **test1_Account** as password

```sh
tbears deploy slot-machine -k keystores/keystore_test1.json -c config/tbears_cli_config.json
tbears txresult txnhash
tbears call -c config/tbears_cli_config.json testcmdline/call.json
tbears sendtx -k keystores/keystore_test1.json -c config/tbears_cli_config.json testcmdline/send_set_treasury.json
tbears sendtx -k keystores/keystore_test1.json -c config/tbears_cli_config.json testcmdline/send_bet.json
```

### Deployment to testnet

note: use **p@ssword1** as password

```sh
tbears deploy -t tbears slot-machine -f hxe9d75191906ccc604fc1e45a9f3c59fb856c215f -k keystores/keystore1.json -c config/tbears_cli_config_testnet.json
tbears txresult txnhash -c config/tbears_cli_config_testnet.json
```

- Testnet tracker https://bicon.tracker.solidwallet.io/ put the score address

- Iconex extension in chrome browser. Create a wallet and get wallet address
