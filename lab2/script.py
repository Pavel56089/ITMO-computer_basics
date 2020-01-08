import keyboard
import time

NUMBERS = {
	'091': 'E094',
	'092': '0200',
	'093': '0200',
	'094': '0200',
	'095': 'A09D',
	'096': '2092',
	'097': 'E094',
	'098': '0200',
	'099': '6093',
	'09A': '6094',
	'09B': 'E091',
	'09C': '0100',
	'09D': 'E091'
}

start_addr = '091'

run_key = 'space'
continue_key = run_key
pause_time = 0 # Pause in miliseconds

def press(k):
	time.sleep(pause_time * 0.001)
	keyboard.press_and_release(k)

def press_insert_address():
	print('Inserting address from IR to IP')
	press('F4')

def press_write():
	print('Writing data from IR to RAM')
	press('F5')

def press_read():
	print('Getting data from RAM to DR')
	press('F6')

def press_start():
	press('F7')

def tobin16(num):
	num = bin(int(num, 16))
	num = num[2::]
	num = (16 - len(num)) * '0' + str(num)
	return num

def write_IR(num):
	bin16 = tobin16(num)

	print('Write to IR number:', bin16, '. Equals', num, 'in hex')

	for x in bin16:
		press(x)

def save_val(addr, num):
	print('Saving value. addr:', addr, 'num:', num)

	write_IR(addr)

	press_insert_address()

	write_IR(num)

	press_write()


def start():
	write_IR(start_addr)
	press_insert_address()
	press_start()

def run():

	nums = {}
	for i in NUMBERS:
		nums['0x' + i] = '0x' + NUMBERS[i]

	for i in nums:
		save_val(i, nums[i])

if __name__ == '__main__':
	print('Press', run_key, 'to run')
	keyboard.add_hotkey(run_key, lambda: run())
	keyboard.wait(run_key)