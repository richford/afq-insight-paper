.PHONY: clean data

data:
	python src/data/get_data.py --dataset=all

docker-build:
	docker build -t afq-insight-paper .

docker-lab:
	docker run -it -p 8899:8899 insight-paper

clean:
	cd src && make clean
	cd reports && make clean
