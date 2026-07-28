import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, mode=False, complexity=1, smooth_landmarks=True, 
                 detection_con=0.5, tracking_con=0.5):
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=mode,
            model_complexity=complexity,
            smooth_landmarks=smooth_landmarks,
            min_detection_confidence=detection_con,
            min_tracking_confidence=tracking_con
        )
        self.results = None

    def find_pose(self, img, draw=True):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)

        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(
                img,
                self.results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
        return img

    def find_position(self, img):

        lm_list = []
        if self.results and self.results.pose_landmarks:
            h, w, c= img.shape
            for id, lm in enumerate(self.results.pose_landmarks.landmark):

                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

        return lm_list