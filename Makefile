run:
	docker run -it --entrypoint /bin/sh chrome

build:
	docker build --platform linux/amd64 -t chrome .

