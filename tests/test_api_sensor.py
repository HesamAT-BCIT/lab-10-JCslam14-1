import os
def test_sensor_data_no_api_key(client, mocker):
    mocker.patch.dict(os.environ, {"SENSOR_API_KEY": "test-sensor-key"})
    response = client.post('/api/sensor_data', json={"temp": 23}, headers={"X-API-Key": ''})
    assert response.status_code == 401

def test_sensor_data_wrong_key(client, mocker):
    mocker.patch.dict(os.environ, {"SENSOR_API_KEY": "test-sensor-key"})
    response = client.post('/api/sensor_data', json={"temp": 23}, headers={"X-API-Key": "key"})
    assert response.status_code == 401

def test_sensor_data_valid_key(client, mocker):
    mocker.patch.dict(os.environ, {"SENSOR_API_KEY": "test-sensor-key"})
    response = client.post('/api/sensor_data', json={"temp": 23}, headers={"X-API-Key":"test-sensor-key"})
    data = response.get_json()
    assert response.status_code == 201
    assert data is not None