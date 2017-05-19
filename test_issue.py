import pytest


@pytest.fixture(autouse=True)
def try_backports_import_nowrite(monkeypatch):
	"""
	Simulate what happens in a setuptools sandbox when
	it attempts to prevent writing outside of the sandbox.
	"""
	def dont_mkdir(*args, **kwargs):
		raise RuntimeError("Don't make dirs")

	monkeypatch.setattr('os.mkdir', dont_mkdir)

	try:
		__import__('backports.does_not_exist')
	except ImportError:
		pass

def test_sunshine_and_roses():
	pass
