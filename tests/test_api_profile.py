def test_get_profile_no_auth(client):
    response = client.get("/api/profile")
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data
#GET without Authorization header returns 401

def test_get_profile_bad_token_format(client):
    response = client.get("/api/profile", headers = {"Authorization": "NotBearer 12345678"})
    assert response.status_code == 401

#Authorization header without Bearer prefix returns 401

def test_get_profile_invalid_token(client, mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", side_effect=Exception("invalid token"))
    response = client.get("/api/profile", headers = {"Authorization": "Bearer asdjdfl"})
    assert response.status_code == 401
#Mock verify_id_token to raise Exception, expect 401

def test_get_profile_success(client, mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", return_value={"uid":"12345678"})
    response = client.get("/api/profile", headers={"Authorization": "Bearer 12345678"})
    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
#Valid mocked token + mocked Firestore, expect 200 with profile payload

def test_create_profile_missing_fields(client, mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", return_value={"uid": "12345678"})
    response = client.post("/api/profile", json={
        "first_name": "Test",
        "last_name": "User",
    }, headers={"Authorization": "Bearer 12345678"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
#POST incomplete JSON body, expect 400

def test_create_profile_success (client, mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", return_value={"uid": "12345678"})
    response = client.post("/api/profile", json={
        "first_name": "Test",
        "last_name": "User",
        "student_id": "12345678",
    }, headers = {"Authorization": "Bearer 12345678"})
    assert response.status_code == 200
    data = response.get_json()
    #print(data)
    assert data["profile"]["first_name"] == "Test"
#POST valid data with mocked auth and Firestore, expect 200

def test_update_profile_invalid_field (client, mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", return_value={"uid": "12345678"})
    response = client.put("/api/profile", json={"age": 25}, headers = {"Authorization": "Bearer 12345678"})
    assert response.status_code == 400
    data = response.get_json()
    assert 'Invalid field(s): age. Only first_name, last_name, and student_id are allowed.' in data["errors"]
# PUT {"age": 25}, expect 400 and whitelist error message