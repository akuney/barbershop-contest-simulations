import numpy, operator
from collections import Counter

scores_2015 = {
"instant_classic": [91.9, 91.0, 91.7, 93.7, 94.5, 93.3],
"forefront": [91.1, 93.6, 92.9, 93.2, 92.1, 92.7],
"main_street": [90.7, 91.5, 91.3, 92.1, 95.3, 93.3],
"lemon_squeezy": [90.4, 90.8, 90.2, 91.2, 92.3, 93.1],
"throwback": [90.1, 89.2, 89.6, 90.9, 89.0, 89.5],
"a_mighty_wind": [87.8, 87.9, 89.8, 88.5, 88.3, 88.3],
"the_crush": [88.3, 88.7, 87.7, 88.0, 87.7, 87.7],
"after_hours": [86.3, 85.8, 89.3, 89.8, 88.3, 88.6],
"quorum": [85.9, 86.1, 86.7, 85.9, 87.2, 86.2],
"artistic_license": [85.87, 85.4, 86.3, 86.0, 87.2, 87.2]
}

# scores_2014 = {
# 	"musical_island_boys": []
# }



def compute_summary_data(input_data):
	summary_data = {}

	for qtet_name in input_data:
		summary_data[qtet_name] = {}
		summary_data[qtet_name]['mean'] = numpy.mean(input_data[qtet_name])
		summary_data[qtet_name]['std'] = numpy.std(input_data[qtet_name])
	return summary_data

def compute_contest_results(input_data, summary_data):
	simulated_scores = {}
	contest_results = {qtet_name: [] for qtet_name in input_data.keys()}

	for i in range(100):
		simulated_scores[i] = {}

		for qtet_name in summary_data:
			mean = summary_data[qtet_name]['mean']
			std = summary_data[qtet_name]['std']

			simulated_score = 0
			for j in range(6):
				simulated_score = simulated_score + mean + (std * numpy.random.randn())
			simulated_score = simulated_score / 6.0
			simulated_scores[i][qtet_name] = simulated_score

		sorted_result = sorted(
			simulated_scores[i].items(), key=operator.itemgetter(1), reverse=True
		)

		for qtet_result in sorted_result:
			qtet_name = qtet_result[0]
			placement = sorted_result.index(qtet_result) + 1
			contest_results[qtet_name].append(placement)

	return contest_results
input_data = scores_2015
summary_data = compute_summary_data(input_data)
contest_results = compute_contest_results(input_data, summary_data)

for qtet_name in contest_results:
	print qtet_name
	placements = Counter(contest_results[qtet_name])
	print sorted(placements.items(), key=operator.itemgetter(0))

