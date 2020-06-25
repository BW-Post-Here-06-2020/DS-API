from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)



def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
  "title": "Is Fusion nullified for the Extreme Z Awakening Event?",
  "post": "On JP I missed out on my chance to do SSJ3 Goku the first time so I'm doing it now. Been lucked out of rotations for most of these stages and I've noticed that for my Fusions team, LR Gogeta would NEVER fuse. I'm genuinely curious if the mechanic is nullified for the event or i'm just getting AWFUL RNG.",
  "prediction": [
    "DBZDokkanBattle",
    "Subreddit2",
    "Subreddit3",
    "Subreddit4",
    "Subreddit5",
    "Subreddit6",
    "Subreddit7",
    "Subreddit8",
    "Subreddit9",
    "Subreddit10"
  ]
}
    )
    body = response.json()
    assert response.status_code == 200
    assert body['prediction'] in [True, False]
    assert 0.50 <= body['probability'] < 1


def test_invalid_input():
    """Return 422 Validation Error when x1 is negative."""
    response = client.post(
        '/predict',
        json={
            'x1': -3.14,
            'x2': -42,
            'x3': 'banjo'
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'x1' in body['detail'][0]['loc']
