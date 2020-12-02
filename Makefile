test:
	pytest --tb=short

watch-tests:
	ls day/*/*.py | entr pytest --tb=short
