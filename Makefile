test:
    # Remove all cached pyc files, they don't play nice with the containers
	find . -name "*.pyc" -delete
	# Remove test directory if exists
	rm -rf reports
	# Make a test report directory
	mkdir reports
	# Make a coverage sub-directory
	mkdir reports/coverage
    # Build the docker image
	docker build -t test-image:hw-low-level .
    # Run `tox` on the image. Automatically remove the container when it exits
	docker run -v "$(shell pwd)/reports":/reports --rm -t test-image:hw-low-level tox