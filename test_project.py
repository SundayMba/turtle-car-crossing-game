from project import detect_car_crossing, detectCarCollision, create_and_move_car


def test_detect_car_crossing():
    assert detect_car_crossing() == None

def test_detectCarCollision():
    assert detectCarCollision() == False

def test_create_and_move_car():
    assert create_and_move_car() == None