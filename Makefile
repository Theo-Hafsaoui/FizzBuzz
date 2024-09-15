run:
	uvicorn app.api:app
test:
	pytest
lint:
	black .
    


