.PHONY: clean data

data:
	python src/data/get_data.py --dataset=all

clean:
	cd src && make clean
	cd reports && make clean
