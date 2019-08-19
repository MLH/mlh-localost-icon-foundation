# Blockchain Casino: Learning to SCORE

In this fun workshop, students can learn how to build a Slot Machine application where user's bet ICX to play the game, and will either gain or lose ICX based on the outcome. This is a great workshop that aligns well with the content you all already have so it will give students a great jumping off point. The workshop will walk users through on how to set up a wallet on the Blockchain, display their current balance, bet ICX (Send Transactions) and receive transactions (Wins) all via a front-end. Participants will set up and work with T-Bears to generate a project template for SCORE. They will then code and test the smart contract locally in an emulated environment, and when ready, deploy SCORE onto the ICON network (Testnet) via the command-line interface.

## Requirements and dependencies

### Docker

The only required dependency to run the project is docker.

### Used in the project

- [Python3](https://www.python.org/) - We recommend using virtual environments. They will help on the creation of isolated environments so different python versions can run on the same machine. Check more about virtual environments [here](https://docs.python.org/3/library/venv.html). (Needs to be installed manually)
- [Pip](https://pip.pypa.io/en/latest/installing/) - The python package manager. (Needs to be installed manually)
- [Flask](http://flask.pocoo.org/) - A simple and flexible Python Web Framework that provides with tools, libraries and technologies to build a web application. (Installed by pip)
- [iconsdk](https://github.com/icon-project/icon-sdk-python) - Official ICON SDK for Python based on ICON JSON RPC API V3. (Installed by pip)
- [tbears](https://www.icondev.io/docs/tbears-overview) - T-Bears is a suite of development tools for SCORE. [Installation](https://www.icondev.io/docs/tbears-installation)


## Clone the project

Use the command below:

```sh
git clone https://github.com/MLH/mlh-localost-icon-foundation.git
```

## Setup


### docker

Follow [this guide](https://docs.docker.com/get-started/) to install docker

## SCORE's Smart Contract

All the commands in this section should run from the docker container


### Run the tbears containers

```sh
docker run -it -p 9000:9000 $(docker build -t mlh-localhost-icon-tbears -q . -f Dockerfile.tbears)
```

After running this, it will output the `CASINO_SCORE_ADDRESS`. Copy this value and use it in your `.env` file.

### Deployment to local tbears instance

note: use **test1_Account** as password

```sh
# Make sure you are inside the docker tbears container
tbears deploy slot-machine -k keystores/keystore_test1.json -c config/tbears_cli_config.json
tbears txresult txnhash
tbears call -c config/tbears_cli_config.json testcmdline/call.json
tbears sendtx -k keystores/keystore_test1.json -c config/tbears_cli_config.json testcmdline/send_set_treasury.json
tbears sendtx -k keystores/keystore_test1.json -c config/tbears_cli_config.json testcmdline/send_bet.json
```

### Deployment to testnet

note: use **p@ssword1** as password

```sh
# Make sure you are inside the docker tbears container
tbears deploy -t tbears slot-machine -f hxe9d75191906ccc604fc1e45a9f3c59fb856c215f -k keystores/keystore1.json -c config/tbears_cli_config_testnet.json
tbears txresult txhash -c config/tbears_cli_config_testnet.json
```

- Testnet tracker https://bicon.tracker.solidwallet.io/ put the score address

- Iconex extension in chrome browser. Create a wallet and get wallet address


## WebApp

### Environment Variables

Run the following command to create webapp's .env file.

```sh
cp webapp/.env.example webapp/.env
```

Replace the `CASINO_SCORE_ADDRESS` with the address you got from the deployment of the contract.

### Executing the web application

From the root folder, run the following command:

```sh
docker run --env-file=webapp/.env -p 5000:5000 $(docker build -t mlh-localhost-icon -q . -f Dockerfile.webapp)
```

Then open [http://localhost:5000/](http://localhost:5000/) to see the application.
