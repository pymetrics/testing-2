.PHONY: build
serve:
	docker-compose up

image:
	docker-compose build

static:
	docker-compose run hovercraft hovercraft /usr/src/app/presentation/slides.rst /usr/src/app/presentation/_build

clean:
	rm -rf presentation/_build

test:
	docker-compose run hovercraft bash -c "cd presentation/src/coinbot && python manage.py test"

dist:  static
	mkdir dist
	tar -zcvf dist/testing-2.tar.gz presentation/_build
