import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.tokenize import sent_tokenize, word_tokenize
from readers_ import reader_data

class Analyze:

	def anlyser(sentence):
		positive_vocab = reader_data('p.txt')
		negative_vocab = reader_data('n.txt')

		 
		positive_features = [({pos: True}, 'pos') for pos in positive_vocab]
		negative_features = [({neg: True}, 'neg') for neg in negative_vocab]
		# neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
		 
		# train_set = negative_features + positive_features + neutral_features

		train_set = negative_features + positive_features 

		classifier = NaiveBayesClassifier.train(train_set) 

		# Predict
		neg = 0
		pos = 0

		sentence = sentence.lower()
		# words = sentence.split(' ')
		words = word_tokenize(sentence)

		for word in words:
		    classResult = classifier.classify({word: True})
		    print(classResult)
		    if classResult == 'neg':
		        neg = neg + 1
		    if classResult == 'pos':
		        pos = pos + 1
		print('Positive: ' + str(float(pos)/len(words)))
		print('Negative: ' + str(float(neg)/len(words)))

