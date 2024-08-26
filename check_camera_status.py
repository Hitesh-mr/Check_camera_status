import cv2

# Open the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame reading is successful
    if ret:
        # Display the frame in a window
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop and close the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Couldn't retrieve frame.")
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
