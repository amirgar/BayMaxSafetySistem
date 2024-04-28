import os
import time
import numpy as np
import copy
import mtcnn
from mtcnn import MTCNN
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
import cv2


class MTCNN_Detector:
    def __init__(self, min_size, min_confidence):
        self.min_size = min_size
        self.f_detector = MTCNN(min_face_size=min_size)
        self.min_confidence = min_confidence

    def detect(self, frame):
        faces = self.f_detector.detect_faces(frame)

        detected = []
        for (i, face) in enumerate(faces):
            f_conf = face['confidence']
            if f_conf >= self.min_confidence:
                detected.append(face)

        return detected

    def extract(self, frame, face):
        (x1, y1, w, h) = face['box']
        (l_eye, r_eye, nose, mouth_l, mouth_r) = Utils.get_keypoints(face)

        f_cropped = copy.deepcopy(face)
        move = (-x1, -y1)
        l_eye = Utils.move_point(l_eye, move)
        r_eye = Utils.move_point(r_eye, move)
        nose = Utils.move_point(nose, move)
        mouth_l = Utils.move_point(mouth_l, move)
        mouth_r = Utils.move_point(mouth_r, move)

        f_cropped['box'] = (0, 0, w, h)
        f_img = frame[y1:y1 + h, x1:x1 + w].copy()

        f_cropped = Utils.set_keypoints(f_cropped, (l_eye, r_eye, nose, mouth_l, mouth_r))

        return (f_cropped, f_img)


class Utils:
    @staticmethod
    def draw_face(face, color, frame, draw_points=True, draw_rect=True, n_data=None):
        (x1, y1, w, h) = face['box']
        confidence = face['confidence']
        x2 = x1 + w
        y2 = y1 + h
        if draw_rect:
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)
        y3 = y1 - 12
        if not (n_data is None):
            (name, conf) = n_data
            text = name + (" %.3f" % conf)
        else:
            text = "%.3f" % confidence

        cv2.putText(frame, text, (x1, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1, cv2.LINE_AA)
        if draw_points:
            (l_eye, r_eye, nose, mouth_l, mouth_r) = Utils.get_keypoints(face)
            Utils.draw_point(l_eye, color, frame)
            Utils.draw_point(r_eye, color, frame)
            Utils.draw_point(nose, color, frame)
            Utils.draw_point(mouth_l, color, frame)
            Utils.draw_point(mouth_r, color, frame)

    @staticmethod
    def get_keypoints(face):
        keypoints = face['keypoints']
        l_eye = keypoints['left_eye']
        r_eye = keypoints['right_eye']
        nose = keypoints['nose']
        mouth_l = keypoints['mouth_left']
        mouth_r = keypoints['mouth_right']
        return (l_eye, r_eye, nose, mouth_l, mouth_r)

    def set_keypoints(face, points):
        (l_eye, r_eye, nose, mouth_l, mouth_r) = points
        keypoints = face['keypoints']
        keypoints['left_eye'] = l_eye
        keypoints['right_eye'] = r_eye
        keypoints['nose'] = nose
        keypoints['mouth_left'] = mouth_l
        keypoints['mouth_right'] = mouth_r

        return face

    @staticmethod
    def move_point(point, move):
        (x, y) = point
        (dx, dy) = move
        res = (x + dx, y + dy)
        return res

    @staticmethod
    def draw_point(point, color, frame):
        (x, y) = point
        x1 = x - 1
        y1 = y - 1
        x2 = x + 1
        y2 = y + 1
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)

    @staticmethod
    def draw_faces(faces, color, frame, draw_points=True, draw_rect=True, names=None):
        for (i, face) in enumerate(faces):
            n_data = None
            if not (names is None):
                n_data = names[i]
            Utils.draw_face(face, color, frame, draw_points, draw_rect, n_data)



class Face_Align:
    def __init__(self, size):
        self.size = size

    def align_point(self, point, M):
        (x, y) = point
        p = np.float32([[[x, y]]])
        p = cv2.perspectiveTransform(p, M)

        return (int(p[0][0][0]), int(p[0][0][1]))

    def align(self, frame, face):
        (x1, y1, w, h) = face['box']
        (l_eye, r_eye, nose, mouth_l, mouth_r) = Utils.get_keypoints(face)

        (pts1, pts2) = self.get_perspective_points(l_eye, r_eye, nose, mouth_l, mouth_r)

        s = self.size
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(frame, M, (s, s))

        f_aligned = copy.deepcopy(face)
        f_aligned['box'] = (0, 0, s, s)
        f_img = dst

        l_eye = self.align_point(l_eye, M)
        r_eye = self.align_point(r_eye, M)
        nose = self.align_point(nose, M)
        mouth_l = self.align_point(mouth_l, M)
        mouth_r = self.align_point(mouth_r, M)

        f_aligned = Utils.set_keypoints(f_aligned, (l_eye, r_eye, nose, mouth_l, mouth_r))

        return (f_aligned, f_img)


class Face_Align_Nose(Face_Align):
    def get_perspective_points(self, l_eye, r_eye, nose, mouth_l, mouth_r):
        (xl, yl) = l_eye
        (xr, yr) = r_eye
        (xn, yn) = nose
        (xm, ym) = (0.5 * (xl + xr), 0.5 * (yl + yr))
        (dx, dy) = (xn - xm, yn - ym)
        (xl2, yl2) = (xl + 2.0 * dx, yl + 2.0 * dy)
        (xr2, yr2) = (xr + 2.0 * dx, yr + 2.0 * dy)

        s = self.size
        pts1 = np.float32([[xl, yl], [xr, yr], [xr2, yr2], [xl2, yl2]])
        pts2 = np.float32([[s * 0.25, s * 0.25], [s * 0.75, s * 0.25], [s * 0.75, s * 0.75], [s * 0.25, s * 0.75]])

        return (pts1, pts2)


class Face_Align_Mouth(Face_Align):
    def get_perspective_points(self, l_eye, r_eye, nose, mouth_l, mouth_r):
        (xl, yl) = l_eye
        (xr, yr) = r_eye
        (xml, yml) = mouth_l
        (xmr, ymr) = mouth_r

        (xn, yn) = (0.5 * (xl + xr), 0.5 * (yl + yr))
        (xm, ym) = (0.5 * (xml + xmr), 0.5 * (yml + ymr))
        (dx, dy) = (xm - xn, ym - yn)
        (xl2, yl2) = (xl + 1.1 * dx, yl + 1.1 * dy)
        (xr2, yr2) = (xr + 1.1 * dx, yr + 1.1 * dy)

        s = self.size
        pts1 = np.float32([[xl, yl], [xr, yr], [xr2, yr2], [xl2, yl2]])
        pts2 = np.float32([[s * 0.3, s * 0.3], [s * 0.7, s * 0.3], [s * 0.7, s * 0.75], [s * 0.3, s * 0.75]])

        return (pts1, pts2)


class VideoFD:
    def __init__(self, detector):
        self.detector = detector

    def detect(self, video, save_path=None, align=False, draw_points=False):
        detection_num = 0;
        capture = cv2.VideoCapture(video)
        img = None

        dname = 'AI face detection'
        cv2.namedWindow(dname, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(dname, 960, 720)

        frame_count = 0
        dt = 0
        face_num = 0

        if align:
            fa = Face_Align_Nose(160)

        # Capture all frames
        while (True):
            (ret, frame) = capture.read()
            if frame is None:
                break
            frame_count = frame_count + 1

            t1 = time.time()
            faces = self.detector.detect(frame)
            t2 = time.time()
            p_count = len(faces)
            detection_num += p_count
            dt = dt + (t2 - t1)

            if (not (save_path is None)) and (len(faces) > 0):
                f_base = os.path.basename(video)
                for (i, face) in enumerate(faces):
                    if align:
                        (f_cropped, f_img) = fa.align(frame, face)
                    else:
                        (f_cropped, f_img) = self.detector.extract(frame, face)
                    if (not (f_img is None)) and (not f_img.size == 0):
                        if draw_points:
                            Utils.draw_faces([f_cropped], (255, 0, 0), f_img, draw_points, False)
                        face_num = face_num + 1
                        dfname = os.path.join(save_path, f_base + ("_%06d" % face_num) + ".png")
                        cv2.imwrite(dfname, f_img)

            if len(faces) > 0:
                Utils.draw_faces(faces, (0, 0, 255), frame)
                if not (save_path is None):
                    dfname = os.path.join(save_path, f_base + ("_%06d" % face_num) + "_frame.png")
                    cv2.imwrite(dfname, frame)

            # Display the resulting frame
            cv2.imshow(dname, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()
        fps = frame_count / dt
        return (detection_num, fps)


class FaceNetRec:
    def __init__(self, model, min_distance):
        self.model = load_model(model)
        self.min_distance = min_distance

    def get_model(self):
        return self.model

    def embeddings(self, f_img):
        r_img = cv2.resize(f_img, (160, 160), cv2.INTER_AREA)
        arr = r_img.astype('float32')
        arr = (arr - 127.5) / 127.5
        samples = np.expand_dims(arr, axis=0)
        embds = self.model.predict(samples)
        return embds[0]

    def eval_distance(self, embds1, embds2):
        dist = distance.cosine(embds1, embds2)
        return dist

    def img_distance(self, f_img1, f_img2):
        embds1 = self.embeddings(f_img1)
        embds2 = self.embeddings(f_img2)
        dist = self.eval_distance(embds1, embds2)
        return dist

    def match(self, embds1, embds2):
        dist = self.eval_distance(embds1, embds2)
        return dist <= self.min_distance

    def img_match(self, f_img1, f_img2):
        embds1 = self.embeddings(f_img1)
        embds2 = self.embeddings(f_img2)
        return self.match(embds1, embds2)

    def recognize(self, embds, f_db):
        minfd = 2.0
        indx = -1
        f_data = f_db.get_data();
        for (i, data) in enumerate(f_data):
            (name, embds_i, p_img) = data
            dist = self.eval_distance(embds, embds_i)
            if (dist < minfd) and (dist < self.min_distance):
                indx = i
                minfd = dist
        if indx >= 0:
            (name, embds_i, p_img) = f_data[indx]
            return (name, minfd, p_img)

        return None

    def img_recognize(self, f_img, f_db):
        embds = self.embeddings(f_img)

        return self.recognize(embds, f_db)


class FaceNetRec:
    def __init__(self, model, min_distance):
        self.model = load_model(model)
        self.min_distance = min_distance

    def get_model(self):
        return self.model

    def embeddings(self, f_img):
        r_img = cv2.resize(f_img, (160, 160), cv2.INTER_AREA)
        arr = r_img.astype('float32')
        arr = (arr - 127.5) / 127.5
        samples = np.expand_dims(arr, axis=0)
        embds = self.model.predict(samples)
        return embds[0]

    def eval_distance(self, embds1, embds2):
        dist = distance.cosine(embds1, embds2)
        return dist

    def img_distance(self, f_img1, f_img2):
        embds1 = self.embeddings(f_img1)
        embds2 = self.embeddings(f_img2)
        dist = self.eval_distance(embds1, embds2)
        return dist

    def match(self, embds1, embds2):
        dist = self.eval_distance(embds1, embds2)
        return dist <= self.min_distance

    def img_match(self, f_img1, f_img2):
        embds1 = self.embeddings(f_img1)
        embds2 = self.embeddings(f_img2)
        return self.match(embds1, embds2)

    def recognize(self, embds, f_db):
        minfd = 2.0
        indx = -1
        f_data = f_db.get_data();
        for (i, data) in enumerate(f_data):
            (name, embds_i, p_img) = data
            dist = self.eval_distance(embds, embds_i)
            if (dist < minfd) and (dist < self.min_distance):
                indx = i
                minfd = dist
        if indx >= 0:
            (name, embds_i, p_img) = f_data[indx]
            return (name, minfd, p_img)

        return None

    def img_recognize(self, f_img, f_db):
        embds = self.embeddings(f_img)

        return self.recognize(embds, f_db)


class VideoFR:
    def __init__(self, detector, rec, f_db):
        self.detector = detector
        self.rec = rec
        self.f_db = f_db

    def process(self, video, align=False):
        detection_num = 0;
        rec_num = 0
        capture = cv2.VideoCapture(video)
        img = None

        dname = 'AI face recognition'
        cv2.namedWindow(dname, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(dname, 960, 720)

        frame_count = 0
        dt = 0
        if align:
            fa = Face_Align_Mouth(160)

        # Capture all frames
        while (True):
            (ret, frame) = capture.read()
            if frame is None:
                break
            frame_count = frame_count + 1

            faces = self.detector.detect(frame)
            f_count = len(faces)
            detection_num += f_count

            names = None
            if (f_count > 0) and (not (self.f_db is None)):
                t1 = time.time()
                names = [None] * f_count
                for (i, face) in enumerate(faces):
                    if align:
                        (f_cropped, f_img) = fa.align(frame, face)
                    else:
                        (f_cropped, f_img) = self.detector.extract(frame, face)
                    if (not (f_img is None)) and (not f_img.size == 0):
                        embds = self.rec.embeddings(f_img)
                        data = self.rec.recognize(embds, self.f_db)
                        if not (data is None):
                            rec_num += 1
                            (name, dist, p_photo) = data
                            conf = 1.0 - dist
                            names[i] = (name, conf)

                t2 = time.time()
                dt = dt + (t2 - t1)

            if len(faces) > 0:
                Utils.draw_faces(faces, (0, 0, 255), frame, True, True, names)

            # Display the resulting frame
            cv2.imshow(dname, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()

        if dt > 0:
            fps = detection_num / dt
        else:
            fps = 0

        return (detection_num, rec_num, fps)


if __name__ == "__main__":
    fa = Face_Align_Mouth(160)
    db_path = r"C:\Users\Airat\PycharmProjects\BayMax_Bank\db"
    align = True
    p_name = "amir"
    f_file = r"C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photo\photo.png"
    d = MTCNN_Detector(min_size=50, min_confidence=0.95)
    fimg = cv2.imread(f_file, cv2.IMREAD_UNCHANGED)
    faces = d.detect(fimg)
    r_file = os.path.join(db_path, p_name + ".png")
    face = faces[0]
    if align:
        (f_cropped, f_img) = fa.align(fimg, face)
    else:
        (f_cropped, f_img) = d.extract(fimg, face)
    if (not (f_img is None)) and (not f_img.size == 0):
        cv2.imwrite(r_file, f_img)
        plt.imshow(f_img)
        print(p_name + " appended to Face DB.")
    else:
        print("Wrong image.")
