import os
from deepface import DeepFace


def verify_face(captured_image):

    best_match = None
    best_distance = 999

    for file in os.listdir("known_faces"):

        if not file.endswith(
            (".jpg", ".jpeg", ".png")
        ):
            continue

        known_image = os.path.join(
            "known_faces",
            file
        )

        try:

            result = DeepFace.verify(
                img1_path=captured_image,
                img2_path=known_image,
                model_name="Facenet512",
                detector_backend="opencv",
                enforce_detection=False
            )

            distance = result["distance"]

            print(
                f"{file} -> {distance}"
            )

            if distance < best_distance:
                best_distance = distance
                best_match = file

        except Exception as e:
            print(e)

    if best_match and best_distance < 0.65:

        username = os.path.splitext(
            best_match
        )[0]

        return True, username

    return False, None