import numpy, operator
from collections import Counter

actual_scores = {
"instant_classic": [91.9, 91.0, 91.7, 93.7, 94.5, 93.3],
"forefront": [91.1, 93.6, 92.9, 93.2, 92.1, 92.7],
"main_street": [90.7, 91.5, 91.3, 92.1, 95.3, 93.3],
"lemon_squeezy": [90.4, 90.8, 90.2, 91.2, 92.3, 93.1],
"throwback": [90.1, 89.2, 89.6, 90.9, 89.0, 89.5]
}

summary_data = {}

simulated_scores = {}

contest_results = {qtet_name: [] for qtet_name in actual_scores.keys()}

for qtet_name in actual_scores:
	summary_data[qtet_name] = {}
	summary_data[qtet_name]['mean'] = numpy.mean(actual_scores[qtet_name])
	summary_data[qtet_name]['std'] = numpy.std(actual_scores[qtet_name])

for i in range(1, 100):
	simulated_scores[i] = {}

	for qtet_name in summary_data:
		mean = summary_data[qtet_name]['mean']
		std = summary_data[qtet_name]['std']

		simulated_score = mean + (std * numpy.random.randn())
		simulated_scores[i][qtet_name] = simulated_score

	sorted_result = sorted(
		simulated_scores[i].items(), key=operator.itemgetter(1), reverse=True
	)

	for qtet_result in sorted_result:
		qtet_name = qtet_result[0]
		placement = sorted_result.index(qtet_result) + 1
		contest_results[qtet_name].append(placement)

for qtet_name in contest_results:
	print qtet_name
	placements = Counter(contest_results[qtet_name])
	print sorted(placements.items(), key=operator.itemgetter(0))

