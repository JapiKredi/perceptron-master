import json, string

weightVector1 ={}
weightVector2 = {}
bias1 = 0
bias2= 0
sentences = []
lineID = []
#stopWords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
stopWords = set(["onto","think","thru","that","seem","who's","as","others","himself","aside","there","their","looking","you're","am","herself","i","see","most","happens","saying","upon","to","some","hi","the","what's","it","they'll","very","own","inc","kept","two","herein","uses","asking","only","his","follows","hereby","it'll","thereby","there's","goes","meanwhile","get","will","still","whoever","placed","knows","somehow","que","said","lately","hows","theirs","try","ought","them","beside","ie","comes","would","behind","got","specified","therein","ex","been","for","an","yourself","ever","a's","won't","specifying","themselves","out","wherein","ltd","off","soon","along","somewhat","ones","secondly","consider","without","though","because","via","whole","yet","between","this","why's","able","taken","it's","want","so","we've","you'd","anyhow","around","thence","whereby","toward","its","corresponding","going","self","here","whatever","at","together","neither","hed","gives","know","go","need","seeming","you'll","few","ok","through","needs","lest","anyone","wouldn't","appear","usually","weren't","considering","t's","we're","edu","maybe","name","twice","latterly","came","former","oh","etc","downwards","used","seeing","seven","also","i'm","what","having","brief","has","that's","itself","non","from","you've","she'll","my","six","wish","let","may","anyways","gotten","he","it'd","then","re","when","old","went","became","ourselves","such","gets","and","nd","else","each","one","let's","hereafter","she'd","therefore","keeps","several","whence","here's","second","they're","something","in","once","other","thereafter","or","with","above","yes","does","regarding","sensible","seemed","we","whose","keep","whether","three","can","i'll","given","again","was","nearly","you","followed","i've","often","are","by","say","whereas","every","getting","of","within","whom","our","a","indeed","becoming","yours","value","ours","third","sometimes","when's","hereupon","seen","yourselves","next","whither","i'd","viz","up","using","per","these","done","have","wasn't","gone","use","quite","which","do","eg","says","wherever","formerly","willing","him","us","ask","th","while","saw","thereupon","thus","same","sub","is","since","thats","elsewhere","looks","took","they'd","someone","she","your","nine","furthermore","how","somewhere","under","if","he's","sometime","no","eight","selves","becomes","myself","truly","even","trying","nowhere","were","too","latter","across","might","why","come","those","tried","among","they've","whenever","hence","take","tends","specify","where","we'll","later","now","we'd","than","known","various","into","sure","away","become","they","inward","seems","tell","near","sent","she's","ain't","sup","almost","further","whereafter","theres","could","following","but","down","okay","tries","anyway","doing","who","whereupon","namely","all","way","besides","over","vs","mean","somebody","wants","beyond","be","before","below","amongst","her","where's","on","either","un","towards","about","hers","both","during","me","i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
def percepTest(weightVector,bias, sentence):
    words = sentence.split()
    featureVector = {}
    for word in words:
        if word not in stopWords:
            if word in featureVector:
                featureVector[word]+=1
            else:
                featureVector[word] =1
    activation = 0
    for w in featureVector:
        if w in weightVector:
            activation += weightVector[w] * featureVector[w]
    activation += bias
    return activation


def percepClassify():
    outputFile = open("percepoutput.txt", 'w')
    for i in range(0, len(sentences)):
        activaiton1 = percepTest(weightVector1, bias1, sentences[i])
        label1 = "True" if activaiton1>0 else "Fake"
        activaiton2 = percepTest(weightVector2, bias2, sentences[i])
        label2 = "Pos" if activaiton2>0 else "Neg"
        outputFile.write((lineID[i].strip()) + " " + label1.strip() + " " + label2.strip() + "\n")

def readData():
    global weightVector1,weightVector2,bias1, bias2
    with open(sys.argv[1],"r") as json_data:
        data = json.load(json_data)
    weightVector1 = data[0]
    weightVector2 = data[2]
    bias1 = data[1]
    bias2 = data[3]
    print(bias2)
    with open(sys.argv[2],"r") as f:
        for line in f:
            lineID.append(line[:line.find(" ")])
            newLine = " ".join(line.split()[3:])
            trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            newLine = newLine.translate(trans).lower()
            sentences.append(newLine)

def main():
    readData()
    percepClassify()


if __name__ == "__main__":
    main()