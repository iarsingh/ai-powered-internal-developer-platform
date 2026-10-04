from fastapi.testclient import TestClient
from aiidp.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'ci': True, 'helm': True, 'policy': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'ci': True, 'helm': True}).json()
    assert bad["passed"] is False
    assert "policy" in bad["failed"]
