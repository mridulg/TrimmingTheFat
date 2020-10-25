import constants
import json
from save_frames import saveFrames
to_analyze_file = constants.DATABASE_PATH + "to_analyze.json"
analyzed_file = constants.DATABASE_PATH + "analyzed.json"


def get_results(path):
	img_dir = 'frames'

	return path
	pass


def queue_analyze_video(path, name):
	f = open(to_analyze_file).read()
	d = {"path": path, "name": name}
	l = list(json.loads(f))
	l.append(d)
	j = json.dumps(l)
	f = open(to_analyze_file, "w")
	f.write(j)
	f.close()

def analyze_video(vobj): #with name and path
	# results = json.loads(open("/mnt/c/Users/Palash/Downloads/out.json").read())

	results = get_results(vobj['path'])
	print results
	# TODO: Get results

	f = open(vobj['path'] + '.json', 'w')
	f.write(results)
	f.close()

	#TODO: write to analyzed
	# f = open(to_analyze_file).read()

if __name__ == "__main__":
	f = open(to_analyze_file).read()
	l = list(json.loads(f))
	if len(l)>0: 
		analyze_video(l[0])
	# analyze_video()