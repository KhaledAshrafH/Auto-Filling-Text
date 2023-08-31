import nltk
import re


class AutoFilling:
    def __init__(self, text, n):
        self.text = text
        self.tokens = []
        self.ngrams = {}
        self.n = n

    def tokenize(self):
        print('Tokenization process running now.')
        self.text = re.sub(r'/W', '', self.text)
        self.tokens = nltk.word_tokenize(self.text)

    def generate_ngrams(self):
        if len(self.tokens) > 0:
            print('generating ngrams process running now.')
            for i in range(len(self.tokens) - (self.n - 1)):
                seq_list = self.tokens[i:i + self.n - 1]
                seq = ""
                for word in seq_list:
                    seq += word
                    seq += " "
                seq = seq.strip()
                if seq in self.ngrams:
                    self.ngrams[seq][self.tokens[i + (self.n - 1)]] = self.ngrams[seq].get(
                        self.tokens[i + (self.n - 1)], 0) + 1
                else:
                    self.ngrams[seq] = {}
                    self.ngrams[seq][self.tokens[i + (self.n - 1)]] = 1
        else:
            print('You should tokenize the text first! tokenization process running now.')
            self.tokenize()
            self.generate_ngrams()

    def calculate_prob(self):
        if len(self.ngrams) > 0:
            print('probability calculations process running now. ')
            for prev_seq in self.ngrams:
                total_prev_cnt = 0.0
                for key in self.ngrams[prev_seq].keys():
                    total_prev_cnt += self.ngrams[prev_seq][key]

                for key in self.ngrams[prev_seq].keys():
                    self.ngrams[prev_seq][key] /= total_prev_cnt
                self.ngrams[prev_seq] = sorted(self.ngrams[prev_seq].items(), key=lambda x: (x[1], x[0]),
                                               reverse=True)

        else:
            print('You should generating ngrams first!')
            self.generate_ngrams()
            self.calculate_prob()

    def suggest_next_ngrams(self, str_input):
        res = []
        str_input.strip()

        list_input = str_input.split()
        if len(list_input) >= self.n-1:

            last_n_words = ""
            for i in range(self.n-1):
                last_n_words = last_n_words + list_input[((i+1)*-1)]
            if last_n_words in self.ngrams:
                for i in range(len(self.ngrams[last_n_words])):
                    predicted = self.ngrams[last_n_words][i]
                    res.append(predicted[0])
                    if i == 10:
                        break
        else:
            pass
        return res
