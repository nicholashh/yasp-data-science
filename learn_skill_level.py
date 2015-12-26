
from codecs import open as codecs_open
from flatten_match import flatten_match
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf

# TODO
# class match_iterator_from_matches_dump

class match_iterator_from_data_file:

    def __init__(self, path_to_data_file):
        self._file = codecs_open(path_to_data_file, "r", "utf-8-sig")

    def __iter__(self): return self

    # def __next__(self):
    #     line = self._file.readline()
    #     if line == "": raise StopIteration
    #     else: return eval(line)

    def next(self):
        line = self._file.readline()
        if line == "": raise StopIteration
        else: return eval(line)

def learn_skill_level (match_iterator, path_to_skill_file):

    # process skill levels file
    match_id_to_skill = {}
    n = 0
    for match in open(path_to_skill_file):
        (match_id, skill) = match.split(",")
        match_id_to_skill[int(match_id)] = int(skill.strip())
        n += 1
        if n % 100000 == 0:
            print(1.0 * n / 30160551)
        
    # start up spark
    A6conf = ( SparkConf()
        .setMaster("local")
        .setAppName("A6")
        .set("spark.driver.memory", "6g")
        .set("spark.executor.memory", "6g") )
    sc = SparkContext(conf = A6conf)

    first = True
    data = sc.parallelize(["no data yet"])
    for match in match_iterator:

        match_id = match["match_id"]
        if match_id in match_id_to_skill:
            skill = match_id_to_skill[int(match_id)]
            match_data = flatten_match(match)
            data_point = sc.parallelize([LabeledPoint(skill, match_data)])
            if first: data = data_point; first = False
            else: data += data_point
        else: print("match_id %s not in match_id_to_skill" % match_id)

    # actually do the ML

    print(data.collect())

match_iterator = match_iterator_from_data_file("./data_5/learning")
learn_skill_level(match_iterator, "./match_skill.csv")
