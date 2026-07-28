import numpy as np

def calculate_angle(a: tuple, b: tuple, c:tuple):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360.0 - angle

    return float(angle)

if __name__ == "__main__":
    hip = (0, 10)
    knee = (0, 0)
    ankle = (10, 0)

    test_angle = calculate_angle(hip, knee, ankle)
    print(f"test angle: {test_angle}")