import string
from collections import Counter
import json

labelDict = {}
sentences = []
wordCorpus = []
# stopWords = set(["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"])
stopWords = set(
    [
        "onto",
        "think",
        "thru",
        "that",
        "seem",
        "who's",
        "as",
        "others",
        "himself",
        "aside",
        "there",
        "their",
        "looking",
        "you're",
        "am",
        "herself",
        "i",
        "see",
        "most",
        "happens",
        "saying",
        "upon",
        "to",
        "some",
        "hi",
        "the",
        "what's",
        "it",
        "they'll",
        "very",
        "own",
        "inc",
        "kept",
        "two",
        "herein",
        "uses",
        "asking",
        "only",
        "his",
        "follows",
        "hereby",
        "it'll",
        "thereby",
        "there's",
        "goes",
        "meanwhile",
        "get",
        "will",
        "still",
        "whoever",
        "placed",
        "knows",
        "somehow",
        "que",
        "said",
        "lately",
        "hows",
        "theirs",
        "try",
        "ought",
        "them",
        "beside",
        "ie",
        "comes",
        "would",
        "behind",
        "got",
        "specified",
        "therein",
        "ex",
        "been",
        "for",
        "an",
        "yourself",
        "ever",
        "a's",
        "won't",
        "specifying",
        "themselves",
        "out",
        "wherein",
        "ltd",
        "off",
        "soon",
        "along",
        "somewhat",
        "ones",
        "secondly",
        "consider",
        "without",
        "though",
        "because",
        "via",
        "whole",
        "yet",
        "between",
        "this",
        "why's",
        "able",
        "taken",
        "it's",
        "want",
        "so",
        "we've",
        "you'd",
        "anyhow",
        "around",
        "thence",
        "whereby",
        "toward",
        "its",
        "corresponding",
        "going",
        "self",
        "here",
        "whatever",
        "at",
        "together",
        "neither",
        "hed",
        "gives",
        "know",
        "go",
        "need",
        "seeming",
        "you'll",
        "few",
        "ok",
        "through",
        "needs",
        "lest",
        "anyone",
        "wouldn't",
        "appear",
        "usually",
        "weren't",
        "considering",
        "t's",
        "we're",
        "edu",
        "maybe",
        "name",
        "twice",
        "latterly",
        "came",
        "former",
        "oh",
        "etc",
        "downwards",
        "used",
        "seeing",
        "seven",
        "also",
        "i'm",
        "what",
        "having",
        "brief",
        "has",
        "that's",
        "itself",
        "non",
        "from",
        "you've",
        "she'll",
        "my",
        "six",
        "wish",
        "let",
        "may",
        "anyways",
        "gotten",
        "he",
        "it'd",
        "then",
        "re",
        "when",
        "old",
        "went",
        "became",
        "ourselves",
        "such",
        "gets",
        "and",
        "nd",
        "else",
        "each",
        "one",
        "let's",
        "hereafter",
        "she'd",
        "therefore",
        "keeps",
        "several",
        "whence",
        "here's",
        "second",
        "they're",
        "something",
        "in",
        "once",
        "other",
        "thereafter",
        "or",
        "with",
        "above",
        "yes",
        "does",
        "regarding",
        "sensible",
        "seemed",
        "we",
        "whose",
        "keep",
        "whether",
        "three",
        "can",
        "i'll",
        "given",
        "again",
        "was",
        "nearly",
        "you",
        "followed",
        "i've",
        "often",
        "are",
        "by",
        "say",
        "whereas",
        "every",
        "getting",
        "of",
        "within",
        "whom",
        "our",
        "a",
        "indeed",
        "becoming",
        "yours",
        "value",
        "ours",
        "third",
        "sometimes",
        "when's",
        "hereupon",
        "seen",
        "yourselves",
        "next",
        "whither",
        "i'd",
        "viz",
        "up",
        "using",
        "per",
        "these",
        "done",
        "have",
        "wasn't",
        "gone",
        "use",
        "quite",
        "which",
        "do",
        "eg",
        "says",
        "wherever",
        "formerly",
        "willing",
        "him",
        "us",
        "ask",
        "th",
        "while",
        "saw",
        "thereupon",
        "thus",
        "same",
        "sub",
        "is",
        "since",
        "thats",
        "elsewhere",
        "looks",
        "took",
        "they'd",
        "someone",
        "she",
        "your",
        "nine",
        "furthermore",
        "how",
        "somewhere",
        "under",
        "if",
        "he's",
        "sometime",
        "no",
        "eight",
        "selves",
        "becomes",
        "myself",
        "truly",
        "even",
        "trying",
        "nowhere",
        "were",
        "too",
        "latter",
        "across",
        "might",
        "why",
        "come",
        "those",
        "tried",
        "among",
        "they've",
        "whenever",
        "hence",
        "take",
        "tends",
        "specify",
        "where",
        "we'll",
        "later",
        "now",
        "we'd",
        "than",
        "known",
        "various",
        "into",
        "sure",
        "away",
        "become",
        "they",
        "inward",
        "seems",
        "tell",
        "near",
        "sent",
        "she's",
        "ain't",
        "sup",
        "almost",
        "further",
        "whereafter",
        "theres",
        "could",
        "following",
        "but",
        "down",
        "okay",
        "tries",
        "anyway",
        "doing",
        "who",
        "whereupon",
        "namely",
        "all",
        "way",
        "besides",
        "over",
        "vs",
        "mean",
        "somebody",
        "wants",
        "beyond",
        "be",
        "before",
        "below",
        "amongst",
        "her",
        "where's",
        "on",
        "either",
        "un",
        "towards",
        "about",
        "hers",
        "both",
        "during",
        "me",
        "i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours",
        "ourselves",
        "you",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "her",
        "hers",
        "herself",
        "it",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "should",
        "now",
    ]
)
wordCount = {}
weightVector1 = {}
cachedVector1 = {}
weightVector2 = {}
cachedVector2 = {}
maxIter = 50
PosNegSet = []
TrueFakeSet = []
counts = []


def perceptronTrain(bias, weightVector, classifyLabel, classifySet, cachedVector):
    count = 1
    beta = 0
    for i in range(0, maxIter):
        for j in range(0, len(sentences)):
            givenSent = sentences[j]
            activation = 0

            words = givenSent.split()
            featureVector = {}
            for word in words:
                if word in wordCount:
                    if word in featureVector:
                        featureVector[word] += 1
                    else:
                        featureVector[word] = 1

            for w in featureVector:
                activation += weightVector[w] * featureVector[w]

            activation += bias
            if classifySet[j] == classifyLabel:
                y = 1
            else:
                y = -1
            if activation * y <= 0:
                for word in featureVector:
                    weightVector[word] += y * featureVector[word]
                    cachedVector[word] += y * count * featureVector[word]
                bias += y
                beta += y * count

            count += 1
    return weightVector, bias, cachedVector, beta, count


def percepLearn():
    for givenWord in wordCorpus:
        wordCount[givenWord] = 1

    # print("Wordcount", len(wordCount))
    for word in wordCount:
        weightVector1[word] = 0
        cachedVector1[word] = 0
    finalWeightLabel1, finalBiasLabel1, cached1, beta1, count1 = perceptronTrain(
        0, weightVector1, "True", TrueFakeSet, cachedVector1
    )
    # print( "final weights",finalWeightLabel1, finalBiasLabel1)

    for word in wordCount:
        weightVector2[word] = 0
        cachedVector2[word] = 0
    print(weightVector2)
    finalWeightLabel2, finalBiasLabel2, cached2, beta2, count2 = perceptronTrain(
        0, weightVector2, "Pos", PosNegSet, cachedVector2
    )

    with open("vanillamodel.txt", "w") as file:
        text = [finalWeightLabel1, finalBiasLabel1, finalWeightLabel2, finalBiasLabel2]
        # text = [finalBiasLabel1,finalBiasLabel2]
        print(finalBiasLabel1, finalBiasLabel2)
        json.dump(text, file)

    for word in finalWeightLabel1:
        finalWeightLabel1[word] -= cached1[word] / count1
    finalBiasLabel1 -= beta1 / count1
    for word in finalWeightLabel2:
        finalWeightLabel2[word] -= cached2[word] / count2
    finalBiasLabel2 -= beta2 / count2

    with open("averagedmodel.txt", "w") as file:
        text = [finalWeightLabel1, finalBiasLabel1, finalWeightLabel2, finalBiasLabel2]
        # text = [finalBiasLabel1,finalBiasLabel2]
        print(finalBiasLabel1, finalBiasLabel2)
        json.dump(text, file)


def delHighFreqWords():
    global counts
    counts = Counter(wordCorpus).most_common(20)
    for word in counts:
        wordCorpus.remove(word[0])

    for word in wordCorpus:
        if word in stopWords:
            wordCorpus.remove(word)
    # print("lentg", len(wordCorpus))


def readData():
    with open(sys.argv[1], "r") as f:
        for line in f:
            sentenceSplits = line.split(" ")
            PosNegSet.append(sentenceSplits[2])
            TrueFakeSet.append(sentenceSplits[1])
            newLine = " ".join(sentenceSplits[3:])
            # trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            trans = str.maketrans("", "", string.punctuation)
            newLine = newLine.translate(trans).lower()
            sentences.append(newLine)
            tokenList = [
                word
                for word in newLine.split()
                if ((word not in stopWords) and (word.isalnum()))
                and (len(word.strip()) != 0)
            ]
            # print("toen", tokenList)
            for word in tokenList:
                wordCorpus.append(word)
    print("length of wordCorpus", len(PosNegSet), len(TrueFakeSet), len(sentences))


if __name__ == "__main__":
    readData()
    print(sentences[0])
    delHighFreqWords()
    percepLearn()
