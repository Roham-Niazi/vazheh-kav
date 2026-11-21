import joblib
import hazm
import emoji
import string
from pathlib import Path


def emoji_token(value):
    # Letters-only encoding preserves full Unicode emoji sequences through cleanup.
    encoded = [
        "".join(chr(ord("a") + int(digit, 16)) for digit in format(ord(char), "x"))
        for char in value
    ]
    return "emojitoken" + "z".join(encoded)


class CommentAnalyzer:
	def __init__(self):
		self.normalizer=hazm.Normalizer()
		self.word_tokenizer=hazm.WordTokenizer()
		self.lemmatizer=hazm.Lemmatizer()

		BASE_DIR = Path(__file__).resolve().parent

		self.offensive_detection_pipeline=joblib.load(
			BASE_DIR / "models" / "offensive_detection_pipeline.joblib"
		)

		self.recommendation_detection_pipeline=joblib.load(
			BASE_DIR / "models" / "recommendation_detection_pipeline.joblib"
		)


	def remove_chars(self, text, chars):
		for char in chars: text=text.replace(char, " ")
		return text

	def preprocess_offensive(self, text):
		if not isinstance(text, str):
			return None
		seen_emoji = set()
		protected_tokens = set()

		def replace_emoji(value, data):
			if value in seen_emoji:
				return " "
			seen_emoji.add(value)
			token = emoji_token(value)
			protected_tokens.add(token)
			return " " + token + " "

		# Keep the first occurrence of each exact emoji sequence per comment.
		text = emoji.replace_emoji(text.lower(), replace=replace_emoji)
		text = self.remove_chars(text, string.punctuation + '؟،')
		text = self.normalizer.normalize(text).replace('آ', 'ا')
		text = self.remove_chars(text, '۰۱۲۳۴۵۶۷۸۹')
		tokens = [
			token if token in protected_tokens or token in self.lemmatizer.verbs
			else self.lemmatizer.lemmatize(token).split("#")[0]
			for token in self.word_tokenizer.tokenize(text)
		]
		return " ".join(tokens) if tokens else None

	def preprocess_recommendation(self, text):
		if not isinstance(text, str):
			return None

		text=self.remove_chars(text.lower(), string.punctuation+"؟،")
		text=self.normalizer.normalize(text).replace("آ", "ا")
		# Keep the half-space so negated verbs remain intact during tokenization.
		text=self.remove_chars(text, "۰۱۲۳۴۵۶۷۸۹")
		tokens=[
			token if token in self.lemmatizer.verbs
			else self.lemmatizer.lemmatize(token).split("#")[0]
			for token in self.word_tokenizer.tokenize(text)
		]
		return " ".join(tokens) if tokens else None


	def predict(self, comment):
		positive_idx = list(self.offensive_detection_pipeline.classes_).index(1)

		offensive_comment=self.preprocess_offensive(comment)
		recommendation_comment=self.preprocess_recommendation(comment)
		offensive_result=self.offensive_detection_pipeline.predict_proba([offensive_comment])[0, positive_idx]
		recommendation_result=self.recommendation_detection_pipeline.predict_proba([recommendation_comment])[0, 1]

		return {
			"recommendation_percent": recommendation_result,
			"offensivity_percent": offensive_result
		}


comment_analyzer=CommentAnalyzer()
