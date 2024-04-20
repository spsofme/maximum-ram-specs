import subprocess
from types import NoneType

def main():
	dict_output = {}
	split_output = []
	output = ""
	numbers = "0123456789"

	cmd = subprocess.Popen("wmic memphysical get MaxCapacityEx, MemoryDevices", stdout=subprocess.PIPE, shell=True)

	for i in cmd.communicate():
		if not (type(i) == NoneType or type(i) == None):
			output = str(i, "utf-8")

	output = output.strip()

	for i in output.split(" "):
		if not (i == "" or i == None):
			split_output.append(i)

	i = 0
	while i < len(split_output) / 2:
		dict_output.update({ split_output[i] : split_output[i + 2] })
		i += 1

	dict_output["MaxCapacityEx"] = "".join([(i if i in numbers else "") for i in dict_output["MaxCapacityEx"]])

	
	print(f"Maximum ram capacity: {int(dict_output['MaxCapacityEx']) / 1048576} GB")
	print(f"Avail ram slot: {dict_output['MemoryDevices']}")


	cmd = subprocess.Popen("wmic memorychip get speed", stdout=subprocess.PIPE, shell=True)
	for i in cmd.communicate():
		if not (type(i) == NoneType or type(i) == None):
			output = str(i, "utf-8")

	output = output.strip().split(" ")
	output = output[len(output) - 1].strip()
	print(f"Ram speed: {output}MHz")


if __name__ == '__main__':
	main()