### Dictionary 연습1

- 단어들의 list가 input으로 들어올 때, 각 단어들을 시작 알파벳별로 저장하는 dictionary를 만들고, 그 dictionary를 리턴하는 함수를 만들어 봅시다.

- 이 dictionary는 key가 어떤 알파벳이 되고, value는 input 내의 단어들 중 key로 시작하는 단어들을 모은 list입니다.

- 예) `input = ["apple", "bear", "person", "aurora", "print", "boy"]` 이 주어져 있습니다. 만약 key가 "a" 라면, "a"에 맵핑된 value는 ["apple", "aurora"] 입니다. (단어들의 순서는 달라도 됩니다.)

- 힌트 1) dictionary 의 value는 리스트가 될 수 있습니다.
- 힌트 2) 아래 skeleton code를 사용해도 됩니다.

```python
def mk_word_dict(word_lst):
	# Initialize a word dictionanry
	word_dict = dict()

	for w in word_lst:
		# Get the starting alphabet of w
		start = ????

		# Check whether the key (== start) is in the word dictionary
		start_is_in = ????

		# If the key is not in the dictionary, 
		#  add the key in the dictionary with an empty list
		if ????:
			word_dict[????] = []

		# Add the word into the word dictionary
		word_dict[????].append(???)

	# Retrun the dictionary
	return ????

words = ["apple", "bear", "person", "aurora", "print", "boy"] 
word_dict = mk_word_dict(????)
# word_dict will be
# {"a": ["apple", "aurora"], "b": ["bear", "boy"], "p": ["person", "print"]}
words_start_with_a = word_dict[????]
print(words_start_with_a)
```



### Dictionary 연습 2

- 스트링으로 된 문장 내부에, 각 단어가 몇 번 포함되는지를 나타내는 dictionary 만들기.
- 예를 들어, sss 라는 문장이 다음과 같이 문장이 주어져 있을 때, 
  - sss = 'Love is an open door! Love is an open door! Life can be so much more!'
  - word_cnt_dict = {'Love': 2, 'is': 2, 'an': 2, 'open': 2, 'door!': 2, 'Life': 1, 'can': 1, 'be': 1, 'so': 1, 'much': 1, 'more!': 1} 를 만들어 보세요.



