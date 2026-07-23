.PHONY: help setup validate doe tree

help:
	@echo "make setup     - Python 가상환경 생성"
	@echo "make validate  - 프로젝트 구성 검사"
	@echo "make doe       - 초기 LHS DOE 24점 생성"
	@echo "make tree      - 현재 파일 트리 출력"

setup:
	bash 01_environment/setup_python.sh

validate:
	python scripts/validate_project.py

doe:
	python 08_doe_optimization/generate_doe.py \
		--config 08_doe_optimization/config/design_space.yaml \
		--output 08_doe_optimization/data/doe/initial_doe.csv \
		--samples 24 --method lhs --seed 20260723

tree:
	find . -maxdepth 3 -not -path "./.git/*" | sort
