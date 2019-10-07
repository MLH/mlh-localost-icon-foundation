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

## Deployment

We will be using tbears cli to deploy and configure our aplication. For more information on the commands check [this link](https://www.icondev.io/docs/how-to-use-t-bears). The deployment of the game consists in two steps:

- **Deployment of the contract**: Deploy a new version of the contract to be used
- **Initializing funds**: Adds funds to the treasury

### Deployment to local tbears instance

The steps below are automatically done for you if you are using docker. But if you need/want to deploye manually, you can follow it.

note: use **test1_Account** as password

##### Deploying the contract

To deploy the contract, run:

```sh
# Make sure you are inside the docker tbears container
tbears deploy slot-machine # deploys a new version of the contract
```

note: Make sure to save the `SCORE_ADDRESS` that will be in the output.

##### Adding funds to the the treasury

In order to play the game, we first need to add funds to the treasury. To do that, open the file `testcmdline/send_set_treasury.json` and update the `params.to` attribute with the `SCORE_ADDRESS` you got from the deployment.

```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
    "value": "0xfff05b59d3b200000000",
    "stepLimit": "0x200000",
    "nid": "0x3",
    "nonce": "0x2",
    // UPDATE THE LINE BELOW WITH THE NEW SCORE ADDRESS
    "to": "cx4c83896ab77ee394a72761a39d7c332a6adc05c0",
    "dataType": "call",
    "data": {
      "method": "set_treasury"
    }
  },
  "id": 1
}
```

Then, we will go ahead and use tbears to invoke a command within the deployed contract. To do that, run:

```sh
# Make sure you are inside the docker tbears container
tbears sendtx -c config/tbears_cli_config.json testcmdline/send_set_treasury.json # Adds funds to the treasury
```

note: By default, these commands will use the account created when the tbears server is initialized as it contains all the funds. If you are deploying to a different network and/or wants to use a different wallet for that, make sure to update the `params.from` attribute.

#### More information

For more information about the deployment process (and also instructions on how to deploy to a different network), check [this link](https://www.icondev.io/docs/deploy-guideline#section-tbears-deploy-install).

## WebApp

### Environment Variables

Run the following command to create webapp's .env file.

```sh
cp webapp/.env.example webapp/.env
```

Replace the `CASINO_SCORE_ADDRESS` with the address you got from the deployment of the contract.

#### Using a different wallet

By default, the web app will use the test account that is created by the tbears server. If you want to use a different wallet, you will need your keystore file and your password.

- First, make sure to copy your keystore file to the `keystores` folder. (It's important to copy it to this folder, as it's the folder that dockers use)
- Then, go ahead and update your `webapp/.env` file to replace the value of `PLAYER_WALLET_PRIVATE_KEY_FILE_PATH` with the path to your keyfile (inside the `keystores` folder) and `PLAYER_WALLET_PASSWORD` wiht your password.

```sh
ICON_SERVICE_PROVIDER_URL=http://host.docker.internal:9000/api/v3
CASINO_SCORE_ADDRESS=COPY_FROM_CONTRACT_DEPLOYMENT
PLAYER_WALLET_PRIVATE_KEY_FILE_PATH=./keystores/keystore_test1.json # UPDATE THIS LINE WITH YOUR KEYSTORE FILE PATH
PLAYER_WALLET_PASSWORD=test1_Account # UPDATE THIS LINE WITH YOUR PASSWORD
BET_AMOUNT=100000000000000000000
DEBUG=True
HOST=0.0.0.0
PORT=5000
```

note: Please notice that in order to use a different wallet,

### Executing the web application

From the root folder, run the following command:

```sh
docker run --env-file=webapp/.env -p 5000:5000 $(docker build -t mlh-localhost-icon -q . -f Dockerfile.webapp)
```

Then open [http://localhost:5000/](http://localhost:5000/) to see the application.
