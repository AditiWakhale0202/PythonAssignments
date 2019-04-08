import os.path as path
import re

dict_of_params = {'context name': 'shareinsights2','file': 'data.csv'}

source_with_param = "/v1/{{context name}}/d3/{{file}}"
only_source = "{{context}}"

p= re.compile("{{|}}")
splitsource = p.split(source_with_param)
print splitsource
only_source_split = p.split(only_source)
print only_source_split
for s in splitsource:
    if s in dict_of_params:
        print '{{' + s + '}}'
        print dict_of_params[s]
        source_with_param=source_with_param.replace('{{'+s+'}}',dict_of_params[s])
print splitsource
print source_with_param
