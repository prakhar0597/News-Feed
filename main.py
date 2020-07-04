from flask import request

from flask import Flask, jsonify

from newsapi import NewsApiClient



app = Flask(__name__)


#newsapi = NewsApiClient(api_key='5a5163e6ec8e414a8490dcdfb7f9f223')
newsapi = NewsApiClient(api_key='dbf98eec77b6478eb88ff68e6f1aeb5a')


#--------------------------------------------------------top--------------------------------------------

top_headlines = newsapi.get_top_headlines(country='us', language='en', page_size=30)
articles = top_headlines['articles']

#z=list(articles)
#z = list(articles)
abc=[]
#count=0
#print(articles)
#print(len(z))

split_it = []
for i in range(len(articles)):
	data= articles[i]

#--------------------------------------------word---------------------------------------------------------------
	
	if data['title']!=None:
		split_it.append(data['title'].split())
		#print(data['title'])
	
#------------------------------------------------------word-----------------------------------------------------

	data2= data['source']
	if data['author']!=None and data['url']!=None and data['urlToImage']!='null' and data['urlToImage']!=None and data['publishedAt']!=None and data['content']!=None and data['title']!=None and data['description']!=None and data2['id']!= None and data2['name']!= None :
		abc.append(data)
	
#print(count)		
#print(abc)
#print(len(abc))

#------------------------------------------------------word1-----------------------------------------------------

one_list = []
for sublist in split_it:
    for item in sublist:
        one_list.append(item)
#print(one_list)

unwanted_chars = ['-','_','+','/',',','a',':', "a's", 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', "c'mon", "c's", 'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently', 'd', 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'm', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't', "t's", 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'would', 'would', "wouldn't", 'x', 'y', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'z', 'zero']
wordfreq = {}

bad_chars = [';', ':', '!', "*", "'",',','"']

for total_word in one_list:
    #word = total_word.strip(unwanted_chars)
	word = total_word.lower()
	for i in bad_chars:
    		word = word.replace(i, '')
	if word in unwanted_chars:
		continue
	if total_word not in wordfreq:
		wordfreq[total_word] = 0 
		wordfreq[total_word] += 1

#print(wordfreq)

{k: v for k, v in sorted(wordfreq.items(), key=lambda item: item[1])}

words = list(wordfreq)

#print(words)

if(len(words)>30):

	words = words[0:30]

#print(super_words)

@app.route('/to')
def get_task():
    return jsonify({'word': words})

#------------------------------------------------------word1-----------------------------------------------------


@app.route('/tod')
def get_tasks():
    return jsonify({'articles': abc})


#-------------------------------------------------top------------------------------------


#-----------------------------------------------cnn------------------------------------------

top_headlines_cnn = newsapi.get_top_headlines(sources='cnn', language='en', page_size=30)
articles_cnn = top_headlines_cnn['articles']


#z_cnn=list(articles_cnn)
articles_cn=[]

for i in range(len(articles_cnn)):
	data_cnn= articles_cnn[i]
	data2_cnn= data_cnn['source']
	if data_cnn['author']!=None and data_cnn['url']!=None and data_cnn['urlToImage']!='null' and data_cnn['urlToImage']!=None and data_cnn['publishedAt']!=None and data_cnn['content']!=None and data_cnn['title']!=None and data_cnn['description']!=None and data2_cnn['id']!= None and data2_cnn['name']!= None :
		articles_cn.append(data_cnn)



@app.route('/todo')
def get_tasks1():
    return jsonify({'articles': articles_cn})


#---------------------------------------------cnn------------------------------------------------


#--------------------------------------------fox-------------------------------------------------------------
top_headlines_foxnews = newsapi.get_top_headlines(sources='fox-news', language='en', page_size=30)
articles_foxnews = top_headlines_foxnews['articles']



#z_fox=articles_foxnews

articles_fo=[]
for i in range(len(articles_foxnews)):
	data_fox= articles_foxnews[i]
	data2_fox= data_fox['source']
	if data_fox['author']!=None and data_fox['url']!=None and data_fox['urlToImage']!='null' and data_fox['urlToImage']!=None and data_fox['publishedAt']!=None and data_fox['content']!=None and data_fox['title']!=None and data_fox['description']!=None and data2_fox['id']!= None and data2_fox['name']!= None :
		articles_fo.append(data_fox)

@app.route('/todoo')
def get_tasks2():
    return jsonify({'articles':articles_fo})

#--------------------------------------------fox-------------------------------------------------------------

#-----------------------------------sources------------------------------------------------------------------


@app.route('/sources')
def get_source():

	category = request.args.get('category')

	#print(category)

	sources = newsapi.get_sources(country='us', language='en')
	channel = sources['sources']

	source_ten=[]

	

	for i in range(len(channel)):
		data_source= channel[i]
		if category=='all' and data_source['name']!=None and data_source['id']!=None:
			source_ten.append(data_source)
		elif data_source['name']!=None and data_source['id']!=None and data_source['category']==category:
			source_ten.append(data_source)
		if(len(source_ten)==10):
			break
	return jsonify({'channel': source_ten})

#------------------------------------sources----------------------------------------------------------

#-----------------------------------sources2------------------------------------------------------------------


@app.route('/sources2')
def get_source2():

	category = request.args.get('category')

	#print(category)

	sources = newsapi.get_sources(country='us', language='en')
	channel = sources['sources']

	source_ten=[]

	

	for i in range(len(channel)):
		data_source= channel[i]
		
		if category=='all' and data_source['name']!=None and data_source['id']!=None:
			source_ten.append(data_source)
		elif data_source['name']!=None and data_source['id']!=None and data_source['category']==category:
			source_ten.append(data_source)
		if(len(source_ten)==10):
			break
	return jsonify({'channel': source_ten})

#------------------------------------sources2----------------------------------------------------------

#---------------------------------------------------get_news---------------------------------------------

@app.route('/everything')
def get_news():

	keyword = request.args.get('keyword')
	from_date = request.args.get('from_date')
	to_date = request.args.get('to_date')
	category = request.args.get('category')
	sources1 = request.args.get('sources')

	# print(sources1)
	try:
		print("go")
		if(sources1=='all'):
			all_articles = newsapi.get_everything(q=keyword, from_param=from_date, to=to_date, language='en', sort_by='publishedAt', page_size=30)
			#print(all_articles)
		else:
			all_articles = newsapi.get_everything(q=keyword, sources=sources1, from_param=from_date, to=to_date, language='en', sort_by='publishedAt', page_size=30)
		everything = all_articles['articles']

		articles_all=[]
		for i in range(len(everything)):
			all_data= everything[i]
			all_data2= all_data['source']
			print(all_data['urlToImage'])
			if all_data['author']!=None and all_data['author']!="" and all_data['url']!=None and all_data['urlToImage']!='null' and all_data['urlToImage']!=None and all_data['publishedAt']!=None and all_data['content']!=None and all_data['title']!=None and all_data['description']!=None and all_data2['id']!= None and all_data2['name']!= None :
				articles_all.append(all_data)

			if(len(articles_all)==15):
				break
		# print(articles_all)
		return jsonify({'all_articles': articles_all})
	except Exception as ex:
		print(ex)
		t = {}
		t["message"] = ex.get_message()
		t["status"] = ex.get_status()
		return jsonify(t)
#---------------------------------------------------get_news---------------------------------------------



@app.route('/')
def ren():
	return (app.send_static_file('index.html'))

if __name__ == '__main__':
    app.run(debug=True)