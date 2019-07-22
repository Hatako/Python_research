from statistics import mean, median,variance,stdev
import random

data = [1,2,3,4,5,6]
result = []

for i in range(100000):
    a = random.choice(data)
    result.append(a)

Extraction = 5000

mean_list = []
for i in range(100):
    meam_sample_list = random.sample(result, Extraction)
    m_sample_list = mean(meam_sample_list)
    mean_list.append(m_sample_list)


m = mean(result)
v = variance(result)
print("母平均: {}, 母分散: {}".format(m, v))
print("想定される標本分散: {}".format(v/Extraction))


v_meam_sample = variance(mean_list)
print("標本分散: {}".format(v_meam_sample))

# m = mean(data)
# median_data = median(data)
# variance_data = variance(data)
# stdev = stdev(data)
# print('平均: {0:.2f}'.format(m))
# print('中央値: {0:.2f}'.format(median))
# print('分散: {0:.2f}'.format(variance_data))
# print('標準偏差: {0:.2f}'.format(stdev))



# sample_data = random.sample(data,
# sample_variance = variance(sample_data)
# print('サンプルの分散: {0:.2f}'.format(sample_variance))
