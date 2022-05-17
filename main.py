from time import sleep

import face_recognition
import picamera
import numpy as np
from PIL import Image, ImageDraw

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
youssef_image = face_recognition.load_image_file("youssef.jpeg")
youssef_face_encoding = face_recognition.face_encodings(youssef_image)[0]

dr_muhamed_image = face_recognition.load_image_file("drmuhamrd.jpg")
dr_muhamed_encoding = face_recognition.face_encodings(dr_muhamed_image)[0]


sarahmed_image = face_recognition.load_image_file("sara-ahmed.jpeg")
sarahmed_encoding = face_recognition.face_encodings(sarahmed_image)[0]

sarahmed_image1 = face_recognition.load_image_file("saraahmed1.jpeg")
sarahmed_encoding1 = face_recognition.face_encodings(sarahmed_image1)[0]

saralaa_image = face_recognition.load_image_file("sara-alaa.jpeg")
saralaa_encoding = face_recognition.face_encodings(saralaa_image)[0]

saralaa2_image = face_recognition.load_image_file("saraalaa2.jpeg")
saralaa_encoding2 = face_recognition.face_encodings(saralaa2_image)[0]

saralaa3_image = face_recognition.load_image_file("saraalaa3.jpeg")
saralaa_encoding3 = face_recognition.face_encodings(saralaa3_image)[0]

rewan_image = face_recognition.load_image_file("rewan.jpeg")
rewan_encoding = face_recognition.face_encodings(rewan_image)[0]

rewan_image1 = face_recognition.load_image_file("rewan1.jpeg")
rewan_encoding1 = face_recognition.face_encodings(rewan_image1)[0]

shady_image = face_recognition.load_image_file("shady.jpeg")
shady_encoding = face_recognition.face_encodings(shady_image)[0]

shady_image1 = face_recognition.load_image_file("shady1.jpeg")
shady_encoding1 = face_recognition.face_encodings(shady_image1)[0]

seif_image = face_recognition.load_image_file("seif.jpeg")
seif_encoding = face_recognition.face_encodings(seif_image)[0]

shreef_image = face_recognition.load_image_file("shreef.jpeg")
shreef_encoding = face_recognition.face_encodings(shreef_image)[0]


ahmedtartor_image = face_recognition.load_image_file("ahmedtartor.jpeg")
ahmedtartor_encoding = face_recognition.face_encodings(ahmedtartor_image)[0]

ahmedtarek_image = face_recognition.load_image_file("ahmedtarek.jpeg")
ahmedtarek_encoding = face_recognition.face_encodings(ahmedtarek_image)[0]

mahmoudnabawy = face_recognition.load_image_file("mahmoudnabawy.jpeg")
mahmoudnabawy_encoding = face_recognition.face_encodings(mahmoudnabawy)[0]

mohamedanter_image = face_recognition.load_image_file("mohamedanter.jpeg")
mohamedanter_encoding = face_recognition.face_encodings(mohamedanter_image)[0]

ahmedgamal_image = face_recognition.load_image_file("ahmedgamal.jpeg")
ahmedgamal_encoding = face_recognition.face_encodings(ahmedgamal_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [

    youssef_face_encoding,
    dr_muhamed_encoding,
    sarahmed_encoding,
    saralaa_encoding,
    rewan_encoding,
    shady_encoding,
    seif_encoding,
    shreef_encoding,
    ahmedtartor_encoding,
    ahmedtarek_encoding,
    mahmoudnabawy_encoding,
    mohamedanter_encoding,
    ahmedgamal_encoding,
    saralaa_encoding2,
    saralaa_encoding3,
    sarahmed_encoding1,
    rewan_encoding1,
    shady_encoding1
]
known_face_names = [

    "youssef",
    "Dr Mohamed",
    "saraahemed",
    "saraalaa",
    "rewan",
    "shady",
    "seif",
    "shreef",
    "ahmed tartour",
    "ahmed tarek",
    "mahmoud nabawy",
    "mohamed anter",
    "ahmed gamal",
    "saraalaa2",
    "saraalaa3",
    "saraahmed1",
    "rewwan1",
    "shady1"

]
# Initialize some variables
face_locations = []
face_encodings = []
pil_image = Image.fromarray(output)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)
while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    

    camera.capture(output, format="rgb")

    camera.stop_preview()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([known_face_encodings], face_encoding)
        faceDis = face_recognition.face_distance(known_face_encodings, face_encoding)
        name = "<Unknown Person>"

        
        if True in match:
            first=match.index(True)
            name=known_face_names[first]
            print(name)
            #matchindex=[i for (i,b)in emumerate(matches) if b]
            #counts={}
            #for  i in matchindex:
             #   name=known_face_names[i]
              #  counts[names]=counts.get(name,0)+1  
            #name=max(counts,key=counts.get)
           

        print("I see someone named {}!".format(name))
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
         
            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            # Draw a label with a name below the face
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

            # Remove the drawing library from memory as per the Pillow docs
        del draw
        pil_image.show()
        #for (top, right, bottom, left), name in zip(face_locations, known_face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #    top *= 4

      #      right *= 4
      #      bottom *= 4
       #     left *= 4

            # Draw a box around the face
        #    cv2.rectangle(camera, (left, top), (right, bottom), (67, 23, 255), 2)

            # Draw a label with a name below the face
         #   cv2.rectangle(camera, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
          #  font = cv2.FONT_HERSHEY_DUPLEX
           # cv2.putText(camera, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
        #cv2.imshow('Video', camera)

        # Hit 'q' on the keyboard to quit!
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #   break

# Release handle to the webcam
#video_capture.release()
#cv2.destroyAllWindows()



