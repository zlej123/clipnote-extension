#!/usr/bin/env python3
"""Generate extension icons (16/48/128) programmatically. Requires opencv+numpy."""
import os

import cv2
import numpy as np

SIZE = 512  # draw large, downscale for crisp edges
RED = (77, 72, 229)   # BGR of #e5484d
WHITE = (255, 255, 255)


def rounded_rect(img, p1, p2, radius, color):
    x1, y1 = p1
    x2, y2 = p2
    cv2.rectangle(img, (x1 + radius, y1), (x2 - radius, y2), color, -1)
    cv2.rectangle(img, (x1, y1 + radius), (x2, y2 - radius), color, -1)
    for cx, cy in ((x1 + radius, y1 + radius), (x2 - radius, y1 + radius),
                   (x1 + radius, y2 - radius), (x2 - radius, y2 - radius)):
        cv2.circle(img, (cx, cy), radius, color, -1)


bgr = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
shape_mask = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)

# red rounded-square background (mask defines alpha)
rounded_rect(shape_mask, (16, 16), (SIZE - 16, SIZE - 16), 96, WHITE)
bgr[shape_mask[:, :, 0] > 0] = RED

# white document
rounded_rect(bgr, (112, 96), (304, 416), 28, WHITE)
# red text lines on the document
for i, y in enumerate(range(150, 380, 56)):
    cv2.rectangle(bgr, (150, y), (231 if i == 3 else 267, y + 22), RED, -1)

# play triangle (video), bottom-right: red gap then white triangle
cv2.fillPoly(bgr, [np.array([[300, 250], [300, 440], [452, 345]], dtype=np.int32)], RED)
cv2.fillPoly(bgr, [np.array([[316, 278], [316, 412], [428, 345]], dtype=np.int32)], WHITE)

alpha = shape_mask[:, :, 0]
canvas = np.dstack([bgr, alpha])

os.makedirs("icons", exist_ok=True)
for size in (128, 48, 16):
    icon = cv2.resize(canvas, (size, size), interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"icons/icon{size}.png", icon)
    print(f"icons/icon{size}.png")
