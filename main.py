import cv2
import numpy as np
from src.pose_detector import PoseDetector
from src.utils import calculate_angle
def main():

    counter = 0
    stage = None
    cap = cv2.VideoCapture(0)
    detector = PoseDetector(detection_con=0.6, tracking_con=0.6)

    while cap.isOpened():
        succes, frame = cap.read()
        if not succes:
            break

        frame = detector.find_pose(frame)
        lm_list = detector.find_position(frame)

        if len(lm_list) > 15:
            shoulder = (lm_list[11][1], lm_list[11][2])
            elbow = (lm_list[13][1], lm_list[13][2])
            wrist = (lm_list[15][1], lm_list[15][2])

            angle = calculate_angle(shoulder, elbow, wrist)

            if angle > 160:
                stage = "down"

            if angle < 55 and stage == "down":
                stage = "up"
                counter += 1
                print(f"push-up #{counter} is counted")

            per = np.interp(angle, (30, 160), (100, 0))
            bar = np.interp(angle, (30, 160), (100, 400))


            cv2.putText(
                frame,
                f"{int(angle)} deg",
                (elbow[0] - 40, elbow[1] - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )
            cv2.circle(frame, elbow, 8, (0, 0, 255), cv2.FILLED)
            cv2.rectangle(frame, (50, 100), (85, 400), (0, 255, 0), 2)
            cv2.rectangle(frame, (50, int(bar)), (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f"{int(per)}%", (45, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.rectangle(frame, (0, 0), (280, 75), (245, 117, 16), -1)
            cv2.putText(frame, 'REPS', (15, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(frame, str(counter), (10, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(frame, 'STAGE', (120, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(frame, str(stage).upper() if stage else "-", (120, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow("AI Fitness Tracker - Pose Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()