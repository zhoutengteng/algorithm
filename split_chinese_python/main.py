#coding=utf-8
import copy
import math
import argparse

def recursion(inputStr, begin, end, file_wordsdic, chunk, result,file_charsdic_list_key,file_charsdic_list_frequency):
    if (len(chunk) == 3 or (len(chunk) < 3 and begin >= len(inputStr))):
    	result.append(chunk)
    	return
    for j in range(begin+3, end+1, 3):
    	oneword = inputStr[begin:j]
        chunk.append(oneword)
        if ("".join(oneword) in file_charsdic_list_key or  "".join(oneword) in file_wordsdic_list):
            recursion(inputStr, j, end, file_wordsdic, copy.deepcopy(chunk) ,result,file_charsdic_list_key,file_charsdic_list_frequency)
        chunk.pop()

def maximum_matching(inputStr, file_wordsdic, file_charsdic_list_key, file_charsdic_list_frequency):
    result = []
    chunk = []
    recursion(inputStr, 0, len(inputStr), file_wordsdic, chunk, result,file_charsdic_list_key,file_charsdic_list_frequency)
    maxlength = 0
    maxResult = []
    for one in result:
    	thisLength = len("".join(one)) / 3
    	if maxlength == thisLength:
    		maxResult.append(one)
    	if maxlength < thisLength:
            maxResult = [one]
            maxlength = thisLength
    return maxlength,maxResult


def largest_average_word_length(maximum_matching_list, file_wordsdic, file_charsdic_list_key, file_charsdic_list_frequency):
    largeAverage = 0
    largeResult = []
    for one in maximum_matching_list:
        thisAverage = (len("".join(one)) + 0.0) / 3 / len(one)
        if abs(largeAverage - thisAverage) <= 0.0001:
            largeResult.append(one)
            largeAverage = thisAverage
        if largeAverage < thisAverage:
            largeResult = [one]
            largeAverage = thisAverage
    return largeAverage,largeResult

def smallest_variance_of_word_lengths(largeResult,file_wordsdic, file_charsdic_list_key, file_charsdic_list_frequency):
    smallestVariance = 100000000
    smallestVarianceResult = []
    for one in largeResult:
        thisAverage = len("".join(one)) / 3 / len(one)
        thisVarianceTotal = 0
        for one_in in one:
            thisVarianceTotal += (thisAverage -len(one_in) / 3) ** 2
        thisVariance = math.sqrt((thisVarianceTotal  + 0.0) / len(one))
        if abs(smallestVariance - thisVariance) <= 0.0001:
            smallestVarianceResult.append(one)
        if smallestVariance > thisVariance:
            smallestVarianceResult = [one]
            smallestVariance = thisVariance
    return smallestVariance,smallestVarianceResult

def largest_sum_of_degree_of_log_of_one_character_words(smallestVarianceResult, file_wordsdic,file_charsdic_list_key, file_charsdic_list_frequency):
    largeSumLog = 0.0
    largetSumOLogResult = []
    for one in smallestVarianceResult:
        thisSumLog = 0
        for one_in in one:
            if len(one_in) / 3 == 1:
                if one_in in file_charsdic_list_key:
                    frequency = file_charsdic_list_frequency[file_charsdic_list_key.index(one_in)]
                    thisSumLog += math.log(float(frequency))
                else:
                    print "error " + one_in + " is not in the dict"
        if abs(largeSumLog - thisSumLog) <= 0.0001:
            largetSumOLogResult.append(one)
        if largeSumLog < thisSumLog:
            largeSumLog = thisSumLog
            largetSumOLogResult = [one]
    return largeSumLog,largetSumOLogResult



def round(inputStr, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency):

    maxlength,maxResult = maximum_matching(inputStr, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)
    print "\Step1"
    for one in maxResult:
        print " ".join(one)
    largeAverage,largeResult = largest_average_word_length(maxResult, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)
    print "\Step2"
    for one in largeResult:
        print " ".join(one)
    smallestVariance,smallestVarianceResult = smallest_variance_of_word_lengths(largeResult, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)
    print "\Step3"
    for one in smallestVarianceResult:
        print " ".join(one)
    largeSumLog,largetSumOLogResult = largest_sum_of_degree_of_log_of_one_character_words(smallestVarianceResult, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)
    print "\Step4"
    for one in largetSumOLogResult:
        print " ".join(one)
    return len("".join(largetSumOLogResult[0][0])) / 3, "".join(largetSumOLogResult[0][0])



def load(file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency):
    file_charsdic = open('data/chars.dic', 'r')

    try:
        all_lines_in_file_charsdic = file_charsdic.readlines( )
    finally:
        file_charsdic.close( )

    for line in all_lines_in_file_charsdic:
        char, frequency = line.strip().split(' ')
        file_charsdic_list_key.append(char)
        file_charsdic_list_frequency.append(frequency)
    file_wordsdic = open('data/words.dic', 'r')

    try:
        all_lines_in_file_wordsdic = file_wordsdic.readlines( )
    finally:
        file_wordsdic.close( )

    for line in all_lines_in_file_wordsdic:
        word = line.strip()
        file_wordsdic_list.append(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Terminal Login tool')
    parser.add_argument('-w','--word',help='chinese word')
    args = parser.parse_args()

    file_wordsdic_list = []
    file_charsdic_list_key = []
    file_charsdic_list_frequency = []
    load(file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)

    if args.word is not None:
        inputStr = args.word
    else:
        inputStr="设施和服务"
        inputStr="有一个女人爱上一个比自己小的男人，\
而那个比那个女人岁数小的男人并不喜欢比自己岁数大的女人。\
女人千方百计讨好那个男人而那个男人喜欢的另外一个女人不喜欢这个男人而喜欢上一个比自己岁数的\
小的男人而被第一个女人喜欢的男人是一个事业有成的男人而那个被自己喜欢的女人而喜欢的那个比自己喜欢的女人岁数小的男人\
只不过是一个混混于是那个男人就让那个喜欢自己的女人接近想弄明白为什么女人会喜欢这样的男人希望可以挽回和自己喜欢的女人的缘分。\
正当剧情发展到连编剧都要搞不清楚的时候，突然出现一个男人要和第一个男人抢那喜欢第一个男人的女人那个男人不喜欢这个女人只喜欢那个女人但是突然发现原来自己也对自己原来不喜欢的女人有了好感，\
而那个混混男人因为和喜欢第一个男人的女人出现了一些矛盾而分手于是这个女人就很想回到原来的男人身边而突然出现的那人就在里面陶调拨关系使那个女人又和那个原来男人不喜欢而现在喜欢的女人产生了矛盾，\
可是那个混混男人要报复那个女人所以就要报复那个男人就和那个突然出现的男人一起抢那个女人于是那个女人看着三个男人不知道要挑哪个男人。\
"
    print "input=>" + inputStr

    length = len(inputStr) / 3
    thisLength = 0
    index = 1
    allresult = []
    while thisLength < length:
        print ""
        print "第" + str(index) + "趟"
        wordLength, word = round(inputStr, file_wordsdic_list, file_charsdic_list_key, file_charsdic_list_frequency)
        print "第" + str(index) + "趟 结果==>" + word
        thisLength += wordLength
        inputStr = inputStr[wordLength*3:]
        index += 1
        allresult.append(word)
    print "\n在分词之后的结果是"
    print " ".join(allresult)
