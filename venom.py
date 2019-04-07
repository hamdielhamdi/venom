import signal
import sys
import speech_recognition as sr
import time
import os

# used to interept process with keyboard
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)


# print(sr.__version__)

class Venom:
	def __init__(self):
		pass

	""" main class : venom is a series of class and method that 
	help you to  """

	#  intinialize class recognizer and activate mic
	def initializer():

		# Recognize audio 
		r = sr.Recognizer()
				#  activate mic, set to the second mic
		mic = sr.Microphone(device_index=1)

		return r,mic

	#  TODO : to be integrated in comm method as var
	def recognizer_method(index = None):
		if index == 'off_line':
			return r.recognize_sphinx(audio , show_all=True)
		return r.recognize_google(audio , show_all=True)

	# where the job is done
	def communicate(r, mic):

		with mic as source:
			print('make a request')
			r.adjust_for_ambient_noise(source, duration = 0.01)
			audio = r.listen(source)
			try: 
				response = r.recognize_google(audio , show_all=True)
				if len(response) == 0:
					pass
				else: 
					response = response['alternative'][0]['transcript']
					return response

			except Exception as e:
				print('I have no idea what you mean, pleaze try again !!! ')
				time.sleep(0.1)
				return False



if __name__ == '__main__':
	print('****** Venom is up and running ******') 
	init = Venom.initializer()
	what_is_said = []
	while True:
		comm = Venom.communicate(init[0],init[1])
		if comm :
			what_is_said.append(comm)

		print(what_is_said)










