EDGES = [

    # ================= BODY =================
    (0, 1), (1, 2),              # Right arm
    (3, 4), (4, 5),              # Left arm
    (0, 3),                      # Shoulders
    (0, 6), (3, 7), (6, 7),      # Torso

    # Face minimal (nose to body + simple face structure)
    (8, 0), (8, 3),
    (8, 9), (9, 10), (10, 11), (11, 15),
    (8, 12), (12, 13), (13, 14), (14, 16),
    (17, 18),

    # ================= RIGHT HAND =================
    (2, 19),  # wrist connection

    # Thumb
    (19, 20), (20, 21), (21, 22), (22, 23),

    # Index
    (19, 24), (24, 25), (25, 26), (26, 27),

    # Middle
    (19, 28), (28, 29), (29, 30), (30, 31),

    # Ring
    (19, 32), (32, 33), (33, 34), (34, 35),

    # Pinky
    (19, 36), (36, 37), (37, 38), (38, 39),

    # Palm
    (24, 28), (28, 32), (32, 36),

    # ================= LEFT HAND =================
    (5, 40),  # wrist connection

    # Thumb
    (40, 41), (41, 42), (42, 43), (43, 44),

    # Index
    (40, 45), (45, 46), (46, 47), (47, 48),

    # Middle
    (40, 49), (49, 50), (50, 51), (51, 52),

    # Ring
    (40, 53), (53, 54), (54, 55), (55, 56),

    # Pinky
    (40, 57), (57, 58), (58, 59), (59, 60),

    # Palm
    (45, 49), (49, 53), (53, 57),
]


JOINTS = {

    # ===== BODY (0–18) =====
    "RShoulder": 0,
    "RElbow": 1,
    "RWrist": 2,
    "LShoulder": 3,
    "LElbow": 4,
    "LWrist": 5,
    "RHip": 6,
    "LHip": 7,
    "Nose": 8,
    "LeftEyeInner": 9,
    "LeftEye": 10,
    "LeftEyeOuter": 11,
    "RightEyeInner": 12,
    "RightEye": 13,
    "RightEyeOuter": 14,
    "LeftEar": 15,
    "RightEar": 16,
    "MouthLeft": 17,
    "MouthRight": 18,

    # ===== RIGHT HAND (19–39) =====
    "RHand_Wrist": 19,
    "RThumb1": 20, "RThumb2": 21, "RThumb3": 22, "RThumb4": 23,
    "RIndex1": 24, "RIndex2": 25, "RIndex3": 26, "RIndex4": 27,
    "RMiddle1": 28, "RMiddle2": 29, "RMiddle3": 30, "RMiddle4": 31,
    "RRing1": 32, "RRing2": 33, "RRing3": 34, "RRing4": 35,
    "RPinky1": 36, "RPinky2": 37, "RPinky3": 38, "RPinky4": 39,

    # ===== LEFT HAND (40–60) =====
    "LHand_Wrist": 40,
    "LThumb1": 41, "LThumb2": 42, "LThumb3": 43, "LThumb4": 44,
    "LIndex1": 45, "LIndex2": 46, "LIndex3": 47, "LIndex4": 48,
    "LMiddle1": 49, "LMiddle2": 50, "LMiddle3": 51, "LMiddle4": 52,
    "LRing1": 53, "LRing2": 54, "LRing3": 55, "LRing4": 56,
    "LPinky1": 57, "LPinky2": 58, "LPinky3": 59, "LPinky4": 60,
}
