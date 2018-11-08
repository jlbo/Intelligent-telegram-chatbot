settings = {
	'gentbot': {
		'replyrate': 15
		,"data_dir": "./data/" #data dir
		,"num_contexts": 0 # Total word contextx
		,"num_words": 0 # Total unique words known
		,"max_words": 12000 # Max limit in the number of words known
		,"learning": True # Allow the bot to learn?
		,"ignore_list": ['!.', '?.', "'", ',', ';', 'asl', 'h'] # Words to ignore
		,"no_save": False # If true, dont save to disk
                , "name": 'gentbot'
	},
	'telegram': {
		'token': 'YOUR KEY HERE'
	}
}
