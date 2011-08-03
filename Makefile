test:
	@env PYTHONPATH=. pyvows --cover --cover_package=lie_to_me --cover_threshold=80.0 vows/
