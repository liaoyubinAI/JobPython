import string

template_text = '''
	Delimiter:	%%
	Replaced:	%with_undersore
	Ignored	:	%notundersored
'''

d = {'with_undersore':'replaced',
	'notundersored':'not replaced',
	}

class MyTempate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'

t = MyTempate(template_text)
print "Modified ID pattern:"
print t.safe_substitute(d)
