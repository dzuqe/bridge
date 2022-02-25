all: build

build:
	@echo build

polygon:
	@~/.solc-select/usr/bin/solc-v0.8.0 contracts/polygon/Reserve.sol

deploy:
	@echo $1
