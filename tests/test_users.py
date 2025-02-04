from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app)

# Mocking la base de données
@patch("app.db.session.database.execute", new_callable=AsyncMock)
@patch("app.db.session.database.fetch_one", new_callable=AsyncMock)
def test_create_user(mock_fetch_one, mock_execute):
    # Simuler une réponse de la base de données
    mock_execute.return_value = 1  # ID généré pour l'utilisateur
    mock_fetch_one.return_value = None  # Aucun utilisateur existant trouvé

    # Payload pour l'inscription
    payload = {"email": "test@example.com", "password": "securepassword"}

    # Envoyer une requête POST
    response = client.post("/api/v1/users/", json=payload)

    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == payload["email"]

@patch("app.db.session.database.fetch_one", new_callable=AsyncMock)
@patch("app.db.session.database.execute", new_callable=AsyncMock)
def test_create_user_already_exists(mock_execute, mock_fetch_one):
     # Simuler qu'un utilisateur existe déjà
    mock_fetch_one.return_value = {"id": 1, "email": "test@example.com"}

    payload = {"email": "test@example.com", "password": "securepassword"}
    response = client.post("/api/v1/users/", json=payload)

    # Vérifiez que le code HTTP est 400
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}

    #TODO add unit test for getme