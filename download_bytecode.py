from web3 import Web3
import argparse


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', help='Contract address')
    parser.add_argument('--host', help='Host to connect', default='http://localhost:8545')
    parser.add_argument('-o', '--output', help='Save binary file')
    args = parser.parse_args()

    return args


def main():
    args = parseargs()    

    address = args.address
    host = args.host
    filepath = args.output

    w3 = Web3(Web3.HTTPProvider(host))

    bytecode = w3.eth.getCode(address)

    if filepath:
        wf = open(filepath, 'wb')
        wf.write(bytecode)

    print(bytecode.hex())


if __name__ == "__main__":
    main()