from flet import *
# THIS PROJECT USE OPENCV THEN INSTALL OPENCV IN YOU PC
import cv2
import time
import os

def main(page:Page):
	page.update()

	# SHOW YOU FACE IMAGE WIDGET
	myimage = Image(
		src=False,
		width=300,
		height=300,
		fit="cover"

		)

	# REMOVE ALL IMAGE IN YOUPHOTO FOLDER 
	def removeallyouphoto():
		folder_path = "youphoto/"
		# CHECK ALL FILE IN YOUPHOTO FOLDER
		files = os.listdir(folder_path)
		for file in files:
			file_path = os.path.join(folder_path,file)
			# AND IF FOUND THEN REMOVE
			if os.path.isfile(file_path):
				os.remove(file_path)
				print(f"YOU FILE SUUCESS REMOVE {file_path}")

		page.update()



	def takemepicture(e):
		removeallyouphoto()
		cap = cv2.VideoCapture(0)
		cv2.namedWindow("Webcam",cv2.WINDOW_NORMAL)
		# AND SET YOU WINDOW HEIGHT AND WIDTH WEBCAM
		cv2.resizeWindow("Webcam",400,600)

		# AND SAVE THE FILE NAME WITH TIME NOW 
		timestamp = str(int(time.time()))
		myfileface = str("myCumFaceFile" + "_" + timestamp + '.jpg')
		try:
			while True:
				ret,frame = cap.read()
				cv2.imshow("Webcam",frame)
				myimage.src = ""
				page.update()

				# AFTER THAT WAITING YOU INPUT FROM KEYBOARD
				key = cv2.waitKey(1)

				# AND IF YOU PRESS Q FROM YOU KEYBOARD THEN
				# THE WEBCAM WINDOW CAN CLOSE 
				# AND YOU NOT CAPTURE YOU IMAGE
				if key == ord("q"):
					break
				elif key == ord("s"):
					# AND IF YOU PRESS s FROM YOU KEYBOARD
					# THE THE YOU CAPTURE WILL SAVE IN FOLDER YOUPHOTO
					cv2.imwrite(f"youphoto/{myfileface}",frame)
					# AND SHOW TEXT YOU PICTURE SUCCESS INPUT
					cv2.putText(frame,"YOU SUCESS CAPTURE GUYS !!!",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
					cv2.imshow("Webcam",frame)
					cv2.waitKey(3000)
					folder_path = "youphoto/"
					myimage.src = folder_path + myfileface
					page.update()
					break

			cap.release()
			cv2.destroyAllWindows()
			page.update()

		except Exception as e:
			print(e)
			print("YOU FAILED CHECK ERROR !!!!")




	page.add(
	Column([
	Text("Webcam Capture You FAce",
		size=30,weight="bold"
	),
	ElevatedButton("Take My Face",
		bgcolor="blue",color="white",
		on_click=takemepicture
	),
	myimage 

	])
	)

flet.app(target=main,assets_dir="youphoto")


# AND PRESS s for capture
# YOU FACEs